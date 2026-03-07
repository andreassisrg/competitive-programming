from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        count = 0
        while left < len(nums) and right < len(nums):
            if left == 0:
                count += 1
                left += 1
                right += 1
                continue

            if nums[left] == nums[left - 1]:
                count += 1
            else:
                count = 1

            if count > 2 or nums[left] < nums[left - 1]:
                while True:
                    right += 1
                    if right >= len(nums):
                        return left

                    if nums[right] > nums[left]:
                        if (
                            nums[right] == nums[left - 1]
                            and nums[right] == nums[left - 2]
                        ):
                            continue

                        nums[left], nums[right] = nums[right], nums[left]
                        break
                count = 1

            left += 1

        return left
