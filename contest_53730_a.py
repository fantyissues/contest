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


if __name__ == '__main__':
    n = int(input())
    containers = [int(num) for num in input().split()]
    m = int(input())
    pattern = [int(num) for num in input().split()]
    print(*pattern_sorted(containers, pattern))
