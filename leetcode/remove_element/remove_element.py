from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        forward, backward = 0, len(nums) - 1
        while backward >= forward:
            if nums[backward] == val:
                k += 1
                backward -= 1
                continue

            nums[forward], nums[backward] = nums[backward], nums[forward]
            forward += 1

        return len(nums) - k
