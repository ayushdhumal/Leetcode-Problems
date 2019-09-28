class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #If the count increases more than 1, return False
        count = 0
        
        for x in range(len(nums)-1):
        #Comparing two elements
            if(nums[x]>nums[x+1]):
                count+= 1
        #If the first element is greater than the second change it to the second
                if(x == 0):
                    nums[x] = nums[x+1]
                elif(nums[x-1]<=nums[x+1]):
                    nums[x] = nums[x-1]
                else:
                    nums[x+1] = nums[x]
            if(count>1):
                return False
        return True
