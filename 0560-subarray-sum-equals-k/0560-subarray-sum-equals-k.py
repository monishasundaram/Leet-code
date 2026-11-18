class Solution(object):
    def subarraySum(self, nums, k):
        p = 0
        c = 0
        pm = {0:1}
        for n in nums:
            p += n
            if p-k in pm:
                c += pm[p-k]
            pm[p] = pm.get(p,0)+1

        return c