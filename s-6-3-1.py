# コッホ曲線
# なんとなく写経
import math

class Point:
  def __init__(self):
    self.x = None
    self.y = None

def koch(n, a, b):
  if n == 0:
    return
  s, t, u = Point(), Point(), Point()
  th = math.pi * 60.0 / 180.0
  
  s.x = (2.0 * a.x + 1.0 * b.x) / 3.0
  s.y = (2.0 * a.y + 1.0 * b.y) / 3.0
  t.x = (1.0 * a.x + 2.0 * b.x) / 3.0
  t.y = (1.0 * a.y + 2.0 * b.y) / 3.0
  u.x = (t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x
  u.y = (t.x - s.x) * math.sin(th) - (t.y - s.y) * math.cos(th) + s.y
  
  koch(n - 1, a, s)
  print(f'{s.x} {s.y}')
  koch(n - 1, s, u)
  print(f'{u.x} {u.y}')
  koch(n -1, u, t)
  print(f'{t.x} {t.y}')
  koch(n -1, t, b)
  
a, b = Point(), Point()
n = 5

a.x = 0
a.y = 0
b.x = 100
b.y = 0

print(f'{a.x} {a.y}')
koch(n, a, b)
print(f'{b.x} {b.y}')
  
  
  
  