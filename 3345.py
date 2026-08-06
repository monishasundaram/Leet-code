class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            pro = 1
            num = n

            while num > 0:
                pro *= num % 10
                num //= 10

            if pro % t == 0:
                return n

            n += 1
