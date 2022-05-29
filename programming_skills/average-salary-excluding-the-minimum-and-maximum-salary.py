from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)


print(Solution().average(salary=[4000, 3000, 1000, 2000]))
