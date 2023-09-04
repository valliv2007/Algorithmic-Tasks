# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item


def solution(node, idx):
    # Your code
    # ヽ(´▽`)/
    previous_head = node
    if idx == 0:
        new_head = node.next_item
        del node
        return new_head  
    while idx - 1:
        node = node.next_item
        idx -= 1
    deleted_node = node.next_item
    node.next_item = node.next_item.next_item
    del deleted_node
    return previous_head


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3
    del node1
    print(node1.value)

if __name__ == '__main__':
    test()
