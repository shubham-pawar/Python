# Dynamic Programming: Fibonacci sequence with memoization

def fib_memoization(n, table):
    if n not in table:
        table[n] = fib_memoization(n-1, table) + fib_memoization(n-2, table)
    else:
        # we do nothing
        pass
    
    print(table)
    return table[n] # O(1) running time

print(fib_memoization(5,{0:1, 1:1}))