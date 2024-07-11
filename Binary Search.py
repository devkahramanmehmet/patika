class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)
    if self.root is None:
      self.root = new_node
      return
    current = self.root
    while True:
      if value < current.value:
        if current.left is None:
          current.left = new_node
          return
        current = current.left
      else:
        if current.right is None:
          current.right = new_node
          return
        current = current.right

  # Diğer işlemler (ara, silme, gezinme vb.) burada uygulanabilir

# Verilen diziyi BST'ye ekleme
data = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]
bst = BinarySearchTree()
for value in data:
  bst.insert(value)

# BST'yi yazdırma (örnek: ön sıralı gezinme)
def preorder(node):
  if node is None:
    return
  print(node.value)
  preorder(node.left)
  preorder(node.right)

preorder(bst.root)
