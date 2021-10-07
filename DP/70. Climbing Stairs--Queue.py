class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """        
        stair_number = []
        stair_number.append(1)
        stair_number.append(2)

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(3, n + 1):
                stair_number.append(stair_number[-1] + stair_number[-2])
                stair_number.pop(0)
            return stair_number[-1]
