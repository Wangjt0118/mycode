nums = [2, 3, 6, 5, 1, 4, 8, 11, 0, 7]


def quick_sort(nums):
    if not nums:
        return []
    else:
        pivot = nums[0]
        quick_left = [i for i in nums[1:] if i < pivot]
        quick_right = [i for i in nums[1:] if i >= pivot]

    return quick_sort(quick_left) + [pivot] + quick_sort(quick_right)


print(quick_sort(nums))

