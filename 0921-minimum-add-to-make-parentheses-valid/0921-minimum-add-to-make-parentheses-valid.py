class Solution(object):
    def minAddToMakeValid(self, s):
        opened = added = 0
        for ch in s:
            if ch == "(":
                opened += 1
            elif opened:  # close a pending "("
                opened -= 1
            else:  # ")" with nothing to close -> add a "("
                added += 1
        return added + opened