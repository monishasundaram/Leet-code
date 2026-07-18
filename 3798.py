class Solution(object):
    def largestEven(self, s):
        while s and s[-1] == '1':
            s = s[:-1]
        return s
