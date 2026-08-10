class Solution(object):
    def winnerSquareGame(self, n):
        dp = {}

        def win(n):
            if n == 0:
                return False

            if n in dp:
                return dp[n]

            i = 1
            while i * i <= n:
                if not win(n - i * i):
                    dp[n] = True
                    return True
                i += 1

            dp[n] = False
            return False

        return win(n)
