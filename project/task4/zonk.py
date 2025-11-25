from typing import List, Optional
import random


class Game:
    """
    Main game controller for Zonk.

    Manages game state, player turns, dice rolling, scoring, and win conditions.
    Coordinates between players, dice, and scoring combinations.

    Attributes:
        winning_score (int): Target score to win the game (default: 10000)
        players (List[BotPlayer]): List of bot players in the game
        combinations (List[Combination]): All possible scoring combinations
        dice_set (List[Die]): Six dice used in the game
        state (bool): Whether game is currently running
        winner (Optional[BotPlayer]): The winning player when game ends
        current_player (int): Index of player whose turn it is
    """

    winning_score: int = 10000

    def __init__(
        self,
        players: List["BotPlayer"],
        combinations: List["Combination"],
        dice_set: List["Die"],
        state: bool = False,
        winner: Optional["BotPlayer"] = None,
        current_player: int = 0,
    ):
        """
        Initialize a new Zonk game.

        Args:
            players: List of bot players participating
            combinations: All possible scoring combinations for the game
            dice_set: Six dice for the game (defaults to new dice if None)
            state: Initial game state (default: False - not started)
            winner: Initial winner (default: None)
            current_player: Starting player index (default: 0)
        """
        if dice_set is None:
            dice_set = [Die() for _ in range(6)]

        self.players = players
        self.combinations = combinations
        self.dice_set = dice_set
        self.state = state
        self.winner = winner
        self.current_player = current_player

    def start(self):
        """Start the main game loop and run until completion."""
        self.state = True

        while self.state:
            for die in self.dice_set:
                die.in_combination = False

            if any(player.extra_round_used for player in self.players) and not (
                self.players[self.current_player].make_decision(
                    self.dice_set, self.winner, 2
                )
            ):
                if self.win_check():
                    self.state = False

                    for player in self.players:
                        if player.total_score > self.winner.total_score:
                            self.winner = player

                    self.display()

                self.switch_turn()
                continue

            self.display()
            self.roll()
            if self.zonk_check():
                print("ZONK")
                self.display()
                self.switch_turn()
                continue
            while self.players[self.current_player].make_decision(
                self.dice_set, self.winner, 0
            ) and not (all(die.in_combination for die in self.dice_set)):
                self.roll()
                if not (self.zonk_check()):
                    self.players[self.current_player].choose_combination(
                        self.combinations, self.dice_set
                    )
                    self.display()
                else:
                    self.players[self.current_player].round_score = 0
                    print("ZONK")
                    self.display()
                    break

            if all(die.in_combination for die in self.dice_set):
                for die in self.dice_set:
                    die.in_combination = False
                if self.players[self.current_player].make_decision(
                    self.dice_set, self.winner, 1
                ):
                    self.roll()
                    if not (self.zonk_check()):
                        self.players[self.current_player].choose_combination(
                            self.combinations, self.dice_set
                        )
                    else:
                        print("ZONK")
                        self.display()
                        self.players[self.current_player].round_score = 0

            self.players[self.current_player].total_score += self.players[
                self.current_player
            ].round_score
            self.players[self.current_player].round_score = 0

            if self.win_check():
                self.state = False

                for player in self.players:
                    if player.total_score > self.winner.total_score:
                        self.winner = player

                self.display()

            self.switch_turn()

    def switch_turn(self):
        """Advance to the next player's turn."""
        self.current_player = (self.current_player + 1) % len(self.players)

    def win_check(self) -> bool:
        """
        Check if game should end and handle extra rounds.

        Returns:
            bool: True if game should end, False otherwise
        """
        if any(player.total_score >= self.winning_score for player in self.players):
            if all(player.extra_round_used for player in self.players):
                return True
            else:
                if self.winner is None:
                    self.winner = self.players[self.current_player]
                self.players[self.current_player].extra_round_used = True

        return False

    def zonk_check(self) -> bool:
        """
        Check if current dice roll resulted in a Zonk (no scoring combinations).

        Returns:
            bool: True if Zonk (no scoring combinations), False otherwise
        """
        for combination in self.combinations:
            combination.possibility_check(self.dice_set)
            if combination.is_possible:
                return False
        return True

    def roll(self):
        """Roll all dice that are not currently in scoring combinations."""
        for die in self.dice_set:
            if not (die.in_combination):
                die.set_value()

    def display(self):
        """Display current game state to the console."""
        current = self.players[self.current_player]
        print(f"\n--- {current.name}'s Turn (Strategy: {current.strategy}) ---")
        print(f"Dice: {[d.value for d in self.dice_set if not d.in_combination]}")
        print(f"Turn Score: {current.round_score} | Total: {current.total_score}")


