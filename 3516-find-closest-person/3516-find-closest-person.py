class Solution(object):
    def findClosest(self, x, y, z):
         return 0 if abs(x-z)==abs(y-z) else 2-(abs(x-z)<abs(y-z))