import sys


def rhyme(N: int, K: int) -> int:
    applicants = list(range(1, N + 1))
    index = 0
    while len(applicants) > 1:
        index = (index + K - 1) % len(applicants)
        applicants.pop(index)
    return applicants[0]


def main():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    print(rhyme(N, K))


if __name__ == '__main__':
    main()
