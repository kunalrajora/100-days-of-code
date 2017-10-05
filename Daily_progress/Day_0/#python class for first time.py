# python class for first time
class emp:

    def __init__(self, first, last, pay,):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + "last" + "@gmail.com"

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))


emp1 = emp('kunal', 'rajora', '1')

print(emp1.fullname())
print(emp1.email)
