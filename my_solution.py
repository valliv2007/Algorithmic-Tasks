# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


def check_tree(root, numbers, check, left_stop, right_stop):
    if root.value in numbers or not check[0] :
        check[0] = False
        return False
    else:
        numbers.append(root.value)
    if root.right:
        if root.right.value <= root.value or root.right.value <= left_stop or root.right.value >= right_stop:
            check[0] = False
            return False
        else: 
            check_tree(root.right, numbers, check, root.value, right_stop)
    if root.left:
        if root.left.value >= root.value or root.left.value >= right_stop or root.left.value <= left_stop:
            check[0] = False
            return False
        else: 
            check_tree(root.left, numbers, check, left_stop, root.value)
    return check[0]
    

def solution(root):
    numbers = []
    left_stop = float('nan')
    right_stop = float('nan')
    check = [True]
    return check_tree(root, numbers, check, left_stop, right_stop)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    
    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()