# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value
            self.right = right
            self.left = left


def find_max(root, maximum):
    if root.value > maximum[0]:
        maximum[0] = root.value
    if root.right:
        find_max(root.right, maximum)
    if root.left:
        find_max(root.left, maximum)


def solution(root):
    maximum = [0]
    find_max(root, maximum)
    return maximum[0]


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()  