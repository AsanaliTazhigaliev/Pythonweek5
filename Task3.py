class calculator():
    def __init__(self,firstnum,secondnum):
        self.firstnum=firstnum
        self.secondnum=secondnum
    def add(self):
        return self.firstnum+self.secondnum
    def subtract(self):
        return self.firstnum-self.secondnum
    def multiply(self):
        return self.firstnum*self.secondnum
    def divide(self):
        return self.firstnum/self.secondnum

calc=calculator(10,2)
result=calc.add()
print(result)
result=calc.subtract()
print(result)
result=calc.multiply()
print(result)
result=calc.divide()
print(result)