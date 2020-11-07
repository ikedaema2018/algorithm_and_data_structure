# 分割統治法
def find_maximum(data, more, less):
  mid = (more + less) // 2
  if more + 1 == less:
    return data[more]
  
  u = find_maximum(data, more, mid)
  v = find_maximum(data, mid, less)
  
  return max(u, v)

data = [1,2,3, 999,4,5,6]

print(find_maximum(data, 0, len(data)))

