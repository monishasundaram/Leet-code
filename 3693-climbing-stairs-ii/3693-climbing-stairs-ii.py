class Solution(object):
    def climbStairs(self, n, costs):
        costs = [0] + costs

        a, b, c = costs[n], float('inf'), float('inf')

        for i in reversed(range(n)):
            a, b, c = costs[i] + min(a + 1, b + 4, c + 9), a, b

        return a