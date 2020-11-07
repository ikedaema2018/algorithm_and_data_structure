# 二部探索

s = [1, 2, 3, 4, 5]
t = [3, 4, 1]

def binary_search(s, key):
  left = 0
  right = len(s)
  
  while left < right:
    mid = (left + right) // 2
    if s[mid] == key:
      return True
    elif s[mid] < key:
      left = mid + 1
    else:
      right = mid
  return False

count = 0
for i in t:
  if (binary_search(s, i)):
    count += 1

print(count)
    