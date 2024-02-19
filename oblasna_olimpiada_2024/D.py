'''
A simple solution for the problem, not really fast.
Had an idea to divide the array into blocks, but didn't have enough time
to finish it, but it wasnt good idea anyways
'''


n, q = list(map(int, input().split()))
s = [int(character) for character in input()]

ts = []
for t in range(q):
    ts.append(
        list(map(int, input().split()))
    )

def req_1(i):
    global s
    # 1 ... i = 0, k - кінь
    for k in range(i):
        s[k] = 0

def req_2(i):
    global s
    # 1 ... i = 0, k - кінь
    for k in range(i):
        s[k] = 1

for req in ts:
    index = req[1]
    if req[0] == 1 and req[2] == 0:
        req_1(index)

    if req[0] == 1 and req[2] == 1:
        req_2(index)
    
    if req[0] == 2:
        print(s[index - 1])
