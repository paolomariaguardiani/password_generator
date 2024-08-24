import time

class SetTime():
    def __init__(self):
        self.anno = time.strftime('%y')
        self.mese = time.strftime('%m')
        if len(self.mese) == 1: # se il mese è 8 diventa 08
            self.mese = "0" + self.mese
        self.giorno = time.strftime('%d')

        self.ora = time.strftime('%H')
        self.minuti = time.strftime('%M')
        self.secondi = time.strftime('%S')

        self.data_odierna = f"{self.anno}-{self.mese}-{self.giorno} - {self.ora}:{self.minuti}:{self.secondi}"
        self.data_per_titolo = f"{self.anno}-{self.mese}-{self.giorno}-{self.ora}{self.minuti}{self.secondi}"

