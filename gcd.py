# def gcd(A,B):
#     while(B):
#         A, B = B , A % B
#     return A
# def lcm(A,B):
#     lcm = A * B/gcd(A, B )
#     return lcm
#
# A = 2
# B = 3
#
# print(lcm(A,B ))


class Solution:
    def LCM(self, A, B):
        def gcd(A,B):
            while (B):
                A, B = B, A % B
            return A

        lcm = A * B / gcd(A,B)
        return int(lcm)

A = 272
B = 1479
obj =Solution()
print(obj.LCM(A,B))


