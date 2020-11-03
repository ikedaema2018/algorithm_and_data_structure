# スタック
# 逆ポーランド記法で入力されたデータを計算する
# pythonのarrayでスタックを表現するのではなく、スタックclassを実装
class Stack:
  MAX = 100
  def __init__(self):
    self.top = -1
    self.data = []
    
  def is_empty(self):
    return self.top == -1

  def is_full(self):
    return self.top >= self.MAX - 1
  
  def push(self, x):
    if self.is_full():
      raise Exception('overflow')
    self.top+=1
    self.data.insert(self.top, x)
  
  def pop(self):
    if self.is_empty():
      raise Exception('underflow')
    self.top-=1
    return self.data[self.top + 1]
  
def is_operator(s):
  if s == '+' or s == '-' or s == '*':
    return True
  else:
    return False
  
data = '12+34-*'

def culc(operator, operand1, operand2):
  if operator == '+':
    return operand2 + operand1
  elif operator == '-':
    return operand2 - operand1
  elif operator == '*':
    return operand2 * operand1

stack = Stack()
for s in data:
  if is_operator(s):
    result = culc(s, stack.pop(), stack.pop())
    stack.push(result)
  else:
    stack.push(int(s))

print(stack.pop())
  




    
  
  