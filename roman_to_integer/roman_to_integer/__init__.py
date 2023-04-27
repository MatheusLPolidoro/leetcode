class Solution(object):
    """
    >>> Solution().romanToInt('III')
    3
    >>> Solution().romanToInt('LVIII')
    58
    >>> Solution().romanToInt('MCMXCIV')
    1994
    """

    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        prev = result = 0
        for a in s.upper()[::-1]:
            curr = roman[a]
            result += curr if prev <= curr else -curr
            prev = roman[a]
        return result
