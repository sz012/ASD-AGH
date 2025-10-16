#znajdowanie minimum i maksimum w liscie odsylaczowej
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