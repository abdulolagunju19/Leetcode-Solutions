def containsDuplicate( nums: list[int]) -> bool:
    """
    Optimal time complexity: O(n)
    """
    # use hashset
    hashset = set()
    for x in nums:
        if x in hashset:
            return True
        else:
            hashset.add(x)
    return False


def main():
    nums = [1,2,3,4,1]
    result = containsDuplicate(nums)
    print(result)


main()


