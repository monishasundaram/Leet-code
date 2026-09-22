class Solution(object):
    def countConsistentStrings(self, allowed, words):
        c = 0
        for n in words:
            if all(char in allowed for char in n):
                c+=1
        return c