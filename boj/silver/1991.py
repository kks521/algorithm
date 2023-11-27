#1991, 실버1, 트리
import sys 
n = int(sys.stdin.readline())
tree = {}
def preorderTraversal(root):
    if root != '.':
        print(root, end='')
        preorderTraversal(tree[root][0])
        preorderTraversal(tree[root][1])
def inorderTraversal(root):
    if root != '.':
        inorderTraversal(tree[root][0])
        print(root, end='')
        inorderTraversal(tree[root][1])
def postorderTraversal(root):
    if root != '.':
        postorderTraversal(tree[root][0])
        postorderTraversal(tree[root][1])
        print(root, end='')
            

for _ in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left,right]

preorderTraversal('A')
print()
inorderTraversal('A')
print()
postorderTraversal('A')