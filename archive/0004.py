# January 2, 2024

# getting input
n = int(input())
b_length = list(map(int, input().split()))
workers = list(map(int, input().split()))

# office efficiency
efficiency = [length / worker for length, worker in zip(b_length, workers)]
office_order = [
    i[0] + 1 for i in sorted(enumerate(efficiency), key=lambda x:x[1])
    ]

print(*office_order)
