# It's picture day at the local school and you are the photographer assigned to take class photos. 
# The described class has an even number of students, and each of those students wears a red or blue shirt. 
# In fact, exactly half of the class has red shirts and the other half has blue shirts. 
# You are responsible for lining up students in two rows before taking pictures. Each row must have the same number of students 
# and follow these guidelines: All students wearing a red shirt must be in the same row. All students in blue shirts must be in the same row. 
# Every student in the back row must be strictly taller than the student immediately in front of him in the front row. 
# You are given two input tables, one containing the heights of all red-shirted students and the other of all blue-shirted students. 
# These arrays are always the same length, and each height is a positive integer.

# Write a function that returns whether a class image following the given instructions can be drawn or not.

# Note: You can expect at least 2 students in each class.
# Sample Input

# redShirtHeights = [5, 8, 1, 3, 4]
#     blueShirtHeights = [6, 9, 2, 4, 5]
    

# Sample Output

# true // Place all students with blue shirts in the back row.
    
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    
    if redShirtHeights[0] > blueShirtHeights[0]:
        back_row = redShirtHeights
        front_row = blueShirtHeights
    else:
        back_row = blueShirtHeights
        front_row = redShirtHeights
    
    for i in range(len(back_row)):
        if back_row[i] <= front_row[i]:
            return False
    
    return True

print(classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))
