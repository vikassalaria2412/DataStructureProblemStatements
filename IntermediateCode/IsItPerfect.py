# def isPerfect(A):
#     #N = int(input())
#    # in range(A):
#         count = 0
#        # A = int(input())
#         for i in range(1, A + 1):
#             if i < A:
#                 if A % i == 0:
#                     count += i
#                 if count > A:
#                     break
#
#         if count == A:
#             print('YES')
#
#         else:
#             print('NO')
#
#
#
# #A = 24
# print(isPerfect(6))
# # if __name__ == '__main__':
# #     main()

def main():
    N = int(input())
    for i in range(N):
        count = 0
        A = int(input())
        for i in range(1, A + 1):
            if i < A:
                if A % i == 0:
                    count += i
                if count > A:
                    break

        if count == A:
            print('YES')

        else:
            print('NO')

    return 0


if __name__ == '__main__':
    main()