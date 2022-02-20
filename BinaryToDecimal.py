def BinToDec(A):
    decnumber = 0
    counter = 0
    while(A):

        mod = A % 10
        decnumber += mod * 2 ** counter
        A = A // 10
        counter += 1
    print(decnumber)

A = 1010
BinToDec(A)

