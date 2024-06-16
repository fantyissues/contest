import sys


def pattern_sorted(arr: list[int], pattern: list[int]) -> list[int]:
    arr = arr[:]
    len_arr = len(arr)
    offset = 0
    for value in pattern:
        for index in range(len_arr):
            if value == arr[index]:
                arr[offset], arr[index] = arr[index], arr[offset]
                offset += 1
    arr[offset:len_arr] = sorted(arr[offset:len_arr])
    return arr


def main():
    n = int(sys.stdin.readline())
    containers = [int(num) for num in sys.stdin.readline().split()]
    m = int(sys.stdin.readline())
    pattern = [int(num) for num in sys.stdin.readline().split()]
    print(*pattern_sorted(containers, pattern))


if __name__ == '__main__':
    main()
