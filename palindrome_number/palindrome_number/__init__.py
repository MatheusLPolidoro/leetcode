class Solution(object):
    """
    >>> Solution().isPalindrome(121)
    True
    >>> Solution().isPalindrome(-121)
    False
    >>> Solution().isPalindrome(10)
    False
    """

    def isPalindrome(self, x):
        return str(x)[::-1] == str(x)
