"""
N light bulbs are connected by a wire.

Each bulb has a switch associated with it; however, due to faulty wiring, a switch also changes the state of all the bulbs to the right of the current bulb.

Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.

You can press the same switch multiple times.

Note: 0 represents the bulb is off and 1 represents the bulb is on.
Input Format

The first and the only argument contains an integer array A, of size N.



Output Format

Return an integer representing the minimum number of switches required.



Example Input

Input 1:

 A = [0, 1, 0, 1]
Input 2:

 A = [1, 1, 1, 1]


Example Output

Output 1:

 4
Output 2:

 0


Example Explanation

Explanation 1:

 press switch 0 : [1 0 1 0]
 press switch 1 : [1 1 0 1]
 press switch 2 : [1 1 1 0]
 press switch 3 : [1 1 1 1]
Explanation 2:

 There is no need to turn any switches as all the bulbs are already on.



"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        N = len(A)

    res = 0
    count = 0
    for i in range(N):
        if A[i] == 0 and count % 2 == 0:
            res += 1
            count += 1

        elif A[i] == 0 and count % 2 != 0:
            pass

        elif A[i] == 1 and count % 2 == 0:
            pass

        elif A[i] == 1 and count % 2 != 0:
            res += 1
            count += 1

    return res


