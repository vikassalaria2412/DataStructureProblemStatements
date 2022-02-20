# def Least(A,B):
#     if A > B:
#         greatest = A
#     else:
#         greatest = B
#
#     while (True):
#         if greatest % A == 0 and greatest % B == 0:
#             lcm = greatest
#             break
#         greatest += 1
#
#     return lcm

# Alternative

class Solution():
    def Least(self , A, B):
        def gcd(A , B):
            while(B):
                A , B = B , A % B
            return B
        lcm = A * B / gcd(A,B)
        return int(lcm)
