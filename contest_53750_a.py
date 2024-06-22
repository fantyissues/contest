def decode_instructions(encoded_instructions: str) -> str:
    stack: list[tuple[int, str]] = []
    multiplier: int = 0
    instructions: str = ''

    for char in encoded_instructions:
        if char.isdigit():
            multiplier = multiplier * 10 + int(char)
        elif char == '[':
            stack.append((multiplier, instructions))
            multiplier = 0
            instructions = ''
        elif char == ']':
            multiplier, prev_instructions = stack.pop()
            instructions = prev_instructions + multiplier * instructions
            multiplier = 0
        else:
            instructions += char

    return instructions


def main():
    instructions = input()
    print(decode_instructions(instructions))


if __name__ == '__main__':
    main()
