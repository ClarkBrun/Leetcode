class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitsdict = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        
        # integer = []
        strings = []
        output = []

        if len(digits) > 0:
            for i in range(len(digits)):
                # integer.append(digits[i])
                strings.append(digitsdict[digits[i]])

            while(len(strings) > 1):
                for j in range(len(strings[0])):
                    for k in range(len(strings[1])):
                        output.append(strings[0][j] + strings[1][k])
                
                strings.pop(0)
                strings[0] = output
                output = []

            return strings[0]

        else:
            return []
