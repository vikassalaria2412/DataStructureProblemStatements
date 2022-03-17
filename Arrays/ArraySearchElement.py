def main():
    T = int(input())
    for t in range(T):
        tokens = input().split()
        N = int(tokens[0])
        A = []
        for i in range(1, N + 1):
            A.append(int(tokens[i]))
        count = 0
        B = int(input())
        for i in range(N):
            if B == A[i]:
                count += 1

        if count >= 1:
            print(1)

        else:
            print(0)

    return 0


if __name__ == '__main__':
    main()