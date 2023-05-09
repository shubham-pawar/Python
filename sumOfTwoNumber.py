

# Implement a function that accepts an input of integer representing a target addition and an integer indicating a non-empty array of unique numbers. The function should return the numbers in an array, in whatever order, if any two values in the input array add up to the desired amount. The function should be returning an empty array if no two numbers add up to the intended total.

# The desired sum cannot be attained by adding a single integer to itself; rather, it can only be obtained by adding two separate integers in the array.

# Assumption : There will only be one set of numbers that adds up to the desired total.
# Sample Input

# array = [3, 5, -4, 8, 11, 1, -1, 6]
#     targetSum = 10
    

# Sample Output

# [-1, 11] // the numbers could be in reverse order
    



def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        nums[num] = True
        
    return []