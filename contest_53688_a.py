import sys


def measurements_per_second(generation):
    if generation < 2:
        return 1
    return (measurements_per_second(generation - 1)
            + measurements_per_second(generation - 2))


def main():
    generation = int(sys.stdin.readline())
    print(measurements_per_second(generation))


if __name__ == '__main__':
    main()
