"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if(nums[j] < nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]

 """
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_counter = 0
        one_counter = 0
        two_counter = 0

        for i in range(len(nums)):
            if(nums[i] == 0):
                zero_counter += 1
            elif(nums[i] == 1):
                one_counter += 1
            elif(nums[i] == 2):
                two_counter += 1
        print(f"0: {zero_counter}, 1: {one_counter}, 2: {two_counter}")
        for i in range(0, zero_counter):
            nums[i] = 0
        for i in range(zero_counter, zero_counter+one_counter):
            nums[i] = 1
        for i in range(zero_counter+one_counter, zero_counter+one_counter+two_counter):
            nums[i] = 2
        


                
       
        

            