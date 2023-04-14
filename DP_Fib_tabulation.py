# Dynamic Programming: Fibonacci sequence with tabulation

def fib_tabulation(n, table):
    
    # We start with the smallest subproblem.
    # We start with because we already have the base case
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    
    print(table)
    return table[i]

print(fib_tabulation(5,{0:1, 1:1}))