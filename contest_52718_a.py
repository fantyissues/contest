import sys


def count_numbers_less_specified(numbers):
    num_amount = [0] * (max(numbers) + 1)
    for number in numbers:
        num_amount[number] += 1
    result = [sum(num_amount[0:number]) for number in numbers]
    return result


def main():
    numbers = [int(num) for num in sys.stdin.readline().split()]
    print(*count_numbers_less_specified(numbers))


if __name__ == '__main__':
    main()
