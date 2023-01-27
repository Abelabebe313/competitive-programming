class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr_node = self.head
        prev_indx = 0
        while prev_indx < index and curr_node.next:
            curr_node = curr_node.next
            prev_indx += 1
        if curr_node and index == prev_indx:
            return curr_node.val
        return -1
        
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        prev_indx = 0
        curr_node = self.head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        while prev_indx < index-1:
            curr_node = curr_node.next
            prev_indx += 1
        if curr_node:
            new_node.next = curr_node.next
            curr_node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr_node = self.head
        prev_indx = 0
        if index == 0:
            self.head = curr_node.next
            return
        while prev_indx < index-1:
            curr_node = curr_node.next
            prev_indx += 1
        if curr_node:
            if not curr_node.next:
                curr_node.next = None
            else:
                curr_node.next = curr_node.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)