# 連結リスト
class Node:
  def __init__(self, key):
    self.key = key
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):
    self.nil = Node(None)
    self.nil.next = self.nil
    self.nil.prev = self.nil
    
  def insert(self, key):
    node = Node(key)
    node.next = self.nil.next
    self.nil.next = node
    node.next.prev = node
    node.prev = self.nil
  
  def list_search(self, key):
    cur = self.nil.next
    while cur != self.nil and cur.key != key:
      cur = cur.next
    return cur
  
  def delete_node(self, node):
    if node == self.nil:
      return
    node.next.prev = node.prev
    node.prev.next = node.next
    
  def delete_first(self):
    self.delete_node(self.nil.next)
    
  def delete_last(self):
    self.delete_node(self.nil.prev)
  
  def delete_key(self, key):
    self.delete_node(self.list_search(key))
    
  def print_list(self):
    cur = self.nil.next
    while cur != self.nil:
      print(cur.key)
      cur = cur.next
    

data = [
  ['insert', 5],
  ['insert', 2],
  ['insert', 3],
  ['insert', 1],
  ['delete', 3],
  ['insert', 6],
  ['delete', 5]
]

linked_list = LinkedList()
for tuple in data:
  if tuple[0] == 'insert':
    linked_list.insert(tuple[1])
  elif tuple[0] == 'delete':
    linked_list.delete_key(tuple[1])
    
linked_list.print_list()
  
  
    