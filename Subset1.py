class Solution:
	def subsetSums(self, arr, n):
		# code here
		ans = helper(0,0,arr,n,[])
		return ans


def helper(ind,s,arr,n,result):
    if ind==n:
        result.append(s)
        return 
    helper(ind+1,s+arr[ind],arr,n,result)
    helper(ind+1,s,arr,n,result)
    return result 
    