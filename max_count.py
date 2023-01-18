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
		
