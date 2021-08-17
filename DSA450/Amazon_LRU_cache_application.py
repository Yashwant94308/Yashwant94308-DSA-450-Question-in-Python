import gc
from collections import OrderedDict

# simple approach
# arr = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
cache_size = 2


# solution with get set function
class LeastRecentlyUsed:
    def __init__(self, cap):
        self.cap = cap
        self.cache = OrderedDict()

    def get(self, k):
        if k not in self.cache:
            return -1
        else:
            self.cache.move_to_end(k)
            return self.cache[k]

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


cache = LeastRecentlyUsed(cache_size) # capacity

cache.put(1, 1)
print(cache.cache)
cache.put(2, 2)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.put(3, 3)
print(cache.cache)
cache.get(2)
print(cache.cache)
cache.put(4, 4)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.get(3)
print(cache.cache)
cache.get(4)
print(cache.cache)

# cache = []
#
# for i in arr:
#     if i in cache:
#         cache.remove(i)
#         cache.append(i)
#     if i not in cache:
#         if len(cache) < 3:
#             cache.append(i)
#         else:
#             cache.pop(0)
#             cache.append(i)
# cache.reverse()
# print(cache)


# efficient Sol


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         if self.head is not None:
#             self.head.prev = new_node
#         self.head = new_node
#         return new_node
#
#     def delete(self, node):
#         if self.head is None or node is None:
#             return
#         if self.head == node:
#             self.head = node.next
#         if node.next is not None:
#             node.next.prev = node.prev
#         if node.prev is not None:
#             node.prev.next = node.next
#         gc.collect()
#
#     def length_of_ll(self):
#         length = 0
#         cur = self.head
#         while cur is not None:
#             length += 1
#             cur = cur.next
#         return length
#
#     def find_last(self):
#         cur = self.head
#         while cur.next is not None:
#             cur = cur.next
#         return cur
#
#     def printList(self):
#
#         node = self.head
#         while node is not None:
#             print(node.data, end=' ')
#             node = node.next
#
#
# def solution():
#     dic = {}
#     ll = LinkedList()
#     for i in arr:
#         dic[i] = None
#     for i in arr:
#         if dic[i] is not None:
#             ll.delete(dic[i])
#             nn = ll.push(i)
#             dic[i] = nn
#         else:
#             if ll.length_of_ll() < cache_size:
#                 nn = ll.push(i)
#                 dic[i] = nn
#             else:
#                 l_node = ll.find_last()
#                 dic[l_node.data] = None
#                 ll.delete(l_node)
#                 nn = ll.push(i)
#                 dic[i] = nn
#     ll.printList()
#     # print(dic)
#
#
# solution()
