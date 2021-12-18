class account():
    def __init__(self,number):
        self.number=number
        self.balance=0
    def display(self):
        print(f"Bank Account No: {self.number}\nBalance: PLN {int(self.balance)},{int(round(self.balance%1,2)*100)}")
    def deposit(self,summ):
        self.balance+=summ
    def withdraw(self,summ):
        if summ<=self.balance:
            self.balance-=summ
        else: print("Insufficient funds on the account")
q=account(32342342)
q.display()
q.deposit(25.30)
q.display()
q.withdraw(31.70)
q.display()
q.withdraw(14)
q.display()
