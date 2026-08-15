class Solution(object):
    def mostWordsFound(self, sentences):
        count=0
        for i in sentences:
            words=i.split()
            count=max(count,len(words))
                
        return count