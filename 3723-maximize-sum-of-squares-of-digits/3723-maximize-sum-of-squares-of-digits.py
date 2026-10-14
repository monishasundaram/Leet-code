class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num: return ""
        nines, rest = divmod(sum, 9)
        return ("9" * nines + str(rest) + "0" * num)[:num]