class Solution:

	def count(self,nums, n, target):
		if first_occ (nums,target)==-1:
		    return 0
        else:
		    return second_occ(nums,target) - first_occ (nums,target)+1
		   
def first_occ (nums,target):
        start = -1
        low =0 
        high = len(nums)-1 
        while low <= high :
            mid = (low+high)//2 
            if nums[mid]==target: 
                start = mid 
                high = mid -1 
            elif nums[mid]>target :
                high = mid -1 
            else:
                low = mid +1 
        return start 
def second_occ(nums,target):
        ending = -1 
        low =0 
        high = len(nums)-1 
        while low <= high :
            mid = (low+high)//2 
            if nums[mid]==target: 
                ending = mid 
                low = mid + 1 
            elif nums[mid]>target :
                high = mid -1 
            else:
                low = mid +1 
        return ending