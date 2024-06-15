import sys


def rhyme(N: int, K: int) -> int:
    if N == 1:
        return 1
    return (rhyme(N-1, K) + K - 1) % N + 1


def main():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    print(rhyme(N, K))


if __name__ == '__main__':
    main()
