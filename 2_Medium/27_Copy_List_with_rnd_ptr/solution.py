from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # solution 3
        mapOldToCopy ={None : None}
        # create copies of Old Nodes
        ptr_head = head
        while(ptr_head):
            copy = Node(ptr_head.val)
            mapOldToCopy[ptr_head] = copy
            ptr_head = ptr_head.next
        # link copies same as old Nodes are linked
        ptr_head = head
        while(ptr_head):
            mapOldToCopy[ptr_head].next = mapOldToCopy[ptr_head.next]
            mapOldToCopy[ptr_head].random = mapOldToCopy[ptr_head.random]
            ptr_head = ptr_head.next
        return mapOldToCopy[ptr_head]
        

        # #solution 2
        #return deepcopy(head)

        
        # #solution 1
        # if not head:
        #     return None
        # copy_node = Node(head.val)
        # ptr_copy = copy_node
        # ptr_head = head
        # #first iteration to set singly-linked copy
        # while(ptr_head.next):
        #     ptr_copy.next = Node(ptr_head.next.val)
        #     ptr_head = ptr_head.next
        #     ptr_copy = ptr_copy.next
        # ptr_head = head
        # ptr_copy = copy_node
        # while(ptr_head):
        #     if(ptr_head.random == None):
        #         ptr_copy.random = None
        #     else:
        #         #find node which random points to
        #         temp_head = head
        #         temp_copy = copy_node
        #         while(temp_head != ptr_head.random):
        #             temp_head = temp_head.next
        #             temp_copy = temp_copy.next
        #         ptr_copy.random = temp_copy
        #     ptr_head = ptr_head.next
        #     ptr_copy = ptr_copy.next
        # return copy_node
                

        

node_idx_0 = Node(0)
node_idx_1 = Node(1)
node_idx_2 = Node(2)
node_idx_3 = Node(3)
node_idx_0.next = node_idx_1
node_idx_1.next = node_idx_2
node_idx_2.next = node_idx_3
node_idx_3.next = None
node_idx_0.random = node_idx_2
node_idx_1.random = node_idx_2
node_idx_2.random = node_idx_1
node_idx_3.random = node_idx_0

s = Solution()
s.copyRandomList(node_idx_0)