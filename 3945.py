class Solution(object):
    def digitFrequencyScore(self, n):
        s = str(n)
        ans = 0
        for i in range(10):
            ans += i*s.count(str(i))
        return ans
