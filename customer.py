from atm_card import atmcard

def garis():
    print('-'*60)
class customer(atmcard):
    def __init__(self,id,custpin=12345,custbalance=100000):
        self.id=id
        self.pin=custpin
        self.balance=custbalance

    def checkid(self):
        return self.id
    def checkpin(self):
        return self.pin
    def checkbalance(self):
        return self.balance
    def withdrawbalance(self,nominal):
        self.balance -=nominal
    def depositbalance(self,nominal):
        self.balance +=nominal
    


    



