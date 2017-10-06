# class array
class array:

    def __init__(self, a):
        self.n = 0
        self.capacity = 1
        self.a = []

    def size(self):
        return len(self.a)

    def capacityofarray(self):
        if self.n == 0:
            self.capacity = 1
            return self.capacity
        elif self.n >= self.capacity:
            self.capacity = self.n * 2
            return self.capacity
        elif self.n <= self.capacity // 4:
            self.capacity //= 2
            return self.capacity

    def isempty(self):
        return self.n == 0

    def at(self, index):
        if self.n == 0:
            return None
        return self.a[index]

    def push(self, item):
        self.a.append(item)
        self.n += 1

    def insert(self, index, item):
        self.a.insert(index, item)
        self.n += 1

    def prepend(self, item):
        self.a.insert(0, item)
        self.n += 1

    def pop(self):
        self.n -= 1
        self.capacity -= 1
        return print(self.a.pop())

    def delete(self, index):
        del self.a[index]
        self.n -= 1

    def remove(self, item):
        while item in self.a:
            self.a.remove(item)
            self.n -= 1

    def find(self, item):
        self.places = ()
        for i in range(self.n):
            if item == self.a[i]:
                self.places += (i,)
        if self.places == ():
            return (print(-1))
        return print(self.places)


first = array([])
print(first.a)
print(first.size())
print(first.capacityofarray())
print(first.isempty())
print(first.at(0))
first.push(2)
first.insert(0, 3)
first.prepend(3)
first.pop()
first.delete(0)
first.remove(3)
first.remove(3)
first.find(2)
