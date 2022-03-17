import math


def main():
    tokens = input().split()
    N = int(tokens[0])
    A = []
    for i in range(1, N + 1):
        A.append(int(tokens[i]))
        max = A[0]
        min = A[0]
        for i in range(len(A)):
            if A[i] > max:
                max = A[i]
            if A[i] < min:
                min = A[i]

    print(max, min)

    return 0


if __name__ == '__main__':
    main()