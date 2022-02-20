class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        middle = 0
        while (start <= end):
            middle = (start + end) // 2
            if guess(middle) == 1:
                start = middle + 1
            elif guess(middle) == -1:
                end = middle - 1

            else:
                return middle


# def guess(number):
#     if number >