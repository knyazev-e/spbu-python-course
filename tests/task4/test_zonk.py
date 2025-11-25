import pytest
from project.task4.zonk import Game, BotPlayer, Die, Combination


def test_game_initialization():
    bots = [BotPlayer("TestBot")]
    game = Game(players=bots, combinations=[])

    assert game.state == False
    assert game.current_player == 0
    assert game.winner is None
    assert len(game.dice_set) == 6


def test_bot_strategies():
    cautious = BotPlayer("Cautious", strategy="cautious")
    aggressive = BotPlayer("Aggressive", strategy="aggressive")

    cautious.round_score = 300
    aggressive.round_score = 300

    assert cautious.make_decision([], None, 0) == True
    assert aggressive.make_decision([], None, 0) == True


def test_score_accumulation():
    bot = BotPlayer("TestBot")
    bot.round_score = 350
    bot.total_score = 1000

    bot.total_score += bot.round_score
    bot.round_score = 0

    assert bot.total_score == 1350
    assert bot.round_score == 0


def test_zonk_detection():
    dice = [Die(2), Die(3), Die(4), Die(6), Die(2), Die(3)]
    combinations = []

    game = Game(players=[], combinations=combinations)
    game.dice_set = dice

    assert game.zonk_check() == True


def test_turn_progression():
    bots = [BotPlayer("A"), BotPlayer("B"), BotPlayer("C")]
    game = Game(players=bots, combinations=[])

    game.current_player = 0
    game.switch_turn()
    assert game.current_player == 1

    game.switch_turn()
    assert game.current_player == 2

    game.switch_turn()
    assert game.current_player == 0


def test_win_condition():
    bots = [BotPlayer("A", total_score=10000), BotPlayer("B", total_score=5000)]
    game = Game(players=bots, combinations=[])

    assert game.win_check() == False
    assert bots[0].extra_round_used == True

    bots[1].extra_round_used = True
    assert game.win_check() == True


def test_die_initialization_and_set_value():
    die = Die()
    assert die.value == 1
    assert die.in_combination == False

    die_custom = Die(value=3, in_combination=True)
    assert die_custom.value == 3
    assert die_custom.in_combination == True

    for _ in range(50):
        die.set_value()
        assert 1 <= die.value <= 6


def test_roll():
    fixed_die = Die(value=1, in_combination=True)
    free_die = Die(value=2, in_combination=False)

    game = Game(players=[], combinations=[], dice_set=[fixed_die, free_die])
    initial_fixed = fixed_die.value

    game.roll()

    assert fixed_die.value == initial_fixed
    assert 1 <= free_die.value <= 6


def test_combination_choice_increases_score():
    player = BotPlayer("TestPlayer")
    initial_score = player.round_score

    combo = Combination(cost=150, structure=[Die(1), Die(1)])
    dice_set = [Die(1), Die(1)]

    combo.possibility_check(dice_set)
    player.choose_combination([combo], dice_set)

    assert player.round_score == initial_score + 150
    assert all(die.in_combination for die in dice_set)


def test_combination_choice_greedy_selection():
    player = BotPlayer("TestPlayer")

    low_combo = Combination(cost=50, structure=[Die(1)])
    high_combo = Combination(cost=200, structure=[Die(5), Die(5), Die(5)])
    combinations = [low_combo, high_combo]
    dice_set = [Die(1), Die(5), Die(5), Die(5)]

    for combo in combinations:
        combo.possibility_check(dice_set)

    player.choose_combination(combinations, dice_set)

    assert player.round_score >= 200


def test_possibility_check_detection():
    combo = Combination(cost=100, structure=[Die(1), Die(1), Die(1)])

    dice_possible = [Die(1), Die(1), Die(1), Die(2)]
    combo.possibility_check(dice_possible)
    assert combo.is_possible == True

    dice_impossible = [Die(1), Die(1), Die(2), Die(3)]
    combo.possibility_check(dice_impossible)
    assert combo.is_possible == False


def test_possibility_check_resets_dice_state():
    combo = Combination(cost=50, structure=[Die(5)])
    dice_set = [Die(5)]

    combo.possibility_check(dice_set)

    assert all(not die.in_combination for die in dice_set)


def test_game_initialization_with_custom_params():
    players = [BotPlayer("Bot1"), BotPlayer("Bot2")]
    combinations = [Combination(cost=100, structure=[Die(1)])]
    custom_dice = [Die(3), Die(4)]

    game = Game(
        players=players,
        combinations=combinations,
        dice_set=custom_dice,
        state=True,
        current_player=1,
    )

    assert game.players == players
    assert game.combinations == combinations
    assert game.dice_set == custom_dice
    assert game.state == True
    assert game.current_player == 1


def test_bot_player_initialization():
    bot_default = BotPlayer("DefaultBot")
    assert bot_default.strategy == "default"
    assert bot_default.total_score == 0

    bot_aggressive = BotPlayer("AggressiveBot", strategy="aggressive", total_score=500)
    assert bot_aggressive.strategy == "aggressive"
    assert bot_aggressive.total_score == 500


def test_combination_initialization():
    structure = [Die(1), Die(2), Die(3)]
    combo = Combination(cost=300, structure=structure, is_possible=True)

    assert combo.cost == 300
    assert combo.structure == structure
    assert combo.is_possible == True
