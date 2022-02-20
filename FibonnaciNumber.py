"""
Given a positive integer A, write a program to find the Ath Fibonacci number.

In a Fibonacci series, each term is the sum of the previous two terms and the first two terms of the series are 0 and 1. i.e. f(0) = 0 and f(1) = 1. Hence, f(2) = 1, f(3) = 2, f(4) = 3 and so on.

NOTE: 0th term is 0. 1th term is 1 and so on.
"""
#

def fibo(A):
   a = 0
   b = 1
   for i in range(2,A + 1):
       c = a + b
       a = b
       b = c
       if i == A:
           return c

A = 50
print(fibo(A))






