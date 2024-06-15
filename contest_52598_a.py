import sys


def remove_duplicates(arr):
    if len(arr) < 2:
        return arr
    arr = arr[:]
    index = 1
    duplicates = 0
    while index < len(arr):
        if arr[index-1] == arr[index]:
            arr.pop(index)
            duplicates += 1
            continue
        index += 1
    arr.extend(['_'] * duplicates)
    return arr


def main():
    n = int(sys.stdin.readline())
    arr = [int(num) for num in sys.stdin.readline().split()]
    print(*remove_duplicates(arr))


if __name__ == '__main__':
    main()
