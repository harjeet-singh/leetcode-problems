from typing import List

from itertools import combinations


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sums = []
        odd_numbers = filter(lambda x: x % 2 != 0, range(len(arr) + 1))
        for n in list(odd_numbers):
            for i in range(len(arr) - n + 1):
                sums.append(sum(arr[i:i + n]))

        return sum(sums)


print(Solution().sumOddLengthSubarrays(arr=[10, 11, 12]))
