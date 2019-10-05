class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openers = ['(','{','[']
        parantheses = { ")": "(", "}": "{", "]": "[" }
        #To store our string as a stack
        stack = []
        if(s == None):
            return True
        for x in s:
        #If the char is an opener append it
            if(x in openers):
                stack.append(x)
            else:
                #If the stack is empty, return false
                temp = stack.pop() if stack else False
                if(parantheses[x] != temp):
                    return False
        #If the stack has some element by the end, return false
        if stack:
            return False
        else:
            return True
                    
