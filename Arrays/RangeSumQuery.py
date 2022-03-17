"""
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.

Problem Constraints
1 <= N, M <= 105
1 <= A[i] <= 109
1 <= L <= R <= N


Input Format
The first argument is the integer array A.
The second argument is the 2D integer array B.


Output Format
Return an integer array of length M where ith element is the answer for ith query in B.
"""
def rangeSum( A, B):
    N = len(A)
    M = len(B)
    prefixSum = [A[0]]
    for x in A[1:]:
        prefixSum.append(x + prefixSum[-1])
        prefixsumvalue = []
    for j in (B):
        left = j[0] - 1
        right = j[1] - 1
        if left == 0:
            prefixsumvalue.append(prefixSum[right])
        else:
            if left <= right:
                prefixsumvalue.append(prefixSum[right] - prefixSum[left - 1])
            else:
                prefixsumvalue.append(prefixSum[right])

    return prefixsumvalue


A = [1, 2, 3, 4, 5]
B = [[1, 4], [2, 3]]


print(rangeSum(A,B))



