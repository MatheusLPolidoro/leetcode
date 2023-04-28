class Solution(object):
    """
    >>> Solution().longestPalindrome('babad')
    'bab'
    >>> Solution().longestPalindrome('cbbd')
    'bb'
    >>> Solution().longestPalindrome('abcba')
    'abcba'
    >>> Solution().longestPalindrome('aacabdkacaa')
    'aca'
    >>> Solution().longestPalindrome('bacabab')
    'bacab'
    >>> Solution().longestPalindrome('xaabacxcabaaxcabaax')
    'xaabacxcabaax'
    """

    def longestPalindrome(self, s):
        opts = [num for num in range(len(s), 0, -1)]
        for length, opt in zip(opts, opts[::-1]):
            for start in range(opt):
                val = s[start:length]
                length += 1
                if val == val[::-1]:
                    return val
