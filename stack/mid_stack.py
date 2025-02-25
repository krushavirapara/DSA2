class DLLNode:
    def __init__(self, d):
        self.prev = None
        self.data = d
        self.next = None

class myStack:
    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 0

def createMyStack():
    ms = myStack()
    return ms

def push(ms, val):
    new = DLLNode(val)
    if not ms.head:
        ms.head = new
        ms.mid = ms.head
    else:
        ms.head.next = new
        new.prev = ms.head
        ms.head = new
        if ms.count % 2 == 1:  # Adjust mid when count is odd (moving to even count)
            ms.mid = ms.mid.next
    ms.count += 1

def pop(ms):
    if not ms.head:
        return None
    val = ms.head.data
    ms.head = ms.head.prev
    if ms.head:
        ms.head.next = None
    ms.count -= 1
    if ms.count % 2 == 0 and ms.mid:  # Adjust mid when count becomes even
        ms.mid = ms.mid.prev
    return val

def find(ms):
    if ms.mid:
        return ms.mid.data
    return None

def deletemiddle(ms):
    if not ms.mid:
        return None
    val = ms.mid.data
    if ms.count == 1:
        ms.head = None
        ms.mid = None
    else:
        if ms.mid.prev:
            ms.mid.prev.next = ms.mid.next
        if ms.mid.next:
            ms.mid.next.prev = ms.mid.prev
        if ms.count % 2 == 0:
            ms.mid = ms.mid.prev
        else:
            ms.mid = ms.mid.next
    ms.count -= 1
    return val

# Test case
ms = createMyStack()
push(ms, 2)
push(ms, 5)
print("Middle Element:", find(ms))  # Should be 5
push(ms, 3)
push(ms, 7)
push(ms, 4)
print("Middle Element:", find(ms))  # Should be 3
print("Deleted Middle Element:", deletemiddle(ms))  # Should delete 3
print("Middle Element:", find(ms))  # Should be 5
print("Deleted Middle Element:", deletemiddle(ms))  # Should delete 5
print("Middle Element:", find(ms))  # Should be 7
print("Popped Element:", pop(ms))  # Should pop 4
print("Popped Element:", pop(ms))  # Should pop 7
print("Deleted Middle Element:", deletemiddle(ms))  # Should delete 2

