import time

# I directly store the big number and use bitwise operation
# The same method as the old solution

def solution(n):
    n = int(n)
    operation = 0
    while n != 1:
        if n & 1 == 0:
            n = n // 2
        elif n & 3 == 1 or n == 3:
            n = n - 1
        else:
            n = n + 1
        operation += 1
    return operation
    
test = str(10 ** 309 + 2 ** 1000)
print(test)
start = time.time()
print(solution(test))
end = time.time()
print("Time: ", end - start)
