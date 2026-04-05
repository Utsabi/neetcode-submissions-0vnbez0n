class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        n =len(nums)
        count=nums.count(0)

        if count>1:
            product =0

        for item in nums:
            if item != 0:
                product *= item
        
        result=[]
        for item in nums:
            if item == 0:
                result.append(product)
            elif count >= 1:
                result.append(0)
            else:
                val = int(product/ item)
                result.append(val)
        
        return result


        