class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """        

        memory = [0, 1, 2]

        if n == 1:
            return memory[1]
    
        elif n == 2:
            return memory[2]

        else:
            if len(memory) >= (n + 1):
                return memory[n]
            else:
                steps = self.climbStairs(n - 1) + self.climbStairs(n - 2)
                memory.append(steps)
            return steps
