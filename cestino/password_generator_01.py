# Password Generator
# Author: Paolo Maria Guardiani
import random

passowrd_modello = "AAA_aaa12!"

lista_minuscole = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
                   "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "W", "x", "y", "z"]

lista_maiuscole = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                   "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                   "S", "T", "U", "V", "W", "X", "Y", "Z"]

lista_numeri = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

lista_simboli = ["!", "#"]

def random_string(lista, num):
    temp_list = []
    for i in range(num):
        temp_list.append(lista[random.randint(0, len(lista) - 1)])
    print(temp_list)
    return "".join(temp_list)

password = random_string(lista_maiuscole, 3)
password += "_" 
password += random_string(lista_minuscole, 3)
password += random_string(lista_numeri, 2)
password += random_string(lista_simboli, 1)

print(password)


