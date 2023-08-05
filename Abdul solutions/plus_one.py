class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Runtime Complexity: O(n)
        Space Complexity: O(n)
        Algorithm: Turn digits into number, add it by 1, convert number to string, pass in each digit to new array
        """
        number = 0

        for i in range(len(digits)):
            number += digits[i] * 10**(len(digits)-(i+1))
        
        number += 1

        number = str(number)

        new_digits = []

        for i in range(len(number)):
            new_digits.append(int(number[i]))

        return new_digits