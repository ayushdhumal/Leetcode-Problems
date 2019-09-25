class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Creating an array to store the numer of steps required to reach first 3 stairs
        arr = [1,2,3]
        if (n<=3 and n>=0):
            return n
        else:
        #Iterating through the loop and memoizing the sum of previous 2 elements in the array

            for x in range(3,n):
                temp = arr[x-1]+arr[x-2]
        #Appending the sum of elements to the array until the end of for loop
                arr.append(temp)
        #Returning the final element of the array(the number of steps required for climbing n stairs)
            return arr[n-1]
    
