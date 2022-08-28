def eat(a, b, c):
    nums = [0] * 3
    nums[0] = a
    nums[1] = b
    nums[2] = c

    nums.sort()
    total = sum(nums)

    if nums[0] + nums[1] > nums[2]:
        return ceil((num[0] + nums[1] + nums[2]) / 3)
    if 2 * (nums[0] + nums[1]) < nums[2]:
        return ceil(nums[2] / 2)
    
    return ceil((num[0] + nums[1] + nums[2]) / 3)
