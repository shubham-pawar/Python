

# Implement a function in which the input is a non-empty array with sorted integers in ascending order and generates the output of array with the squares of original input integers

# NOTE : the output array should be of same length of input arrat
# Sample Input

# array = [1, 2, 3, 5, 6, 8, 9]
    

# Sample Output

# [1, 4, 9, 25, 36, 64, 81]
    
def sortedSquaredArray(array):
    n = len(array)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(array[left]) > abs(array[right]):
            result[i] = array[left] ** 2
            left += 1
        else:
            result[i] = array[right] ** 2
            right -= 1
    return result