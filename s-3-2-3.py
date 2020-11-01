# バブルソートその2 改良版
data = [5,3,2,4,1]
flag = True
change_count = 0
loop_count = 0
while flag:
  flag = False
  for i in reversed(range(1 + loop_count, len(data))):
    if data[i] < data[i - 1]:
      tmp = data[i]
      data[i] = data[i - 1]
      data[i - 1] = tmp
      change_count = change_count + 1
      flag = True
  loop_count = loop_count + 1
print(data)
print(change_count)
    
    