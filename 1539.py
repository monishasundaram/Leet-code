class Solution(object):
    def findKthPositive(self, arr, k):
        arra = []
        i = 1
        j = 0

        while len(arra) < k:
            if j < len(arr) and arr[j] == i:
                j += 1
            else:
                arra.append(i)

            i += 1

        return arra[k - 1]
