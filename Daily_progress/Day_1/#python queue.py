# python queue
class queue:

    def __init__(self):
        self.q = []
        self.size = 0

    def isempty(self):
        return print(self.size == 0)

    def enqueue(self, item):
        self.q.insert(0, item)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.q.pop()

    def qsize(self):
        return print (self.size)


que = queue()
que.enqueue(2)
que.enqueue(4)
que.enqueue(3)
que.dequeue()
print(que.q)
que.isempty()
que.qsize()
