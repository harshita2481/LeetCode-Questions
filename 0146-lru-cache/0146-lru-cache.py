class Node:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.prev=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertathead(self,node):
        newnode=node
        newnode.prev=self.head
        temp=self.head.next
        newnode.next=temp
        self.head.next=newnode
        temp.prev=newnode
        return 
    def deleteattail(self):
        if self.tail.prev==self.head:
            return None
        node=self.tail.prev
        self.tail.prev=node.prev
        node.prev.next=self.tail
        return node 
    def delete(self,node):
        temp=node.prev
        temp.next=node.next
        node.next.prev=temp
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.cache=LinkedList()
        self.hm={}
        self.limit=capacity

    def get(self, key: int) -> int:
        if key in self.hm:
            node=self.hm[key]
            self.cache.delete(node)
            self.cache.insertathead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node=self.hm[key]
            node.val=value
            self.cache.delete(node)
            self.cache.insertathead(node)
            return 
        if len(self.hm)==self.limit:
            node=self.cache.deleteattail()
            del self.hm[node.key]
        newnode=Node(key,value)
        self.cache.insertathead(newnode)
        self.hm[key]=newnode


        
        
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)