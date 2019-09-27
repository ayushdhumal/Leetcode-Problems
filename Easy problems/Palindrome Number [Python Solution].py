class Solution:    
    def isPalindrome(self, x: int) -> bool:
        #Declaring an extra number for storing our original number
        num =x
        reverse =0
        #Getting the reverse of the input int
        while(x>0):
            temp =x%10
            reverse=reverse*10+temp
            x=x//10
        #Checking if it is a palindrome
        if(num==reverse):
            return True
        else:
            return False
            
