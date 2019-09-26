class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        #Creating a dictionary to store the record of the jewels
        record = {}
        #Count to keep a count of jewels
        count = 0
        #Iterating through jewel and storing the record in the dictionary  
        for gems in J:
            if( gems in record):
                record[gems] += 1
            else: 
                record[gems] = 1
                
        #Calculating the count if stones exist in record
        for stones in S:
            if(stones in record):
                count += record[stones]
                
        return count
