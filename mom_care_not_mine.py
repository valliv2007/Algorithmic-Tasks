# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing
LOCAL = Falses

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item

def solution(node, elem):
    idx = 0
    if type(node) == 'NoneType':
        idx = -1
    else:
        while node.value != elem:
            node = node.next_item
            idx += 1
            if type(node) is 'NoneType':
                idx = -1
                return idx
                break
    return idx

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2


if __name__ == '__main__':
    test()