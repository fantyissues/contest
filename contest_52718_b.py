def max_substring_len(string):
    max_substirng_len = 0
    string_len = len(string)
    for index in range(string_len):
        substring_char_set = set()
        for subindex in range(index, string_len):
            if string[subindex] in substring_char_set:
                break
            substring_char_set.add(string[subindex])
        max_substirng_len = max(max_substirng_len, len(substring_char_set))
    return max_substirng_len


if __name__ == '__main__':
    print(max_substring_len(input()))
