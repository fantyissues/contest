def count_numbers_less_specified(numbers):
    num_amount = [0] * (max(numbers) + 1)
    for number in numbers:
        num_amount[number] += 1
    result = [sum(num_amount[0:number]) for number in numbers]
    return result


if __name__ == '__main__':
    numbers = [int(num) for num in input().split()]
    print(*count_numbers_less_specified(numbers))
