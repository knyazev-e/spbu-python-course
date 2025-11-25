import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from project.task4.zonk import Game, BotPlayer, Die, Combination


def create_combinations():
    combinations = []

    combinations.append(Combination(cost=100, structure=[Die(1)]))
    combinations.append(Combination(cost=50, structure=[Die(5)]))

    for number in range(1, 7):
        cost = 1000 if number == 1 else number * 100
        combinations.append(
            Combination(cost=cost, structure=[Die(number) for _ in range(3)])
        )

    for number in range(1, 7):
        triple_cost = 1000 if number == 1 else number * 100
        combinations.append(
            Combination(cost=triple_cost * 2, structure=[Die(number) for _ in range(4)])
        )

    for number in range(1, 7):
        triple_cost = 1000 if number == 1 else number * 100
        combinations.append(
            Combination(cost=triple_cost * 3, structure=[Die(number) for _ in range(5)])
        )

    for number in range(1, 7):
        triple_cost = 1000 if number == 1 else number * 100
        combinations.append(
            Combination(cost=triple_cost * 4, structure=[Die(number) for _ in range(6)])
        )

    combinations.append(Combination(cost=1500, structure=[Die(i) for i in range(1, 7)]))

    number_pairs = [
        [1, 2, 3],
        [1, 2, 4],
        [1, 2, 5],
        [1, 2, 6],
        [1, 3, 4],
        [1, 3, 5],
        [1, 3, 6],
        [1, 4, 5],
        [1, 4, 6],
        [1, 5, 6],
        [2, 3, 4],
        [2, 3, 5],
        [2, 3, 6],
        [2, 4, 5],
        [2, 4, 6],
        [2, 5, 6],
        [3, 4, 5],
        [3, 4, 6],
        [3, 5, 6],
        [4, 5, 6],
    ]

    for pair_numbers in number_pairs:
        structure = []
        for number in pair_numbers:
            structure.extend([Die(number), Die(number)])
        combinations.append(Combination(cost=1500, structure=structure))

    return combinations


def run_demo():
    print("=== ZONK GAME DEMO ===\n")

    bots = [
        BotPlayer("SafeBot", strategy="cautious"),
        BotPlayer("RiskBot", strategy="aggressive"),
        BotPlayer("BalancedBot", strategy="default"),
    ]

    combinations = create_combinations()

    print(f"Created {len(combinations)} scoring combinations:")
    print("Singles, Triples, 4/5/6 of a kind, Straights, Three pairs")

    game = Game(players=bots, combinations=combinations)
    game.winning_score = 3000

    game.start()
    print(f"The game has finished. The winner is {game.winner.name}!")


run_demo()
