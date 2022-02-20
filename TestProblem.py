# A= [3, 5, 6, 99, 43, 55, 49,9,43,21], target_sum = 148
# B = [3,5,6,9,21,43,43,49,55,99]
# Three Sum
# Pseudo code
"""
# Input the array and calculate length of array
# input target number
#

"""
# A = [3, 5, 6, 99, 43, 55, 49, 9, 43, 21]
# target_sum = 148
# B = [3,5,6,9,21,43,43,49,55,99]
def sumArray(arrVAlue,target):
    B = sorted(arrVAlue)
    N = len(B)
    emptydic = {}
    for i in range(len(B)):

        start, last = i + 1, N-1
        while(start < last):
            if target > B[i] + B[start] + B[last]:
                start += 1

            elif target < B[i] + B[start] + B[last]:
                last -= 1

            else:
                i,start,last


A = [3, 5, 6, 99, 43, 55, 49, 9, 43, 21]
target_sum = 148
sumArray(A,target_sum)





