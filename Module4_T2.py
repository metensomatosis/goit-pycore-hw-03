import random


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list[int]:
    if min_num < 1 or max_num > 1000 or min_num > max_num:
        return []

    if quantity < 1 or quantity > (max_num - min_num + 1):
        return []

    numbers: list[int] = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(numbers)


def main() -> None:
    lottery_numbers: list[int] = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)


if __name__ == "__main__":
    main()
