import sys


def platforms_needed(robots_weights: list[int], limit: int) -> int:
    robots_weights = sorted(robots_weights)
    left: int = 0
    right: int = len(robots_weights) - 1
    result = 0
    while left <= right:
        if robots_weights[left] + robots_weights[right] <= limit:
            left += 1
        right -= 1
        result += 1
    return result


def main():
    robots_weights = [int(weight) for weight in sys.stdin.readline().split()]
    limit = int(sys.stdin.readline())
    print(platforms_needed(robots_weights, limit))


if __name__ == '__main__':
    main()
