class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        ans = float('inf')

        for size in range(l, r + 1):
            total = sum(nums[:size])

            if total > 0:
                ans = min(ans, total)

            for i in range(size, n):
                total += nums[i]
                total -= nums[i - size]

                if total > 0:
                    ans = min(ans, total)

        return -1 if ans == float('inf') else ans