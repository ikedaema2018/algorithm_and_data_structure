# ハッシュ法

hash_memory = [None] * 1046527

def get_char(ch):
  if ch == 'A':
    return 1
  elif ch == 'C':
    return 2
  elif ch == 'G':
    return 3
  elif ch == 'T':
    return 4
  
def get_key(str):
  sum = 0
  p = 1
  for s in str:
    sum += p * get_char(s)
    p *= 5
  return sum

def h1(key):
  return key % len(hash_memory)

def h2(key):
  return 1 + key % (len(hash_memory) -1)

def to_hash(key, i):
  return (h1(key) + i * h2(key)) % len(hash_memory)

def find(str):
  key = get_key(str)
  i = 0
  while True:
    h = to_hash(key, i)
    if hash_memory[h] == str:
      return True
    if not hash_memory[h]:
      return False
    i += 1
    
def insert(str):
  key = get_key(str)
  i = 0
  while True:
    h = to_hash(key, i)
    if hash_memory[h] == str:
      return False
    if not hash_memory[h]:
      hash_memory.insert(h , str)
      return False
    i += 1

# ハッシュ探索にする前
data = [
  'insert AAA',
  'insert AAC',
  'find AAA',
  'find CCC',
  'insert CCC',
  'find CCC'
  ]

for d in data:
  str = d.split(' ')[1]
  if d.split(' ')[0] == 'insert':
    insert(str)
  elif d.split(' ')[0] == 'find':
    if find(str):
      print('yes')
    else:
      print('no')
