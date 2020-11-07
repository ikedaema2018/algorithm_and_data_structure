# e-7-1-1で本のとおりに実装したあとに自力で実装
# マージソート

A = [6,7,4,5,9,8,4,1,3,2]
count = 0
SENTINEL = 200000000

# A[left] ~ A[mid - 1] と A[mid] ~ A[right]は昇順にソートされている
def merge(A, left, right, mid):
  global count
  L = A[left: mid]
  R = A[mid: right]
  L.append(SENTINEL)
  R.append(SENTINEL)
  
  u = v = 0
  # ステーブルなソートにするために <= にする？
  for i in range(left, right):
    count += 1
    if (L[u] <= R[v]):
      A[i] = L[u]
      u += 1
    else:
      A[i] = R[v]
      v += 1
      
def merge_sort(A, left, right):
  if left + 1 >= right:
    return
  mid = (left + right) // 2
  
  merge_sort(A, left, mid)
  merge_sort(A, mid, right)
  merge(A, left, right, mid)
  
merge_sort(A, 0, len(A))

print(A)
print(count)
  