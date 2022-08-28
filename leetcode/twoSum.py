def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))