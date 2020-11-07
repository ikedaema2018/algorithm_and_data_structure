# whileをもちいて線形探索を高速化
import time
start = time.time()
s = range(0, 1000)
t = range(500, 1500)

def linerSearch(s, key):
  i = 0
  s.append(key)
  
  while s[i] != key:
    i +=  1
    
  return i != len(s) -1

count = 0
for i in t:
  if linerSearch(list(s), i):
    count += 1
print(count)
print(time.time() - start)

