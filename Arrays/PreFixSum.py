def prefix(nums):
    P = [nums[0]]
    for x in nums[1:]:
        P.append(x + P[-1])

    print(sumcal(left,right,P))


def sumcal(left,right,P):
    if left == 0:
        prefixsumval = P[right]
    elif left <= right:
        prefixsumval = P[right] -  P[left -1]

  

    return prefixsumval


#nums = [2,4,7,8,1,9,22,56]
nums = [-2,0,3,-5,2,-1]
#[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]



left = 2
right = 5
print(prefix(nums))