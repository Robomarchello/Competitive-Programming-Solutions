# getting input
n = int(input())
a = list(map(int, input().split()))

best = -1 * 10 ** 12
s1 = 0
s2 = sum(a)
for i in range(n - 1):
    s1 += a[i]
    s2 -= a[i]
    
    diff = s1 - s2
    best = max(best, diff)

print(best)

