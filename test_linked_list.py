
def test_init_empty_list():
    from linked_list import LinkedList
    new_list = LinkedList()
    assert new_list.head_node.value == None

def test_insert():
    from linked_list import LinkedList
    new_list = LinkedList()
    new_list.insert(5)
    assert new_list.head_node.value == 5
    new_list.insert(10)
    assert new_list.head_node.value == 10
    assert new_list.head_node.next.value == 5
    assert new_list.head_node.next.next.value == None

