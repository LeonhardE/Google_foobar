def valid(start, point):
    left1 = [-17, 15]
    left2 = [-10, 6]
    right1 = [-15, 17]
    right2 = [-6, 10]
    validator = True
    move = point - start
    if start % 8 < 2 and move in left2:
        validator = False
    if start % 8 < 1 and move in left1:
        validator = False 
    if start % 8 > 5 and move in right2:
        validator = False
    if start % 8 > 6 and move in right1:
        validator = False 
    if point < 0 or point > 63:
        validator = False
    return validator

def solution(start, dest):
    movement = [-17, -15, -10, -6, 6, 10, 15, 17]
    previous = [start]
    nexts = []
    steps = 0
    flag = True
    while flag:
        steps += 1
        for item in previous:
            for move in movement:
                next = item + move
                if valid(item, next):
                    if next not in nexts:
                        nexts.append(next)
                    if next == dest:
                        flag = False
        # print(nexts)
        previous = nexts
        nexts = []
    return str(steps)

print(solution(0, 1))
print(solution(19, 36))
print(solution(3, 45))