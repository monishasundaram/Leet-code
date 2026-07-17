class Solution(object):
    def maximumWealth(self, accounts):
        if not accounts:
            return 0
        max_wealth = 0
        for customer in accounts:
            total = 0
            for bal in customer:
                total += bal
            if total > max_wealth:
                max_wealth = total
        return max_wealth
