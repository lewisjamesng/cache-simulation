class LinkedList:
    # made a inked list implementation as the native deque doesnt give back pointers
    # pointers are required for constant time LRU access because of the removal being O(n) by index
    def __init__(self, list):
        curr = LinkedListNode()
        self.root = curr
        for i in range(len(list)):
            curr.succ = LinkedListNode(val=list[i], prev=curr)
            curr = curr.succ

        curr.succ = LinkedListNode(prev=curr)
        self.tail = curr.succ

    def remove(self, linked_list_node):
        linked_list_node.prev.succ = linked_list_node.succ
        linked_list_node.succ.prev = linked_list_node.prev


    def addFront(self, val):
        linked_list_node = LinkedListNode(val)
        holder = self.root.succ

        # prev and succ attr
        holder.prev = linked_list_node
        self.root.succ = linked_list_node

        #  node attr
        linked_list_node.prev = self.root
        linked_list_node.succ = holder

        return linked_list_node
        
    def popBack(self):
        ret_val = self.tail.prev
        holder = self.tail.prev.prev

        holder.succ = self.tail
        self.tail.prev = holder

        return ret_val


class LinkedListNode:
    def __init__(self, val=None, prev=None, succ=None):
        self.val = val
        self.prev = prev
        self.succ = succ

    