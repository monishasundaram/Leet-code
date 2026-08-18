class Solution(object):
    def largestInteger(self, nums, k):
        count = {}

        for i in range(len(nums) - k + 1):
            sub = set(nums[i:i+k])

            for n in sub:
                count[n] = count.get(n, 0) + 1

        ans = -1

        for n in count:
            if count[n] == 1:
                ans = max(ans, n)

        return ans