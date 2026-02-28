from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m, n
        while i > 0 or j > 0:
            if j == 0:
                return

            if i == 0:
                for k in range(j):
                    nums1[k] = nums2[k]
                return

            if nums1[i - 1] > nums2[j - 1]:
                nums1[i + j - 1], nums1[i - 1] = nums1[i - 1], nums1[i + j - 1]
                i -= 1
                continue

            nums1[i + j - 1], nums2[j - 1] = nums2[j - 1], nums1[i + j - 1]
            j -= 1
