def binarySearch(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l

"""
- Using this template if the target exists, than we would be returning the leftmost index
- If it does not exist then we would be returning the index of the position it would be located if it did exist
"""