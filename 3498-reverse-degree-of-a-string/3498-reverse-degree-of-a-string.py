class Solution(object):
    def reverseDegree(self, s):
        res = 0
        for i in range(len(s)):
            val = ord(s[i]) - ord('a') + 1
            reverse = 26 - val + 1
            res += (i + 1) * reverse

        return res