class Solution(object):
    def checkTwoChessboards(self, c1, c2):
        s1 = ord(c1[0])+ord(c1[1])
        s2 = ord(c2[0])+ord(c2[1])
        return s1%2 == s2%2