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


if __name__ == '__main__':
    arr = [int(num) for num in input().split()]
    print(is_regular_mountain(arr))
