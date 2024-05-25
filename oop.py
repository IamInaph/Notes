#e.g
class Student:
    def __init__(self,name,marks): # parametarized constructor
        self.name = name
        self.marks = marks  
    
    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print( self.name," your avg marks:", sum/3)

s1 = Student("Srijana",[100,56,78]) 
s1.get_avg()     


#e.g 

class Account:
    def __init__(self,accno,accname,inititial_balance =0):
        self.accno = accno
        self.accname = accname
        self.balance = inititial_balance

    def debit(self,amount):
        if amount > self.balance:
            print("insufficient balance")

        else :
            self.balance -= amount
            print("your balance is debited by RS.", self.balance)

    def credit(self,amount):
        self.balance += amount
        print("your balance is credited by RS.", self.balance)

    def print_balance(self):
        print("your current balance is:", self.balance)


A = Account(47478,"Srijana",60000)
A.print_balance()
A.debit(900)

A.credit(4000)
A.print_balance()
