class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        helper(0, [],ans,nums)
        return ans
def helper(s, path,ans,nums):
    ans.append(path)
    if s == len(nums):
        return
    for i in range(s, len(nums)):
        if i > s and nums[i] == nums[i - 1]:
          continue
        helper(i + 1, path+[nums[i]],ans,nums)