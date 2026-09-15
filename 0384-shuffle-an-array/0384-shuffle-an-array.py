class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.original = nums[:]

    def reset(self):
        return self.original

    def shuffle(self):
        shuffled = self.nums[:]
        for i in range(len(shuffled) - 1, 0, -1):
            j = random.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()