class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """        

        if n == 1:
            return 1
    
        elif n == 2:
            return 2

        else:
            ways = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return ways
