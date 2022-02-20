
A =  [3, 4, 4, 6]
B =  [20, 4, 10, 2]
def mobilephones(A,B):
    emptyarray = []
    for i in range(len(B)):
        count = 0
        sum = 0
        for j in range(len(A)):
            sum = sum + A[j]
            if (sum <= B[i]):
                count += 1

        emptyarray.append(count)
    return emptyarray











print(mobilephones(A,B))



