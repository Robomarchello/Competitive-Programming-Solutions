# January 4, 2024

l = 0
r = 10 ** 9

print(r)
m = r
for _ in range(47):
    guess = input()

    if guess == '<':
        l = m
        
    if guess == '>': 
        r = m

    if guess == '=':
        exit()
    
    m = l + (r - l) // 2

    print(m)
