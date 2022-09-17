class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        
        for n in range(len(nums)):
            if i == 0:
                max_distinct = nums[i]
                i += 1
            elif nums[n] != max_distinct and i < 3:
                max_distinct = nums[n]
                i += 1
            
        print(max_distinct)
        if i == 3: 
            return max_distinct
        else:
            return nums[0]
                
            
            
        
        
        
       
            
                
        
        