import sys


def satisfied_customers(orders: list[int], samples: list[int]) -> int:
    orders = sorted(orders, reverse=True)
    samples = sorted(samples, reverse=True)
    len_orders = len(orders)
    len_samples = len(samples)
    order_index = 0
    sample_index = 0
    satisfied = 0
    while order_index < len_orders and sample_index < len_samples:
        if orders[order_index] > samples[sample_index]:
            order_index += 1
            continue
        satisfied += 1
        order_index += 1
        sample_index += 1
    return satisfied


def main():
    n = int(sys.stdin.readline())
    orders = [int(num) for num in sys.stdin.readline().split()]
    m = int(sys.stdin.readline())
    samples = [int(num) for num in sys.stdin.readline().split()]
    print(satisfied_customers(orders, samples))


if __name__ == '__main__':
    main()
