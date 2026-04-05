class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix={}
        suffix={}
        result=[]
        running = 1
        for i,item in enumerate(nums):
            running *=item
            prefix[i]= running
        
        running =1 
        last_index =len(nums)-1
        for i in range(last_index, -1, -1):
            running *=nums[i]
            suffix[i]= running


        for i in range(0,len(nums),1):
            if i == 0:
                result.append(suffix[1])
            elif i == len(nums)-1:
                result.append(prefix[len(nums)-2])
            else:
                result.append(suffix[i+1]*prefix[i-1])
        return result


        