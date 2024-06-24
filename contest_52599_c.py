def is_correct_sequence(bracket_sequence):
    bracket_mapping = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in bracket_sequence:
        if char in bracket_mapping:
            open_bracket = stack.pop() if stack else '!'
            if open_bracket != bracket_mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack


if __name__ == '__main__':
    print(is_correct_sequence(input()))
