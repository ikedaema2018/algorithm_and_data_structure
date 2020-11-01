# 選択ソート
data = [5,6,4,2,1,3]

for i in range(len(data) - 1):
  minj = -1
  min_value = 100
  for j in range(i, len(data)):
    if min_value > data[j]:
      min_value = data[j]
      minj = j
  tmp = data[i]
  data[i] = data[minj]
  data[minj] = tmp
print(data)
  
  
  