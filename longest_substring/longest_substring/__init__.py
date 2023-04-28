class Solution(object):
    """
    >>> Solution().lengthOfLongestSubstring('abcabcbb')
    3
    >>> Solution().lengthOfLongestSubstring('bbbbbb')
    1
    >>> Solution().lengthOfLongestSubstring('pwwkew')
    3
    >>> Solution().lengthOfLongestSubstring('')
    0
    >>> Solution().lengthOfLongestSubstring('x')
    1
    >>> Solution().lengthOfLongestSubstring('aab')
    2
    >>> Solution().lengthOfLongestSubstring('dvdf')
    3
    >>> Solution().lengthOfLongestSubstring('anviaj')
    5
    >>> Solution().lengthOfLongestSubstring('qrsvbspk')
    5
    >>> Solution().lengthOfLongestSubstring('ohvhjdml')
    6
    """

    def lengthOfLongestSubstring(self, s):
        strs = []
        val = ''
        for letter in s:
            if letter in val:
                val = val[val.index(letter) + 1 :] + letter
            else:
                val += letter
            strs.append(len(val))
        return max(strs) if strs else len(s)
