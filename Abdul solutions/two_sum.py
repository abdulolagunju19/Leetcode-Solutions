def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    integer_array = nums
    indices = []
    leftovers = dict()

    for index, value in enumerate(integer_array):
        leftovers[value] = index

    for index, value in enumerate(integer_array):
        remaining = target - value

        if remaining in leftovers and index != leftovers[remaining]: 
            return [index, leftovers[remaining]]