data = [5,2,4,6,1,3]

def trace(new_data):
  for v in new_data:
    print(v, end=' ')
  print('\n')
  
trace(data)
for i in range(1, len(data)):
  v = data[i]
  change_flag = False
  for j in reversed(range(i)):
    if data[j] < v:
      data[j + 1] = v
      change_flag = True
      break
    data[j + 1] = data[j]
  if not change_flag:
    data[0] = v
  trace(data)
  