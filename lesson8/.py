import random
arr = random.sample(range(1,30),11)
sum  = 0

for i in range (len(arr)):
    if arr[i] % 2 == 0:
        sum += arr[i]
        print(arr)
        print(sum)