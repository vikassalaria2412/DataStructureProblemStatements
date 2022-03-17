"""
I Count good pairs
given a strings
48 characters
all letters an lowercase
Count the number of pairs i j such that
i j and sci a and s j ig e
given String S count the no f occurrences
of the subsequence ag
"""
def goodpair(A):
    N = len(A)
    gcount = [0] * N
    count = 0

    for i in range(N-1,-1,-1):
        if A[i] =='g':
            count += 1
        gcount[i] = count
    countNew = 0
    for i in range(N):
        if A[i] == 'a':
            countNew += gcount[i]

    return countNew

A = 'baxaghygxag'
############################# Best Solution
def carryforward(A):
    n = len(A)
    gs= 0
    count  = 0

    for i in range(n-1,-1,-1):
        if A[i] == 'a':
            count += gs
        elif A[i] == 'g':
            gs += 1


        else:
            if A[i] == 'a':
                As += 1



print(goodpair(A))



