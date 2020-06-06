class InsufficientFundsException(Exception):
    def __init__(self,exceptionDescrip):
        self.exceptionDescrip=exceptionDescrip

class Transaction:
    def __init__(self):
        self.AccNo         = input("Account Number      :")
        self.AccHolderName = input("Account Holder Name :")
        self.AccType       = input("Account Type        :")
        self.balance       = int(input("Account Balance     :"))

    def Withdraw(self,withAmt):
        print("Transaction Details")
        print("--------------------------------")
        print("Account Number        :","*******"+self.AccNo[7:11:1])
        print("Account Holder Name   :",self.AccHolderName)
        print("Account Type          :",self.AccType)
        print("Withdraw Amount       :",withAmt)
        try:
            if withAmt>self.balance:
                print("Total Balance         :",self.balance)
                print("Transaction Status    :Failure")
                raise InsufficientFundsException("reason: Insufficient funds in your Account")
            else:
                self.balance=self.balance-withAmt
                print("Total Balance         :", self.balance)
                print("Transaction Status    :","Success")
        except InsufficientFundsException as ex:
            print(ex)
        finally:
            print()
            print("  ******Thank You 🙂******\n  ******Visit Again******")

tx1=Transaction()
tx1.Withdraw(withAmt=int(input("Withdraw Amount : ")))