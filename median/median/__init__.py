class Solution:
    """
    >>> Solution().findMedianSortedArrays(nums1 = [1, 3], nums2 = [2])
    2.0

    >>> Solution().findMedianSortedArrays(nums1 = [1, 2], nums2 = [3, 4])
    2.5
    """

    def findMedianSortedArrays(
        self, nums1: list[int], nums2: list[int]
    ) -> float:
        from math import ceil, floor

        nums = nums1 + nums2
        nums.sort()
        return float(
            sum(
                [nums[func((len(nums) + 1) / 2) - 1] for func in (ceil, floor)]
            )
            / 2
        )
