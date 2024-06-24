def measurements_per_second(generation):
    if generation < 2:
        return 1
    return (measurements_per_second(generation - 1)
            + measurements_per_second(generation - 2))


if __name__ == '__main__':
    print(measurements_per_second(int(input())))
