nums = [2, 3, 6, 5, 1, 4, 8, 11, 0, 7]

# 模拟栈操作实现非递归的快速排序

def quick_sort(nums):
    if len(nums) < 2:
        return nums

    stack = []
    # 初始把待排序列表起始和结束位置放入栈
    stack.append(len(nums)-1)
    stack.append(0)

    # 当栈有元素就一直循环
    while stack:
        left = stack.pop()
        right = stack.pop()
        # 确定基准值
        index = partition(nums, left, right)
        if left < index - 1:
            stack.append(index - 1)
            stack.append(left)
        if right > index + 1:
            stack.append(right)
            stack.append(index + 1)
    return nums


def partition(nums, left, right):
    # 在当前列表，还是按照快排思想，左边小于基准值，右边大于等于基准值，左右下标向中间靠拢，返回左或右值
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]

    # 此时left == right
    nums[left] = pivot

    return left


print(quick_sort(nums))