
num1 = [1,2,2,3,7]
num2 = [7,8,2,7]
def Intersection(num1,num2):
    num1 = set(num1)
    num2 = set(num2)
    num1 = list(num1)
    num2 = list(num2)
    newArray = []
    for i in range(len(num1)):
        for j in range(len(num2)):
            if num1[i] == num2[j]:
                newArray.append(num1[i])

    return newArray




print(Intersection(num1,num2))

