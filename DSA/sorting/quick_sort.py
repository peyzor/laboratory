def quick_sort(nums, low, high):
    if low >= high:
        return None

    p = partition(nums, low, high)
    quick_sort(nums, low, p - 1)
    quick_sort(nums, p + 1, high)
    return nums


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = nums[high], nums[i]
    return i


def main():
    nums = [4, 3, 1, 5, 61, 3, 17]
    print('nums', nums)
    sorted_nums = quick_sort(nums, 0, len(nums) - 1)
    print('sorted_nums', sorted_nums)


if __name__ == '__main__':
    main()
