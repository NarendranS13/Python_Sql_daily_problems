class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ## Normal loops method

        # n = len(nums)
        # missing = 0
        # for i in range(0,n+1):
        #     if i in nums:
        #         continue
        #     else:
        #         missing += i
    
        # return missing

        ### Using Set method
        n = len(nums)
        num_set = set(nums)
        
        for i in range(n+1):
            if i not in num_set:
                return i 
            
### Testing the code
sol = Solution()
print(sol.missingNumber([3,0,1]))