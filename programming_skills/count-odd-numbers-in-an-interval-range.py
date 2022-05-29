class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = (high - low)
        if low % 2 != 0 and high % 2 != 0:
            return int((diff + 1) / 2) + 1
        else:
            return int((diff + 1) / 2)


print(Solution().countOdds(low=3, high=7))
