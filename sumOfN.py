# Description: sum of n numbers

n = 5
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# Time complexity: O(n)
# Space complexity: O(1)


# recurvise function
def sumOfN(n):
    if n == 1:
        return 1
    else:
        return n + sumOfN(n-1)
print(sumOfN(5))

# Time complexity: O(n)
# Space complexity: O(n)

import time

def sum_all_recursion(n):
    # base case?
    # When should we end this recursion?
    if n == 0:
        return 0
    
    # recursive step?
    return n + sum_all_recursion(n - 1)














# Non -recursive
def sum_all_iter(n):
    summ = 0
    for num in range(1, n+1):
        summ += num
        
    return summ

# constant time
def constant_time(n):
    return n * (n + 1) // 2# Gauss summation




start = time.time()
print(sum_all_recursion(900))
end = time.time()
elapsed = end - start
print("recursion time", elapsed)


start = time.time()
print(sum_all_iter(900))
end = time.time()
elapsed = end - start
print("iteration time", elapsed)