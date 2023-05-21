from pytest import mark

from median import Solution


@mark.parametrize('nums1, nums2', [([1, 3], [2])])
def test_median(nums1, nums2):
    res = Solution().findMedianSortedArrays(nums1, nums2)
    assert res == 2.0
