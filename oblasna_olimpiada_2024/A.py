import math

n, k, c = list(map(int, input().split()))

needed = n * 4
boxes = needed / k

print(math.ceil(boxes) * c)
