d = [0] * 100

# 첫번째 피보나치 수, 두번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])