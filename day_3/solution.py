from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        ### Brute Force method Using Loops

        # if len(nums) < 2:
        #     print("Array required minimum two values")
        # else:
        #     results_list_of_tuples =  [(i,j) for i in range(0,len(nums)) for j in range(i+1, len(nums)) if target == nums[i] + nums [j]]
        #     # for i in range(0,len(nums)):
        #     #     for j in range(i+1,len(nums)):
        #     #         output = nums[i] + nums[j]
        #     #         if output == target:
        #     #             return list((i,j))
        #     if results_list_of_tuples:
        #     # The result is [(0, 1)]. We get the first element (0, 1)
        #         found_tuple = results_list_of_tuples[0]
        #     # Convert the tuple (0, 1) to a list [0, 1]
        #     return list(found_tuple)

        ### Using HashMap/Dictionary Faster and standard
        if len(nums) < 2:
            print("Array required minimum two values")
        seen = {}
        for i, current_num in enumerate(nums):
            needed = target - current_num
            if needed in seen:
                return [seen[needed], i]
            seen[current_num] = i
        return None
    
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))