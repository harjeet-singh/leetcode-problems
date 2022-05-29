from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for w in accounts:
            sum_w = sum(w)
            if sum_w > max_wealth:
                max_wealth = sum_w
        return max_wealth


# def maximumWealth(self, accounts):
#     return max(map(sum, accounts))
