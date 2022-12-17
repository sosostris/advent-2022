from typing import List
from day11_lib import Monkey, get_test


def init_sample_monkeys() -> List[Monkey]:
    monkey_0 = Monkey(items=[79, 98],
                      operation=lambda old: old * 19,
                      test=get_test(23, 2, 3))
    monkey_1 = Monkey(items=[54, 65, 75, 74],
                      operation=lambda old: old + 6,
                      test=get_test(19, 2, 0))
    monkey_2 = Monkey(items=[79, 60, 97],
                      operation=lambda old: old * old,
                      test=get_test(13, 1, 3))
    monkey_3 = Monkey(items=[74],
                      operation=lambda old: old + 3,
                      test=get_test(17, 0, 1))

    return [monkey_0, monkey_1, monkey_2, monkey_3]


def init_monkeys() -> List[Monkey]:
    monkey_0 = Monkey(items=[66, 59, 64, 51],
                      operation=lambda old: old * 3,
                      test=get_test(2, 1, 4))
    monkey_1 = Monkey(items=[67, 61],
                      operation=lambda old: old * 19,
                      test=get_test(7, 3, 5))
    monkey_2 = Monkey(items=[86, 93, 80, 70, 71, 81, 56],
                      operation=lambda old: old + 2,
                      test=get_test(11, 4, 0))
    monkey_3 = Monkey(items=[94],
                      operation=lambda old: old * old,
                      test=get_test(19, 7, 6))
    monkey_4 = Monkey(items=[71, 92, 64],
                      operation=lambda old: old + 8,
                      test=get_test(3, 5, 1))
    monkey_5 = Monkey(items=[58, 81, 92, 75, 56],
                      operation=lambda old: old + 6,
                      test=get_test(5, 3, 6))
    monkey_6 = Monkey(items=[82, 98, 77, 94, 86, 81],
                      operation=lambda old: old + 7,
                      test=get_test(17, 7, 2))
    monkey_7 = Monkey(items=[54, 95, 70, 93, 88, 93, 63, 50],
                      operation=lambda old: old + 4,
                      test=get_test(13, 2, 0))

    return [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]


def play_one_round(monkeys: List[Monkey]) -> None:
    for i in range(0, len(monkeys)):
        for item in monkeys[i].items:
            monkeys[i].inspection_times += 1
            new_worry = int(monkeys[i].operation(item) / 3)
            passed_to_monkey = monkeys[i].test(new_worry)
            monkeys[passed_to_monkey].items.append(new_worry)
        monkeys[i].items = []


def calc_monkey_business(monkeys: List[Monkey], rounds: int) -> int:
    for i in range(0, rounds):
        play_one_round(monkeys)

    monkeys.sort(key=lambda monkey: monkey.inspection_times, reverse=True)
    return monkeys[0].inspection_times * monkeys[1].inspection_times


def solve(rounds: int) -> None:
    monkeys = init_sample_monkeys()
    # monkeys = init_monkeys()
    monkey_business = calc_monkey_business(monkeys, rounds)
    print(f"Monkey business: {monkey_business}")


solve(20)
