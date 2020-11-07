# ハッシュ探索にする前
data = [
  'insert AAA',
  'insert AAC',
  'find AAA',
  'find CCC',
  'insert CCC',
  'find CCC'
  ]

box = []

for str in data:
  if str.split(' ')[0] == 'insert':
    box.append(str.split(' ')[1])
  elif str.split(' ')[0] == 'find':
    exist = False
    for b_str in box:
      if b_str == str.split(' ')[1]:
        exist = True
    if exist:
      print('yes')
    else:
      print('no')
      