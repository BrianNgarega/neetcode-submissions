class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.solve(nums[1:]), self.solve(nums[:-1]))
        


    def solve(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
    
    
        first = nums[0] 
        second = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            current = max(first + nums[i], second)
            first = second
            second = current
            
        return second

     