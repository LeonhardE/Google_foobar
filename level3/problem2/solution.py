from fractions import Fraction

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(x, y):
    return x * y // gcd(x, y)

def count_terminal(m):
    count = 0
    for row in m:
        rowsum = 0
        for i in range(len(row)):
            rowsum += row[i]
        if rowsum == 0:
            count += 1
    return count

def extract(m, n):
    Q = []
    R = []
    for i in range(len(m) - n):
        line1 = []
        line2 = []
        for j in range(len(m[i])):
            rowsum = 0
            for k in range(len(m[i])):
                rowsum += m[i][k]
            if j < len(m) - n:
                line1.append(m[i][j] / rowsum)
            else:
                line2.append(m[i][j] / rowsum)
        Q.append(line1)
        R.append(line2)
    return Q, R

def multiple(A, B):
    AB = []
    for i in range(len(A)):
        newline = []
        for j in range(len(B[0])):
            value = 0
            for k in range(len(B)):
                value += A[i][k] * B[k][j]
            newline.append(value)
        AB.append(newline)
    return AB

def transposeMatrix(m):
    return list(map(list,zip(*m)))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def subtract_inverse(Q):
    newQ = []
    for i in range(len(Q)):
        line = []
        for j in range(len(Q[i])):
            if j == i:
                line.append(1 - Q[i][j])
            else:
                line.append(-Q[i][j])
        newQ.append(line)
    return getMatrixInverse(newQ)

def get_vector(FR):
    hit_vector = []
    denoms = []
    for number in FR[0]:
        frac = Fraction(number).limit_denominator()
        hit_vector.append(frac.numerator)
        denoms.append(frac.denominator)
    lcd = 1
    for denom in denoms:
        lcd = lcm(lcd, denom)
    for i in range(len(hit_vector)):
        hit_vector[i] *= int(lcd / denoms[i])
    hit_vector.append(lcd)
    return hit_vector

def solution(m):
    # Your code here
    n = count_terminal(m)
    Q, R = extract(m, n)
    F = subtract_inverse(Q)
    FR = multiple(F, R)
    return get_vector(FR)



print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 1, 0, 1, 0, 0], [3, 0, 2, 1, 0, 0], [0, 4, 0, 0, 3, 2], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))