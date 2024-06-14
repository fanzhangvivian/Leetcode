#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = dict()
        
    def get_node(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_node: # node doesnot exsit
            return None
        node = self.key_to_node[key] # node exsits
        self.remove(node) # remove it from the LRU
        self.push_front(node) # put it on the top/ the recently used in the LRUcashe
        return node

    def get(self, key):
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.get_node(key)
        if node: # if node exsits, update its value
            node.value = value
            return
        self.key_to_node[key] = node = Node(key, value) # new node
        self.push_front(node) # put it in the top/recently used in the LRU cashe
        if len(self.key_to_node) > self.capacity: # if numbers exceed the capacity
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node) # remove the last/least recently used node
        
    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev

    def push_front(self, x):
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

