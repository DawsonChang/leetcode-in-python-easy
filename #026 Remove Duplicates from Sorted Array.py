class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        swap_index = 0
        temp = nums[0]
        for current_index in range(len(nums)):
            if nums[current_index] != temp:
                temp = nums[current_index]
                swap_index +=1
                nums[swap_index] = nums[current_index]
        return swap_index+1
        
                    
                
            
            
        
