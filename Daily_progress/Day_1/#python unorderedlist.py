# python unorderedlist
class node:

    def __init__(self, element):
        self.element = element
        self.next = None

    def getelement(self):
        return self.element

    def getnext(self):
        return self.next

    def setelement(self, newelement):
        self.element = newelement

    def setnext(self, newnext):
        self.next = newnext


class unordered:

    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head == None

    def add(self, item):
        temp = node(item)
        temp.setnext(self.head)
        self.head = temp

    def getsize(self):
        current = self.head
        count = 0
        while current != None:
            current = current.getnext()
            count += 1
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getelement() == item:
                found = True
            else:
                current = current.getnext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getelement() == item:
                found = True
            else:
                previous = current
                current = current.getnext()
        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())


ul = unordered()
ul.add(95)
ul.add(100)
print(ul.getsize())
print(ul.search(100))
ul.remove(100)
print(ul.getsize())
