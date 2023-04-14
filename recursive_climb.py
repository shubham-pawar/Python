# Recursive climbing stairs

class Solution:
    def climbStairs_helper(self, current_step, n):
        if (current_step > n):
            return 0
        
        if (current_step == n):
            return 1
        
        return (self.climbStairs_helper(current_step + 1, n) +
                self.climbStairs_helper(current_step + 2, n))

    def climbStairs(self, n: int) -> int:
        return self.climbStairs_helper(0, n)
    
if __name__ == "__main__":
    print(Solution().climbStairs(5))