#defination of upper bound is that smallest index such that arr[ind]> x
def upper_bound(arr, x):
    left, right = 0, len(arr) - 1
    ans = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > x: 
            ans= mid 
            right = mid - 1
        else:                     
            left=mid+1 
    return ans 
arr = [1,2,3,4,5]
x= 2
print(upper_bound(arr, x))