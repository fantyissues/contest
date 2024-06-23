from string import digits


def decode_instructions(encoded_instructions: str) -> str:
    stack: list[tuple[int, str]] = []
    multiplier: str = ''
    instructions: str = ''

    for char in encoded_instructions:
        if char in digits:
            multiplier += char
        elif char == '[':
            stack.append((int(multiplier), instructions))
            multiplier = ''
            instructions = ''
        elif char == ']':
            repeat, prev_instructions = stack.pop()
            instructions = prev_instructions + repeat * instructions
        else:
            instructions += char

    return instructions


def main():
    instructions = input()
    print(decode_instructions(instructions))


if __name__ == '__main__':
    main()
