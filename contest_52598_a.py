def remove_duplicates(arr):
    len_arr = len(arr)
    if len_arr < 2:
        return arr
    result = [arr[0]]
    duplicates = 0
    for index in range(1, len_arr):
        if arr[index-1] == arr[index]:
            duplicates += 1
            continue
        result.append(arr[index])
    result.extend(['_'] * duplicates)
    return result


if __name__ == '__main__':
    n = int(input())
    arr = [int(num) for num in input().split()]
    print(*remove_duplicates(arr))
