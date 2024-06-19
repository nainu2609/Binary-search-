class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        low = 0 
        high = len(arr)-1 
        while low <= high:
            mid = (low + high )//2 
            if arr[mid]== target :
                return True 
            if (arr[low]== arr[mid] and  arr[mid]==arr[high]):
                low+=1 
                high-=1
                continue
            elif arr[low]<= arr[mid]:#  we are checking that the lower half is sorted or not .
                if arr[low]<= target and arr[mid] >= target :
                    high = mid -1 
                else:
                    low = mid +1 
            else:
                if arr[mid]<= target and arr[high]>= target:
                    low = mid +1 
                else:
                    high=mid -1 
        return False 