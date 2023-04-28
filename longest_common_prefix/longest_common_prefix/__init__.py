class Solution(object):
    """
    >>> Solution().longestCommonPrefix(["flower","flow","flight"])
    'fl'
    >>> Solution().longestCommonPrefix(["dog","racecar","car"])
    ''
    """

    def longestCommonPrefix(self, strs):
        result = ''
        for letters in zip(*strs):
            if not ''.join(letters).replace(letters[0], ''):
                result += letters[0]
            else:
                break
        return result
