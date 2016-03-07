def test_init_empty_list():
    from linked_list import LinkedList
    new_list = LinkedList()
    assert new_list.head_node.value == None
