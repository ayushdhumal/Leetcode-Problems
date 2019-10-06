class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Converting array to string
        number = ''.join(str(digit) for digit in digits)
        number = int(number)
        #Adding one to the number
        number += 1
        #Emptying up digits array
        digits = []
        #Storing the summed up number back in the array
        for x in (str(number)):
            digits.append(int(x))
        return digits
