

# implement a program that returns the least amount of change (the least amount of money) that you are unable to produce, given an array of positive integers indicating the values of the coins you currently have. The provided coins not need to be unique and can have any positive integer value (i.e., you can have multiple coins of the same value).

# For instance, if you are given the quantity of coins [1, 2, 5], the least amount of change you can produce is 4. The smallest amount of change you can't make if you don't have any coins is 1.
# Sample Input

# coins = [5, 7, 1, 1, 2, 3, 22]
    

# Sample Output

# 20
    
def nonConstructibleChange(coins):
    coins.sort()
    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    return currentChangeCreated + 1

