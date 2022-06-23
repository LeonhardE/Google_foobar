def descending(n):
    return sorted(n, reverse=True)

def ascending(n):
    return sorted(n, reverse=False)

def subtract(x, y, k, b):
    z = [0] * k
    for i in range(0, k):
        z[k - 1 - i] = int(x[k - 1 - i]) - int(y[k - 1 - i])
        if z[k - 1 - i] < 0:
            z[k - 1 - i] = z[k - 1 - i] + b
            x[k - 2 - i] = int(x[k - 2 - i]) - 1
    return ''.join(str(x) for x in z)

def solution(n, b):
    #Your code here
    k = len(n)
    cycle = [n]
    length = 0
    
    while len(cycle) > 0:
        x = descending(n)
        y = ascending(n)
        z = subtract(x, y, k, b)
        if z in cycle:
            for i in range(0, len(cycle)):
                if z == cycle[i]:
                    length = len(cycle) - i
                    break
            # print(cycle)
            cycle = []
        else:
            cycle.append(z)
            n = z

    return length

print(solution("1000", 10))