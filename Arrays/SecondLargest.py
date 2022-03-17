class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        largest = A[0]
        secondlargest = None
        for i in range(1, len(A)):
            if A[i] >= largest:
                secondlargest = largest
                largest = A[i]

            elif A[i] > secondlargest:
                secondlargest = A[i]

        if secondlargest == None:
            return (-1)

        else:
            return secondlargest




