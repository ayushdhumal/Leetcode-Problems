class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #If a number is power of three, its mod of 3**(something) will be 0
        return n>0 and 3**20%n == 0
