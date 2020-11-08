def partition(A, first, last):
  x = A[last]
  i = first - 1
  for j in range(first, last):
    if A[j] <= x:
      i += 1
      print(j)
      tmp = A[i]
      A[i] = A[j]
      A[j] = tmp
  A[last] = A[i + 1]
  A[i + 1] = x
  return A[i + 1]

data = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
print(partition(data, 0, len(data) - 1))
print(data)