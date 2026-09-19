class Solution:
    def checkOverlap(self, r, cx, cy, x1, y1, x2, y2):
        x = max(x1, min(cx, x2)) - cx
        y = max(y1, min(cy, y2)) - cy

        return x * x + y * y <= r * r