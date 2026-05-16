class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length 
        
        # Pass 1: Calculate Left Products (Prefix)
        left_product = 1
        i = 0
        while i < length:
            answer[i] = left_product
            left_product *= nums[i] 
            i += 1 
            
        
        right_product = 1
        i = length - 1  
        while i >= 0:
            answer[i] *= right_product  
            right_product *= nums[i]   
            i -= 1                
            
        return answer