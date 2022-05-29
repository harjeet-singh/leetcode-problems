from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        global nums_input
        nums_input = nums
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                for k in range(i, len(nums) - 1):
                    nums[k] = nums[k + 1]
                nums[len(nums) - 1] = 0


nums_input = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums_input)
