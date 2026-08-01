class Solution(object):
    def clearDigits(self, s):
        a = ""
        for ch in s:
            if ch.isalpha():
                a += ch
            else:
                a = a[:-1]
        return a
