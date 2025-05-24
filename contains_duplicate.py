def contains_duplicate_sort(nums):
    nums.sort    
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    
    return False


print(contains_duplicate_sort([1, 2, 3, 1]))