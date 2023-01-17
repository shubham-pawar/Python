# bubble sort

def bubbleSort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp


nums = [0,99, 4, 21, 8, 48, 1]

bubbleSort(nums)

print('Our sorted list is ',nums)