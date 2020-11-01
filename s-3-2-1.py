# 挿入ソート

data = [5,2,4,6,1,3]
new_data = [data[0]]

def print_result(x, y):
  for n in x:
    print(n, end=' ')
  for n in y:
    print(n, end=' ')
  print('\n')

for idx, n in enumerate(data[1:]):
  new_idx = idx + 1
  print_result(new_data, data[new_idx:])
  change_flag = False
  for nidx, v in enumerate(new_data):
    if n < v:
      source_data = n
      for i in range(nidx, len(new_data)):
        tmp = new_data[i]
        new_data[i] = source_data
        source_data = tmp
      new_data.append(source_data)
      change_flag = True
      break
  if not change_flag:
    new_data.append(n)
print_result(new_data, [])
    
        
    
    
       
    