def define_insert_index(arr, desire_value):
    for index, value in enumerate(arr):
        if value >= desire_value:
            return index
    return len(arr)


if __name__ == '__main__':
    arr = [int(num) for num in input().split()]
    value = int(input())
    print(define_insert_index(arr, value))
