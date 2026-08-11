class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        left = 0
        right = 0

        for i in nums1:
            if i in nums2:
                left += 1
        
        for j in nums2:
            if j in nums1:
                right += 1
        
        return [left, right]
