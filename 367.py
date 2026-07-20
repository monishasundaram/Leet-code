class Solution(object):
    def isPerfectSquare(self, num):
        odd = 1
        while num > 0:
            num -= odd
            odd += 2
        return num == 0
