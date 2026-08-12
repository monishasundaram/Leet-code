class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        for i in range(len(arr1)):
            c1=0
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])>d:
                    c1+=1
            if c1==len(arr2):
                count+=1
        return count
