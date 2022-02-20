def dectoBin(A):
    revNum = ""
    finalNum = ""

    while( A ):
        num = A % 2
        A = A // 2
        revNum += str(num)

    for i in range(1 , len(revNum) + 1):
        finalNum +=  str(revNum[-i])

    return  finalNum



A = 10
print(dectoBin(A))



