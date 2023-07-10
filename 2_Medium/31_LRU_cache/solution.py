from itertools import islice
# # Tip: better to use 
# from collections import OrderedDict

class LRUCache:
    class Node:
        def __init__(self, val, key, next= None, prev = None) -> None:
            self.val = val
            self.key = key
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ptr_hashmap = {-1:self.Node(None, None)} #begin of LRU cache
        self.ptr_last = self.ptr_hashmap[-1]

    def get(self, key: int) -> int:
        if key not in self.ptr_hashmap:
            return -1
        if self.ptr_hashmap[key] == self.ptr_last:
            return self.ptr_hashmap[key].val
        else:
            self.ptr_hashmap[key].prev.next = self.ptr_hashmap[key].next
            self.ptr_hashmap[key].next.prev = self.ptr_hashmap[key].prev
            self.ptr_last.next = self.ptr_hashmap[key]
            self.ptr_last.next.prev = self.ptr_last
            self.ptr_last = self.ptr_last.next
            self.ptr_last.next = None
            return self.ptr_hashmap[key].val


    def put(self, key: int, value: int) -> None:
        if len(self.ptr_hashmap) <= self.capacity:
            if key in self.ptr_hashmap:
                if self.ptr_hashmap[key] == self.ptr_last:
                    self.ptr_last.val = value
                    return
                else:
                    self.ptr_hashmap[key].prev.next = self.ptr_hashmap[key].next
                    self.ptr_hashmap[key].next.prev = self.ptr_hashmap[key].prev
                    del self.ptr_hashmap[key]
            #put element to top
            self.ptr_last.next = self.Node(value, key, None, self.ptr_last)
            self.ptr_last = self.ptr_last.next
            #add element to hashmap
            self.ptr_hashmap[key] = self.ptr_last
        #if max capacity reached -> put new element in place of the oldest one
        else:
            #delete element with same key
            if key in self.ptr_hashmap:
                node_to_delete = self.ptr_hashmap[key]
            #or delete oldest element from hashmap
            else:
                node_to_delete = self.ptr_hashmap[-1].next
            del self.ptr_hashmap[node_to_delete.key]
            #at least 2 linked elements
            if node_to_delete.next:
                temp = self.Node(value, key)
                self.ptr_hashmap[key] = temp
                #put new element on top
                self.ptr_last.next = temp
                temp.prev = self.ptr_last
                self.ptr_last = self.ptr_last.next
                #break old link
                node_to_delete.prev.next = node_to_delete.next
                node_to_delete.next.prev = node_to_delete.prev
            #last element
            else:
                self.ptr_last.val = value
                self.ptr_last.key = key
                self.ptr_hashmap[key] = self.ptr_last


# Open the text file
with open('D:\\projects\\Python\\LeetCode\\2_Medium\\31_LRU_cache\\test15.txt', 'r') as file:
    current_line = 0
    # Read each line from the file
    for line in islice(file, 380):
        # Remove leading/trailing whitespaces and newline characters
        command = line.strip()
        current_line += 1
        # Execute the command using exec()
        exec(command)
    for line in file:
        # Remove leading/trailing whitespaces and newline characters
        command = line.strip()
        current_line += 1
        # Execute the command using exec()
        exec(command)


# obj = LRUCache(2)
# obj.put(2,1)
# obj.put(2,2)
# print(obj.get(2))
# obj.put(1,1)
# obj.put(4,1)     
# print(obj.get(2))

# obj2 = LRUCache(2)
# print(obj2.get(2))
# obj2.put(2,6)     
# print(obj2.get(1))
# obj2.put(1,5)     
# obj2.put(1,2)
# print(obj2.get(1))
# print(obj2.get(2))