def longestConsecutive( nums: list[int]) -> int:
    """
    Optimal Time complexity: O(n)
        -Algorithm: check if there is no left neighbour, search set for next one 
    :param nums:
    :return:
    """
    numSet = set(nums)
    longest = 0

    for n in numSet:
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest
def longestConsecutive_space( nums: list[int]) -> int:
    """
    Optimal space complexity
    :param self:
    :param nums:
    :return:
    """
    maximum = 0
    nums.sort()
    print(nums)
    i = 0
    while (i < len(nums)):
        j = i
        length = 1
        while j + 1 < len(nums) and (nums[j + 1] == nums[j] + 1 or nums[j + 1] == nums[j]):
            if (nums[j + 1] == nums[j] + 1):
                length += 1
            j += 1
        if maximum < length:
            maximum = length
        i = j + 1
    return maximum

