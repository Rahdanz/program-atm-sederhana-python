class atmcard:
    def __init__(self,defaultpin,defaultbalance):
        self.defaultpin=defaultpin
        self.defaultbalance=defaultbalance

    def cekPinAwal(self):
        return self.defaultpin

    def cekSaldoAwal(self):
        return self.defaultbalance
