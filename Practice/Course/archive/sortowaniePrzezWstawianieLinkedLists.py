#sortowanie przez wstawianie w liscie odsylaczowej przy uzyciu gotowych funkcji
import math
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def l_min(head):
    if head.next == None:
        return None
    minVal = math.inf
    v = None
    while head.next != None:
        if head.next.val < minVal:
            minVal = head.next.val
            v = head
        head = head.next
    ret = v
    v.next = v.next.next
    return ret

def wstaw(head, v):
    while head.next != None:
        if head.next.val > v.val:
            v.next = head.next
            head.next = v
            return
        head = head.next
    v.next = None
    head.next = v

def sort(head):
    w = Node(None, None) #wartownik
    while head.next != None:
        v = l_min(head)
        wstaw(w, v)
    return w