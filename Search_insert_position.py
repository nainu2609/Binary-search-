#using lower bound to solve this question.
def lower_bound(arr, x):
    left, right = 0, len(arr) - 1
    ans = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >=x: 
            ans= mid 
            right = mid - 1
        else:                     
            left=mid+1 
    return ans 
arr = [1,2,4,5]
x= 0
print(lower_bound(arr, x))