def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1

    return nums


def main():
    nums = [4, 3, 1, 5, 61, 3, 17]
    print('nums', nums)
    sorted_nums = insertion_sort(nums)
    print('sorted_nums', sorted_nums)


if __name__ == '__main__':
    main()
