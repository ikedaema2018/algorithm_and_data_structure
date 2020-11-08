# クイックソート
# パーティションを再帰的に呼び出す

def partition(list, first, last):
  x = list[last]
  i = first - 1
  for j in range(first, last):
    if list[j].split(' ')[1] <= x.split(' ')[1]:
      i += 1
      tmp = list[i]
      list[i] = list[j]
      list[j] = tmp
  list[last] = list[i + 1]
  list[i + 1] = x
  return i + 1

def quick_sort(list, first, last):
  if first < last:
    divide_point = partition(list, first, last)
    quick_sort(list, first, divide_point - 1)
    quick_sort(list, divide_point + 1, last)

data = [
  'D 3',
  'H 2',
  'D 1',
  'S 3',
  'D 2',
  'C 1'
]

quick_sort(data, 0, len(data) - 1)
print(data)
