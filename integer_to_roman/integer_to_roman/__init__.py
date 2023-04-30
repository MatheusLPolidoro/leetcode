class Solution(object):
    """
    >>> Solution().intToRoman(3)
    'III'
    >>> Solution().intToRoman(58)
    'LVIII'
    >>> Solution().intToRoman(1994)
    'MCMXCIV'
    >>> Solution().intToRoman(61)
    'LXI'
    """

    def intToRoman(self, num):
        symbol = [
            'M',
            'CM',
            'D',
            'CD',
            'C',
            'XC',
            'L',
            'XL',
            'X',
            'IX',
            'V',
            'IV',
            'I',
        ]
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''
        index = 0
        while num > 0 and num < 4000:
            if num >= value[index]:
                result += symbol[index]
                num -= value[index]
            else:
                index += 1
        return result
