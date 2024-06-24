def rhyme(N: int, K: int) -> int:
    if N == 1:
        return 1
    return (rhyme(N-1, K) + K - 1) % N + 1


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    print(rhyme(N, K))
