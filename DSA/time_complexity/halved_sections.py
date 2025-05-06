def halved_sections(n):
    rows = []
    i = n
    while i > 0:
        row = []
        for j in range(i + 1):
            row.append(j)

        rows.append(row)
        i //= 2

    return rows


def main():
    # time complexity is calculated for this one as follows:
    # O(n + 1/2n + 1/4n + ...) = O(n(1 + 1/2 + 1/4+ ...) = O(2n)
    # TIME COMPLEXITY: O(n)

    rows = halved_sections(12)
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
