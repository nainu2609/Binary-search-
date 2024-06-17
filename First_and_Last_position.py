class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f= first_occ (nums,target)
        if f == -1 :
            return
        s= second_occ(nums,target)
        return f,s

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