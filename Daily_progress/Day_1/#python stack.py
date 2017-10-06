# python stack
class stack:

    def __init__(self):
        self.s = []
        self.size = 0

    def push(self, item):
        self.s.append(item)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return print("stack is empty")
        self.size -= 1
        return self.s.pop()

    def isempty(self):
        return print(self.size == 0)

    def stacksize(self):
        return self.size


st = stack()
st.push(2)
st.push(4)
print(st.s)
print(st.size)
print(st.pop())
st.isempty()
