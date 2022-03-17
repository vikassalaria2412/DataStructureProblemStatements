def updateArr(A,index,valueReplaced):
    for idx,value in enumerate(A):
        if idx == index:
            A[idx] = valueReplaced

    print(A)



A= [1,3,5]
print(updateArr(A,1,8))