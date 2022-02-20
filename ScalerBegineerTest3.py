
def stringcheck(A):
    N = len(A)

    for i in range(N):
        if A[i] != "a":
            if A[i] != 'b':
                return ("No")
    if 'b' not in A:
        return ('No')
    idA = -1
    idB = N

    for i in range(N):
        if A[i] == 'a':
            idA = i
        else:
            break
    for i in range(N - 1,0,-1):
        if A[i] == 'b':
            idB = i

        else:
            break
    if (idA + 1 != idB):
        return ("No")
    return('Yes')









#A = "aaaabbbbbbaaaaabbbbbb"
#A = "ab"
#A = "aaaabbbb"
#A = "aaaa"
#A = "bbbb"
#A = "axb"
A = "aaabbbb"
print(stringcheck(A))
