# python orderedlist
class Node:

    def __init__(self, element):
        self.element = element
        self.next = None

    def getelement(self):
        return self.element

    def getnext(self):
        return self.next

    def setelement(self, element):
        self.element = element

    def setnext(self, newnext):
        self.next = newnext


class ordered:

    def __init__(self):
        self.head = None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getnext()
        return count

    def isempty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getelement() > item:
                stop = True
            else:
                previous = current
                current = current.getnext()

        temp = Node(item)
        if previous == None:
            temp.setnext(self.head)
            self.head = temp
        else:
            temp.setnext(current)
            previous.setnext(temp)

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getelement() == item:
                found = True
            elif current.getelement() >= item:
                break
            else:
                current = current.getnext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getelement() >= item:
                stop = True
            else:
                previous = current
                current = current.getnext()

        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())


od = ordered()
od.add(12)
print(od.search(12))
print(od.head.getelement())
print(od.size())
print(od.isempty())
od.add(13)
print(od.size())
od.remove(12)
print(od.head.getelement())
