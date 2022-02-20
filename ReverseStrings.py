def Reverse(A):
    reversestring = ''
    A = A.split()
    reversestring = ""
    for i in range(len(A)):
        temp = A[i]
        for j in range(1,len(temp)  + 1):
            char = temp[-j]
            reversestring += char
            if j == len(temp):
                reversestring += " "

    print(reversestring)





A = "Everyone loves data science"
print(Reverse(A))

#############################
A = "Everyone loves data science"
A = A.split()
print(A)
