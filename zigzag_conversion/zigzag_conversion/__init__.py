class Solution(object):
    """
    >>> Solution().convert('PAYPALISHIRING', 3)
    'PAHNAPLSIIGYIR'
    >>> Solution().convert('PAYPALISHIRING', 4)
    'PINALSIGYAHRPI'
    >>> Solution().convert('A', 1)
    'A'
    >>> Solution().convert('AB', 1)
    'AB'
    >>> Solution().convert('ABCDE', 4)
    'ABCED'
    """

    def convert(self, s, numRows):
        if numRows == 1:
            return s
        result = ''
        for row in range(numRows):
            inc = numRows * 2 - 2
            for index in range(row, len(s), inc):
                res += s[index]
                pos = index + inc - 2 * row
                if row == 0 or row == numRows - 1:
                    continue
                if pos < len(s):
                    res += s[pos]
        return result
