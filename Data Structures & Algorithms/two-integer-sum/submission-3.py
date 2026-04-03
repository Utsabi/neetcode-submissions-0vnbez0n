class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num1 in nums:
            num2 = target - num1
            if num2 in nums:
                if num1 == num2:
                    indices = [i for i, x in enumerate(nums) if x == num1]
                    if len(indices)!=2:
                        continue
                    return indices
                else:
                    num1_index = nums.index(num1)
                    num2_index = nums.index(num2)
                    result = [num1_index,num2_index]
                    return result
        