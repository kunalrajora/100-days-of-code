# stack by linklist
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


class stacklist:

    def __init__(self):
        self.head = None

    def isempty(self):
        return print(self.head == None)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getnext()
        return count

    def push(self, item):
        current = self.head
        temp = node(item)
        temp.setnext(current)
        self.head = temp

    def pop(self):
        if self.head == None:
            return print("already Empty")
        self.head = self.head.getnext()


st = stacklist()
print(st.size())
st.push(12)
st.push(15)
print(st.size())
print(st.head.getelement())
st.pop()
print(st.head.getelement())
st.pop()
st.pop()
st.isempty()
