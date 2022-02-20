A = [12,15,21,45,67,88,99,121]

def binary_search(A,searchnumber):

    N = len(A)

    i = 0
    while(middleIndex):
        middleIndex = (N/2**i)/2
        middlevalue = A[middleIndex]
        if middlevalue < searchnumber:
            AVal = A[middlevalue:]
            Afinal = Afinal.append(AVal)

        elif middlevalue > searchnumber:
            AVal = A[:middlevalue]
            Afinal = Afinal.append(AVal)

        else:
            print()




