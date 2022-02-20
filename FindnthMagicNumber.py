"""
Given an integer A, find and return the Ath magic number.

A magic number is defined as a number which can be expressed as a power of 5 or sum of unique powers of 5.

First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….
"""

def magicNum(A):
   power = 1
   answer = 0
   while(A):
       power = power * 5
       if ( A & 1):
           answer += power

       A >>= 1
   return answer
A = 5
print(magicNum(A))
