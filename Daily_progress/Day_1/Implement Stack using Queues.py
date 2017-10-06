class MyStack(object):

    def __init__(self):
        self.stack=[]


    def push(self, x):
        self.stack.append(x)



    def pop(self):
        self.stack.reverse()
        k=self.stack.pop(0)
        self.stack.reverse()
        return k

    def top(self):
        return self.stack[-1]


    def empty(self):
        return len(self.stack)==0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
