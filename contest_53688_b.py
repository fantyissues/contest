import sys


def rhyme(N: int, K: int) -> int:
    result = 0
    for i in range(1, N+1):
        result = (result + K) % i
    return result + 1


def main():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    print(rhyme(N, K))


if __name__ == '__main__':
    main()
