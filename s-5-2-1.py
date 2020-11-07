# 線形探索

import time
start = time.time()
s = range(0, 1000)
t = range(500, 1500)

count = 0

for i in t:
  flag = False
  for j in s:
    if i == j:
      flag = True
  if flag:
    count += 1


print(count)
print(time.time() - start)

