class Node:
    def __init__(self, name=None, num=None,rel=None, next=None) -> None:
        self.name=name
        self.num=num
        self.rel=rel
        self.next=None

class Sinlink:
    def __init__(self) -> None:
        self.head=None
    

    def add_node(self, name, num, rel):
        new_node = Node(name, num, rel)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def iterate(self):
      if self.head is None:
          print("The single linked list is empty")
      else:
          a=self.head
          while a is not None:
              print (a.name ,end=' ')
              print (a.num ,end=' ')
              print (a.rel ,end=' ')
              print()
              a=a.next
    
    def contains(self, name, num, rel):
        current = self.head
        while current:
            if current.num == num:
                return (True, current.name)
            current = current.next
        return (False, None)
    
    def search(self, val):
        current = self.head
        while current:
            if current.name == val or current.num== val :
                return (current.name, current.num, current.rel)
            current = current.next
        return None
    
    def modify(self, nam, numb, rela):
       current = self.head
       while current:
          if current.name == nam or current.num == numb or current.rel == rela:
             if current.name == nam:
                return (current.name, current.num, current.rel)
             if current.num == numb:
                return (current.name, current.num, current.rel)
          current = current.next
       return (None, None, None)

