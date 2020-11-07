# whileをもちいて線形探索を高速化

s = [1, 2, 3, 4, 5]
t = [3, 4, 1]

def linerSearch(s, key):
  i = 0
  s.append(key)
  
  while s[i] != key:
    i +=  1
    
  return i != len(s) -1

count = 0
for i in t:
  if linerSearch(s, i):
    count += 1
print(count)
    