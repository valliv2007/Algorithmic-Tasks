nums = [int(i) for i in input()]
limit = len(nums) / 2
dict_nums = {}
for num in nums:
    try:
        dict_nums[num] += 1
    except KeyError:
        dict_nums[num] = 1
    if dict_nums[num] > limit:
        print(num)
        break