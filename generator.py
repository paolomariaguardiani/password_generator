import random
import set_time
import read_file
from pathlib import Path

rf = read_file.ReadFile()

class Generator():
    def __init__(self):
        self.modello_password = rf.modello_password
        self.lista_minuscole = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
                   "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "W", "x", "y", "z"]

        self.lista_maiuscole = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                        "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                        "S", "T", "U", "V", "W", "X", "Y", "Z"]

        self.lista_numeri = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        self.lista_simboli = ["!", "#"]

    def generate_simple_password(self):
        temp_list = []
        for char in self.modello_password:
            if char == "a":
                temp_list.append(self.lista_minuscole[random.randint(0, len(self.lista_minuscole) - 1)])
            elif char == "A":
                temp_list.append(self.lista_maiuscole[random.randint(0, len(self.lista_maiuscole) - 1)])
            elif char == "3":
                temp_list.append(self.lista_numeri[random.randint(0, len(self.lista_numeri) - 1)])
            elif char == "!":
                temp_list.append(self.lista_simboli[random.randint(0, len(self.lista_simboli) -1)])
            elif char == "_":
                temp_list.append("_")
        password = "".join(temp_list)
        return password

    def shuffle_string(self, stringa):
        temp_list = list(stringa)
        # Mescolo la lista
        random.shuffle(temp_list)
        new_stringa = "".join(temp_list)
        return new_stringa
    