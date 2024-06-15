import sys


def define_insert_index(arr, desire_value):
    for index, value in enumerate(arr):
        if value >= desire_value:
            return index
    return len(arr)


def main():
    arr = [int(num) for num in sys.stdin.readline().split()]
    value = int(sys.stdin.readline())
    print(define_insert_index(arr, value))


if __name__ == '__main__':
    main()
