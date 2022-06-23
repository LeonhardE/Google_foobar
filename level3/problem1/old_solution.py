import time

# I didn't recognize python can store big number at first
# so I use string to store the number and binary form

def toBinary(n):
    binary = ""
    next = ""
    while n != "":
        flag = 0
        for item in n:
            digit = int(item) + flag * 10
            flag = 0
            if digit % 2 == 1:
                digit = digit - 1
                flag = 1
            temp = str(digit // 2)
            if next == "" and temp == "0":
                continue
            else:
                next += temp
        n = next
        next = ""
        binary = str(flag) + binary
    return binary

def solution(n):
    # Your code here
    binary = toBinary(n)
    # binary = "1011011011011011011011011011"
    operation = 0
    while binary != "1":
        n = len(binary)
        # print(binary, operation)
        if binary[n - 1] == "0":
            binary = binary[0 : n - 1]
            operation += 1
        else:
            count = 0
            for i in range(n):
                if binary[n - 1 - i] == "0":
                    break
                count += 1
            if count == 1:
                binary = binary[0 : n - 1]
                operation += 2
            elif count < n:
                binary = binary[0: n - count - 1] + "1"
                operation += count + 1
            elif count == 2 and n == 2:
                binary = "1"
                operation += 2
            else:
                binary = "1"
                operation += count + 1
    return operation

test = str(10 ** 309 + 2 ** 1000)
print(test)
start = time.time()
print(solution(test))
end = time.time()
print("Time:", end - start)