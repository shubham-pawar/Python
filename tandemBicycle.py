# Write a function that, given an input parameter, returns the highest possible total speed or the lowest possible total speed of all ridden tandem bicycles in the fastest way. If fastest = true, the function should return the maximum possible total speed; otherwise, it should return the minimum total speed. "Total speed" is defined as the sum of the speeds of all tandem wheels being towed. For example, if there are riders (2 red shirts and 2 blue shirts) with speeds 1, 3, , 5 and if they are paired on tandem bikes as follows: [1, ] , [5, 3] , then the total speed of their tandem bicycles are 5 = 9.

# A tandem bicycle is a bicycle that is ridden by two people: person A and person B. Both pedal the bicycle, but the faster person dictates the speed of the bicycle. So, if person A pedals at speed 5 and person B pedals at speed , the tandem bike moves at speed 5 (ie tandemSpeed = max(speedA, speedB)).
# Sample Input

# redShirtSpeeds = [5, 5, 3, 9, 2]
#     blueShirtSpeeds = [3, 6, 7, 2, 1] 
#     fastest = true
    

# Sample Output

# 32

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()  

    if fastest:
        blueShirtSpeeds.reverse()

    total_speed = 0

    for i in range(len(redShirtSpeeds)):
        total_speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    return total_speed

print(tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True))