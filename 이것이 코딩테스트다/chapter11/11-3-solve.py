data = list(map(int, input()))

# 전부 0으로 바꿀 때
one_to_zero = 0

data.append(0)
for i in range(1, len(data)):
    if data[i- 1] == 1 and data[i] == 0:
        one_to_zero += 1

# 전부 1로 바꿀때 
zero_to_one = 0
data.pop()
data.append(1)

for i in range(1, len(data)):
    if data[i-1] == 0 and data[i] == 1:
        zero_to_one += 1

# 둘중 가장 작은 수 찾기 
print(min(one_to_zero, zero_to_one))