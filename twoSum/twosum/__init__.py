class Solution(object):
    """
    >>> Solution().twoSum([2, 7, 11, 15], 9)
    [0, 1]
    >>> Solution().twoSum([3, 2, 4], 6)
    [1, 2]
    >>> Solution().twoSum([3, 3], 6)
    [0, 1]
    """

    def twoSum(self, nums, target):
        rest = {num: index for index, num in enumerate(nums)}
        for index, num in enumerate(nums):
            if target - num in rest and rest[target - num] != index:
                return [index, rest[target - num]]
