"""
    Maximum Count of Positive Integer and Negative Integer

    User Accepted: 11422
    User Tried: 11755
    Total Accepted: 11782
    Total Submissions: 14750
    Difficulty: Easy

Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

    In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.

Note that 0 is neither positive nor negative.
"""

pos = 0
neg = 0
class Solution:
    def maximumCount(nums):
        for i in range(len(nums)):
            if nums[i] < 0:
                globals()['neg'] = globals()['neg'] + 1
            if nums[i] > 0:
                globals()['pos'] = globals()['pos'] + 1
            else:
                continue
        return max(pos, neg)


nums = [0,0,-1,1,-2,-12]

print(Solution.maximumCount(nums))

print(nums)
		
