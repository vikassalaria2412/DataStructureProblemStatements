# N = int(input())
# i = 1
#
# while (i <= N):
#     sum = 0
# while (i > 0):
#     rem = i % 10
#     sum += (rem * rem * rem)
#     i = i // 10
# i += 1
# if sum == N:
#     print(N, end="/n")

"""
2nd approach by me
"""

# def Armstrong(N):
#    #N = int(input())
#     for i in range(1, N + 1):
#         sum = 0
#         compare = i
#         while ( i > 0):
#             rem = i % 10
#             sum = sum + (rem * rem * rem)
#             i = i // 10
#             if i == 0:
#                 if sum == compare:
#                     print(sum)
#
#
#         i += 1
#
#    # return 0
#
# N = 100
#
# print(Armstrong(100))
"""
second approach by me scaler
"""


def main():
    N = int(input())
    for i in range(1, N + 1):
        sumV = 0
        compare = i
        while (i > 0):
            rem = i % 10
            sumV = sumV + (rem * rem * rem)
            i = i // 10
            if i == 0:
                if sumV == compare:
                    print(compare)

        i += 1

    return 0


if __name__ == '__main__':
    main()

##########################
def armstrong(n):
    while(n):
        temp = n
        sumV = 0
        rem = n % 10
        sumV += (rem*rem*rem)
        n = n // 10
    if sumV == n:
        return True
    else:
        return False

def main():
    n = int(input())
    for i in range(1, n + 1):
        if (armstrong(i) == True):
            print(i)

    return 0
