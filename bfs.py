class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
# Creating nodes
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")

# Connecting nodes
A.children = [B, C]
B.children = [D, E]
C.children = [F, G]


from collections import deque

def bfs(root, target):
    queue = deque([root])
    count = 0

    while queue:
        node = queue.popleft()
        count += 1

        print("Visited:", node.value)

        if node.value == target:
            print("Element found")
            print("Nodes visited:", count)
            return

        queue.extend(node.children)

    print("Element not found")

bfs(A, "F")
