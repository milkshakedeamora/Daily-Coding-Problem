class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    def string(node):
      if not node:
        return ""
      left= string(node.left)
      right= string(node.right)
      return str(node.val)+" "+ left + right
    return string(root) 

def deserialize(s):
    nodes = s.split(" ")

    def tree():
        if not nodes:
          return 
        val = nodes.pop(0)
        if val == "null" :            
            return None        
        node = Node(val)
        node.left = tree()
        node.right = tree()
        return node 
    return tree()

    
    
        

 


node = Node('root', Node('left', Node('left.left'),Node('left.right')), Node('right'))
print(serialize(node))
print(serialize(deserialize(serialize(node))))
assert deserialize(serialize(node)).left.left.val == 'left.left'
print("assert Ok")
