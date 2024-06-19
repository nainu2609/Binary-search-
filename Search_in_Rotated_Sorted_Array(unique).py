class Solution:
    def search(self, arr: List[int], target: int) -> int:
        low = 0 
        high = len(arr)-1 
        while low <= high:
            mid = (low +high )//2 
            if arr[mid]== target :
                return mid 
            elif arr[low]<= arr[mid]:# checking left half is sorted or not 
                if arr[low]<= target and target<=arr[mid] :
                    high = mid -1 
                else:
                    low = mid +1 
            else: # checking right half is sorted or not 
                if arr[mid]<= target and arr[high]>= target:
                    low = mid +1 
                else:
                    high=mid -1 
        return -1 