# Questions: https://quera.org/problemset/251441

def calculate_perimeter(n, intervals):
    wall = [[False] * 101 for _ in range(101)]
    for i, (l, r) in enumerate(intervals):
        for j in range(l, r):
            wall[i][j] = True

    perimeter = 0

    for i in range(n):
        for j in range(1, 101):
            if wall[i][j]:
                if not wall[i][j - 1]:
                    perimeter += 1
                if not wall[i][j + 1]:
                    perimeter += 1
                if i == 0 or not wall[i - 1][j]:
                    perimeter += 1
                if i == n - 1 or not wall[i + 1][j]:
                    perimeter += 1

    return perimeter


n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

print(calculate_perimeter(n, intervals))
