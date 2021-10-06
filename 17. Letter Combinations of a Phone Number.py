class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitsdict = {
            2 = ['a', 'b', 'c'],
            3 = ['d', 'e', 'f'],
            4 = ['g', 'h', 'i'],
            5 = ['j', 'k', 'l'],
            6 = ['m', 'n', 'o'],
            7 = ['p', 'q', 'r', 's'],
            8 = ['t', 'u', 'v'],
            9 = ['w', 'x', 'y', 'z']
        }
        
        integer = []
        strings = []

        if len(digits) > 0:
            for i in len(digits):
                integer.append(digits[i])
                strings.append(digitsdict[digits[i]])

        else:
            return []
