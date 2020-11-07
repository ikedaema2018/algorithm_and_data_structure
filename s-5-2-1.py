# 線形探索

s = [1, 2, 3, 4, 5]
t = [3, 4, 1]

count = 0

for i in t:
  flag = False
  for j in s:
    if i == j:
      flag = True
  if flag:
    count += 1


print(count)