class BotPlayer:
    """
    An AI player for Zonk with configurable strategy.

    Attributes:
        name (str): Player identifier
        total_score (int): Accumulated score across all turns
        round_score (int): Score accumulated in current turn
        strategy (str): Decision-making strategy ('default', 'cautious', 'aggressive')
        extra_round_used (bool): Whether player has used their extra round
    """

    def __init__(
        self,
        name: str,
        total_score: int = 0,
        round_score: int = 0,
        strategy: str = "default",
        extra_round_used: bool = False,
    ):
        """
        Initialize a bot player.

        Args:
            name: Player name for display
            total_score: Starting total score (default: 0)
            round_score: Starting round score (default: 0)
            strategy: Decision strategy (default: 'default')
            extra_round_used: Whether extra round was used (default: False)
        """
        self.name = name
        self.total_score = total_score
        self.round_score = round_score
        self.strategy = strategy
        self.extra_round_used = extra_round_used

    def make_decision(
        self,
        dice_set: List["Die"],
        winner: Optional["BotPlayer"],
        decision_id: int = 0,
    ) -> bool:
        """
        Make strategic decision based on current game state.

        Args:
            dice_set: Current dice state
            winner: Current winning player (for extra round decisions)
            decision_id: Type of decision to make:
                0 = Roll again vs Bank points
                1 = Take prize roll after hot dice
                2 = Take extra round when available

        Returns:
            bool: True to take the risky option, False to play safe
        """
        if decision_id == 0:
            if self.strategy == "default":
                free_dice = 0
                for die in dice_set:
                    if not die.in_combination:
                        free_dice += 1
                return self.round_score < 500 and free_dice > 2
            elif self.strategy == "cautious":
                return self.round_score < 400
            elif self.strategy == "aggressive":
                return self.round_score < 700

        elif decision_id == 1:
            if self.strategy == "default":
                return self.round_score < 600
            elif self.strategy == "cautious":
                return False
            elif self.strategy == "aggressive":
                return True

        elif decision_id == 2:
            if self.strategy == "default" or self.strategy == "aggressive":
                return True
            elif self.strategy == "cautious":
                return (
                    (winner.total_score - self.total_score) <= 1500 if winner else False
                )

        return False

    def choose_combination(
        self, combinations: List["Combination"], dice_set: List["Die"]
    ):
        """
        Choose scoring combinations from available dice using greedy algorithm.

        Always selects the highest-scoring available combination until no more can be scored.

        Args:
            combinations: All possible scoring combinations
            dice_set: Current dice to score from
        """
        valid_combinations = [c for c in combinations if c.is_possible]
        while valid_combinations:
            max_cost: int = 0
            chosen_combo: Optional["Combination"] = None
            for c in valid_combinations:
                if c.cost >= max_cost:
                    max_cost = c.cost
                    chosen_combo = c

            self.round_score += max_cost
            if chosen_combo:
                for used_die in chosen_combo.structure:
                    for die in dice_set:
                        if not die.in_combination and die.value == used_die.value:
                            die.in_combination = True
                            break

            for c in combinations:
                c.possibility_check(dice_set)
            valid_combinations = [c for c in combinations if c.is_possible]


class Die:
    """
    Represents a single six-sided die in the game.

    Attributes:
        value (int): Current face value (1-6)
        in_combination (bool): Whether die is currently part of a scoring combination
    """

    def __init__(self, value: int = 1, in_combination: bool = False):
        """
        Initialize a die.

        Args:
            value: Starting face value (default: 1)
            in_combination: Whether in scoring combination (default: False)
        """
        self.value = value
        self.in_combination = in_combination

    def set_value(self):
        """Roll the die to get a new random value between 1 and 6."""
        self.value = random.randint(1, 6)


class Combination:
    """
    Represents a scoring combination in Zonk.

    A combination defines a pattern of dice values and their associated point value.

    Attributes:
        cost (int): Point value of this combination
        structure (List[Die]): Pattern of dice required for this combination
        is_possible (bool): Whether this combination can be formed with current dice
    """

    def __init__(
        self,
        cost: int,
        structure: List["Die"],
        is_possible: bool = False,
    ):
        """
        Initialize a scoring combination.

        Args:
            cost: Point value when combination is scored
            structure: Required dice pattern for this combination
            is_possible: Initial possibility state (default: False)
        """
        self.cost = cost
        self.structure = structure
        self.is_possible = is_possible

    def possibility_check(self, dice_set: List["Die"]):
        """
        Check if this combination can be formed with the current dice.

        Temporarily marks dice to test the combination, then resets them.

        Args:
            dice_set: Current dice to check against
        """
        modified_dice: List["Die"] = []

        for desired_die in self.structure:
            for present_die in dice_set:
                if (
                    not present_die.in_combination
                    and present_die.value == desired_die.value
                ):
                    present_die.in_combination = True
                    modified_dice.append(present_die)
                    break

        self.is_possible = len(modified_dice) == len(self.structure)

        for die in modified_dice:
            die.in_combination = False
