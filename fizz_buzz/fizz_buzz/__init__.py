class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        """
        >>> Solution().fizzBuzz(3)
        ['1', '2', 'Fizz']

        >>> Solution().fizzBuzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']

        >>> Solution().fizzBuzz(15)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        """

        result = [
            'Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i)
            for i in range(1, n + 1)
        ]
        return result
