# December 24, 2023

n = int(input())
buildings = list(map(int, input().split()))

sorted_ = sorted(list(range(n)), key=lambda x: buildings[x])
sorted_ = [x + 1 for x in sorted_]

print(*sorted_)