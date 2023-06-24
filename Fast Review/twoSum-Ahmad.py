def twoSum(self, nums: list[int], target: int) -> list[int]:
    """
    Optimal Time complexity: O(n)
    Corresponding Space complexity: O(n)
    - Algorithm: enumerate through list and calculate remaining, check for remaining in dictionary if not there
     add to dictionary
    :param self:
    :param nums:
    :param target:
    :return:
    """
    seen = dict()
    for index, value in enumerate(nums):
        remaining = target - value
        if remaining in seen:
            return [index, seen[remaining]]
        else:
            seen[value] = index

