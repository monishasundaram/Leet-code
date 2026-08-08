class Solution(object):
    def trafficSignal(self, t):
        if t==0:
            return "Green"
        elif t==30:
            return "Orange"
        elif t>30 and t<=90:
            return "Red"
        else:
            return "Invalid"
