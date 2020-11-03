# キュー n個のプロセスをqミリ秒のタイムクオンタムごとに処理
data = [
  [5, 100],
  ['p1', 150],
  ['p2', 80],
  ['p3', 200],
  ['p4', 350],
  ['p5', 20]
]

class Queue:
  MAX = 100000
  def __init__(self, data):
    self.data = data
    self.head = 0
    self.tail = len(data)
    
  def is_empty(self):
      return self.tail <= self.head

  def is_full(self):
    return self.tail >= self.MAX - 1
    
  def dequeue(self):
    if self.is_empty():
      raise Exception('underflow')

    self.head += 1
    return self.data[self.head - 1]

  def enqueue(self, x):
    if self.is_full():
      raise Exception('overflow')
    self.tail += 1
    self.data.insert(self.tail - 1, x)
    
quantum = data[0][1]
queue = Queue(data[1:])
time = 0

while not queue.is_empty():
  process = queue.dequeue()
  process[1] -= quantum
  if process[1] > 0:
    queue.enqueue(process)
    time += 100
  else:
    time += 100 - abs(process[1])
  
    print(f'{process[0]} {time}')
    
    
    