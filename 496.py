class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        arr = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found = -1

                    for v in range(j + 1, len(nums2)):
                        if nums2[v] > nums2[j]:
                            found = nums2[v]
                            break

                    arr.append(found)
                    break

        return arr
