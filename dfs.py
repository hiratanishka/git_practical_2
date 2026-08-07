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



def dfs(root, target):
    stack = [root]
    count = 0

    while stack:
        node = stack.pop()
        count += 1

        print("Visited:", node.value)

        if node.value == target:
            print("Element found")
            print("Nodes visited:", count)
            return

        stack.extend(reversed(node.children))

    print("Element not found")


dfs(A, "F")
