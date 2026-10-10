class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        d = [0] * 100001
        k = k1 + k2
        total_sum = 0
        max_diff = 0
        
        for n1, n2 in zip(nums1, nums2):
            diff = abs(n1 - n2)
            d[diff] += 1
            total_sum += diff
            if diff > max_diff:
                max_diff = diff
                
        if total_sum <= k:
            return 0
            
        for i in range(max_diff, 0, -1):
            if k <= 0:
                break
            if d[i] > 0:
                move = min(k, d[i])
                d[i] -= move
                d[i - 1] += move
                k -= move
                
        ans = 0
        for i in range(1, max_diff + 1):
            if d[i] > 0:
                ans += i * i * d[i]
                
        return ans