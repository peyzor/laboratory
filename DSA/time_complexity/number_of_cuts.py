def count_number_of_cuts(x):
    count = 0
    while x > 1:
        x //= 2
        count += 1

    return count


def main():
    # by doubling the input size, the number of steps increases only by 1
    # this is the definition of a logarithmic solution
    # TIME COMPLEXITY: O(log(n))
    result1 = count_number_of_cuts(100)
    result2 = count_number_of_cuts(200)
    result3 = count_number_of_cuts(400)
    print(result1, result2, result3)


if __name__ == '__main__':
    main()
