class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x<0):
        #If a number is negative, get rid off the minus sign, reverse it and add the minus sign
            x *= -1
            x = str(x)
            x = x[::-1]
            x = int(x)
            return x*-1
        else:
            #Conver the integer to string and then re convert string to integer after reversing it.
            x = str(x)
            x = x[::-1]
            x = long(x)
            return x
