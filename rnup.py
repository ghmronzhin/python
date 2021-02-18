n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)
max = arr[-1]
i = len(arr) - 1
while i >= 0:
    if arr[i] != max:
        rnup = arr[i]
        break
    i-=1
print(rnup)
