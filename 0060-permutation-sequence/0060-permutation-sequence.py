class Solution(object):
    def getPermutation(self, n, k):
        num = [str(i) for i in range(1,n+1)]
        fah = 1
        for i in range(1,n):
            fah*=i
        k-=1
        ans = ""

        while num:
            ind = k // fah
            ans+=num.pop(ind)
            k%=fah
            if num:
                fah//=len(num)
        
        return ans