def merge_sort(nums):
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    l = merge_sort(nums[:mid])
    r = merge_sort(nums[mid:])
    return merge(l, r)


def merge(first, second):
    result = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    while i < len(first):
        result.append(first[i])
        i += 1

    while j < len(second):
        result.append(second[j])
        j += 1

    return result


def main():
    nums = [4, 3, 1, 5, 61, 3, 17]
    print('nums', nums)
    sorted_nums = merge_sort(nums)
    print('sorted_nums', sorted_nums)


if __name__ == '__main__':
    main()
