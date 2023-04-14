# Dynamic Programming: Climbing stairs with memoization

def climb_stairs(n):
    if (n == 1):
        return 1
    
    if n == 2:
        return 2
  
    table = {}
    table[1] = 1
    table[2] = 2

    for i in range(3, n+1):
        table[i] = table[i-1] + table[i-2]
    
    return table[i]

print(climb_stairs(5))

# Time complexity: O(n)
# Space complexity: O(n)

# Dynamic Programming: Climbing stairs with tabulation