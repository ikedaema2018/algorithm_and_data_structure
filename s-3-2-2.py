# バブルソートその1
data = [5,3,2,4,1]
flag = True
count = 0
while flag:
  flag = False
  for i in reversed(range(1, len(data))):
    if data[i] < data[i - 1]:
      tmp = data[i]
      data[i] = data[i - 1]
      data[i - 1] = tmp
      count = count + 1
      flag = True
print(data)
print(count)
    
    