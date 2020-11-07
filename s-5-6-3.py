# 全探索

A = [1,5,7,10,21]
m = [2,4,17,8]

def solve(i, m):
  if m == 0:
    return True
  if m < 0 or i == len(A):
    return False;
  
  u = solve(i + 1, m)
  v = solve(i + 1, m - A[i])
  
  return u or v

for x in m:
  if solve(0, x):
    print('yes')
  else:
    print('no')

  
  