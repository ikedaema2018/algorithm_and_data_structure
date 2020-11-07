# 本のとおりに実装

MAX = 500000
A = [8, 5, 9, 2, 6, 3, 7, 1, 10, 4]
count = 0
SENTINEL = 200000000

def merge(A, left, mid, right):
  global count
  L = A[left:mid]
  R = A[mid:right]
  L.append(SENTINEL)
  R.append(SENTINEL)
  
  u = v = 0
  for i in range(left, right):
    count += 1
    if L[u] > R[v]:
      A[i] = R[v]
      v += 1
    else:
      A[i] = L[u]
      u += 1

def merge_sort(A, left, right):
  if (left + 1) >= right:
    return
  mid = (left + right) // 2
  merge_sort(A, left, mid)
  merge_sort(A, mid, right)
  merge(A, left, mid, right)
  
merge_sort(A, 0, len(A))

print(A)
print(count)
  
  