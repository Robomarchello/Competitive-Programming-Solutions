#not sure what comments to write here, when problem link will be available, will write it here

n, k = list(map(int, input().split()))
ps = list(map(int, input().split()))

count = 1
for i in range(n - 1):
    if ps[i] + 1 != ps[i + 1]:
        count += 1

if count <= k:
    print('Yes')
else:
    print('No')
