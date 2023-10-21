class Node:
    def __init__(self, key =-1, val =-1, next = None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.map = []

        for _ in range(1000):
            self.map.append(Node())

    def put(self, key: int, value: int) -> None:
        curr = self.map[self.hash(key)]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            else:
                curr = curr.next

        curr.next = Node(key,value)

    def get(self, key: int) -> int:
        curr = self.map[self.hash(key)]

        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        curr = self.map[self.hash(key)]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            else:
                curr = curr.next
        

    def hash(self, key):
        return key % len(self.map) # length of map should not be zero to avoid division by zero error

H = MyHashMap()
H.put(1, 1)
H.put(2, 2)
print(H.get(1))
print(H.get(3))
H.put(2,1)
print(H.get(2))
H.remove(2)
print(H.get(2))

    
# print(1001%1000)