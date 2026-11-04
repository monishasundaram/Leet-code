class Solution(object):
    def maximumWealth(self, a):
        if not a:
            return 0
        m = 0
        for c in a:
            t = 0
            for b in c:
                t+=b
            if t>m:
                m = t
        return m
