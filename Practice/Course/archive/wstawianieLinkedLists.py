#wstawianie w liscie odsylaczowej
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def wstaw(head, v):
    while head.next != None:
        if head.next.val > v.val:
            v.next = head.next
            head.next = v
            return
        head = head.next
    v.next = None
    head.next = v
    