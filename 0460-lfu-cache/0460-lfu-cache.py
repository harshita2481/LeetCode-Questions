class Node:
    def __init__(self,key,value):
        self.key=key
        self.freq=1
        self.val=value
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0

    def insertathead(self,node):
        temp=self.head.next
        self.head.next=node
        node.next=temp
        temp.prev=node
        node.prev=self.head
        self.size+=1
        return
    
    def deleteattail(self):
        node=self.tail.prev
        temp=node.prev
        temp.next=self.tail
        self.tail.prev=temp
        self.size-=1
        return node

    def delete(self,node):
        temp=node.prev
        temp.next=node.next
        node.next.prev=temp
        self.size-=1
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.limit=capacity
        self.keys={}
        self.freq={}
        self.minfreq=0
    
    def updatefreq(self,node):
        old=node.freq
        node.freq+=1
        self.freq[old].delete(node)
        if old==self.minfreq and self.freq[old].size==0:
            self.minfreq+=1

        if node.freq not in self.freq:
            self.freq[node.freq]=LinkedList()

        self.freq[node.freq].insertathead(node)

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        node=self.keys[key]
        self.updatefreq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.limit==0:
            return
        if key in self.keys:
            node=self.keys[key]
            node.val=value
            self.updatefreq(node)
            return 
        
        if len(self.keys)==self.limit:
            node=self.freq[self.minfreq].deleteattail()
            del self.keys[node.key]

        if 1 not in self.freq:
            self.freq[1]=LinkedList()

        newnode=Node(key,value)
        self.freq[1].insertathead(newnode)
        self.keys[key]=newnode
        self.minfreq=1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)