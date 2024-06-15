import sys


def is_regular_mountain(heights):
    len_heights = len(heights)
    index = 1
    while index < len_heights:
        if heights[index-1] >= heights[index]:
            break
        index += 1
    else:
        return False
    if index == 1:
        return False
    while index < len_heights:
        if heights[index-1] <= heights[index]:
            return False
        index += 1
    return True


def main():
    arr = [int(num) for num in sys.stdin.readline().split()]
    print(is_regular_mountain(arr))


if __name__ == '__main__':
    main()
