class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def add_to_start(self,value):
        if not isinstance(value,Node):
            value = Node(value)
        
        if self.head == None:
            self.head = value
            self.tail = value
        else:
            value.next = self.head
            self.head = value

    def add_to_end(self,value):
        if not isinstance(value,Node):
            value = Node(value)

        if self.head == None:
            self.head = value
            self.tail = value
        else:
            self.tail.next = value
            self.tail = value

    def pop(self):
        if self.head is None:
            return None
        
        current_element = self.head
        self.head = self.head.next
        return current_element.value

    def search(self,name):
        current_elem = self.head
        while current_elem:
            if current_elem.value["name"] == name:
                return current_elem.value
            current_elem = current_elem.next
        return "Element not found"
    
    def delete(self,name):
        current_elem = self.head
        if current_elem.value["name"] == name:
            self.head = self.head.next
        else:
            while current_elem:
                if current_elem.next is not None:
                    if current_elem.next.value["name"] == name:
                        current_elem.next = current_elem.next.next
                        return
                current_elem = current_elem.next


    def __str__(self):
        current_element = self.head
        output = ""
        while current_element:
            output += (str(current_element.value) + "->")
            current_element = current_element.next
        return output

myList = LinkedList()
myList.add_to_start({"name":"Knyaz" , })
myList.add_to_end({"name":"Anna"})
myList.add_to_start({"name":"David"})
myList.delete("Knyaz")
print(myList)