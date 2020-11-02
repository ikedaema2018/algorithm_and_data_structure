# スタック
# 逆ポーランド記法で入力された数式の計算結果を算出
data = '12+34-*'

stack = []

def is_operator(s):
  if s == '+' or s == '-' or s == '*':
    return True
  else:
    return False

def culc(operator, operand1, operand2):
  if operator == '+':
    return operand2 + operand1
  elif operator == '-':
    return operand2 - operand1
  elif operator == '*':
    return operand2 * operand1

for s in data:
  if is_operator(s):
    result = culc(s, stack.pop(), stack.pop())
    stack.append(result)
  else:
    stack.append(int(s))

print(stack[0])
  
  