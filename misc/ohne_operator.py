def solution(input_str):
    a, b, c = map(int, input_str.split('?'))

    result = max(
        a + b + c,
        a * b * c,
        (a + b) * c,
        a * (b + c),
        a + (b * c),
        (a * b) + c
    )

    return result


expression = input()

print(solution(expression))
