from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        k, seen = 1, 0
        while k < len(nums):
            if nums[k] <= nums[k - 1]:
                while nums[seen] <= nums[k - 1]:
                    seen += 1
                    if seen == len(nums):
                        return k

                nums[k], nums[seen] = nums[seen], nums[k]

            k += 1

        return k
