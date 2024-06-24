def count_blocks(arr: list[int]) -> int:
    blocks = 0
    len_blocks = 0
    for step in range(len(arr)):
        if len_blocks < arr[step]:
            len_blocks = arr[step]
        if len_blocks == step:
            blocks += 1
    return blocks


if __name__ == '__main__':
    n = int(input())
    arr = [int(num) for num in input().split()]
    print(count_blocks(arr))
