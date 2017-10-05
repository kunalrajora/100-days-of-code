# class variable
class emp:

    payUpdate = 1.04

    def __init__(self, first, last, pay,):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + "last" + "@gmail.com"

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    def incPay(self):
        self.pay = int(self.pay * self.payUpdate)
        # put self before using a class variable


emp1 = emp('kunal', 'rajora', 1000)

emp1.incPay()
print(emp1.pay)
