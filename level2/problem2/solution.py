def solution(x, y):
    # Your code here
    level = x + y - 1
    value = 0
    for i in range(0, level):
        value = value + i
    value = value + x
    return str(value)

print(solution(5, 2))