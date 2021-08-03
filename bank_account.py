class Bank_account:
    all_accounts=[]
    def __init__(self,init_deposit=0,int_rate=0.5,fee_rate=5):
        self.balance=0
        self.int_rate=int_rate/100
        self.fee_rate=fee_rate
        self.deposit(init_deposit)
        Bank_account.all_accounts.append(self)

    def deposit(self,amount):
        self.balance+=amount
        return self

    def withdraw(self,amount):
        if Bank_account.can_withdraw(self.balance,amount):
            self.balance-=amount
        else:
            print (f"Insufficient funds: Charging a ${self.fee_rate} fee")
            self.balance-=self.fee_rate
        return self

    def display_account_info(self):
        print(f"Balance : ${self.balance}")
        print(f"Interest Rate : {self.int_rate*100}%")
        print(f"Fee Rate : ${self.fee_rate}/overdraft")
        print()
        return self

    def yield_interest(self):
        self.balance=round(self.balance*(1+self.int_rate))
        return self

    @staticmethod
    def can_withdraw(balance,amount):
        return balance>=amount

    @classmethod
    def display_all(cls):
        for account in cls.all_accounts:
            account.display_account_info()

a=Bank_account(2000)
b=Bank_account(500000,1.2,20)

a.deposit(100).deposit(1000).deposit(9999).withdraw(10000).yield_interest().display_account_info()
b.deposit(99).deposit(102).withdraw(9999).withdraw(10000).withdraw(4000).withdraw(11230).yield_interest().display_account_info()
Bank_account.display_all()
