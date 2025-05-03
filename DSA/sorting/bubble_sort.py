def bubble_sort(nums):
    swapping = True
    end = len(nums)

    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = True

        end -= 1

    return nums


def main():
    nums = [4, 3, 1, 5, 61, 3, 17]
    sorted_nums = bubble_sort(nums)
    print('nums', nums)
    print('sorted_nums', sorted_nums)


if __name__ == '__main__':
    main()
