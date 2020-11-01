# stableなソート
# stableなバブルソートと選択ソートを行い比較する
data = ['H4', 'C9', 'S4', 'D2', 'C3']

# バブルソート

flag = True
loop_count = 0

while flag:
  flag = False
  for i in reversed(range(1 + loop_count, len(data))):
    if int(data[i - 1][1]) > int(data[i][1]):
      tmp = data[i]
      data[i] = data[i - 1]
      data[i - 1] = tmp
      flag = True
  loop_count = loop_count + 1
print('stable')
print(data)

# 選択ソート
data = ['H4', 'C9', 'S4', 'D2', 'C3']

for i in range(len(data)):
  minj = -1
  for j in range(i, len(data)):
    if int(data[minj][1]) > int(data[j][1]):
      minj = j
  tmp = data[minj]
  data[minj] = data[i]
  data[i] = tmp
print('not stable')
print(data)
    