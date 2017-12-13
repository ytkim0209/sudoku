'''
This is python sudoku solving example.
:parameter {type} : problem.txt
:return {type} : Solution of problem.
'''
import time
start_time = time.time()

def checkValidity(index):
    raw = index//9
    col = index%9
    #raw
    for i in range(0, 9):
        if raw*9 + i == index:
            continue
        if chars[index] == chars[raw*9 + i]:
            return False
    #column
    for j in range(0, 9):
        if j*9 + col == index:
            continue
        if chars[index] == chars[j*9 + col]:
            return False
    #subSquare
    for i in range(0, 3):
        for j in range(0, 3):
            ind = (raw//3 * 3 + i) * 9 + col//3 * 3 + j
            if ind == index:
                continue
            if chars[index] == chars[ind]:
                return False
    return True

def solve():
    for i in range(0, 81):
        if chars[i] == 0:
            for j in range(1, 10):
                chars[i] = j
                if checkValidity(i):
                    if solve():
                        return True
            chars[i] = 0
            return False
    return True

def printSolution():
    for t in range(0, 81):
        if t % 9 == 8:
            print(chars[t], end='\n')
        else:
            print(chars[t], end='')
################################################
## Main activity from here
################################################
chars = []
f = open('d:/temp/python_example/sudoku/problem.txt', 'r')
line = f.read().strip().replace('\n', '').replace(' ', '')
for c in line:
    chars.append(c)
chars = list(map(int, chars))
f.close()
if solve():
    printSolution()
else:
    print('There is not solution.')
print('time : ' + str(time.time() - start_time) + ' s')
