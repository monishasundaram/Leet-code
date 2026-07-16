class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        out = []
        maximum = max(candies)

        for i in candies:
            if i + extraCandies >= maximum:
                out.append(True)
            else:
                out.append(False)

        return out
