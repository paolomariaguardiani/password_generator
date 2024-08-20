# Password Generator
# Author: Paolo Maria Guardiani
import random
import time
from pathlib import Path

anno = time.strftime('%Y')
mese = time.strftime('%m')
if len(mese) == 1: # se il mese è 8 diventa 08
    mese = "0" + mese
print(mese)
giorno = time.strftime('%d')

data_odierna = f"{anno}-{mese}-{giorno}"

modello_password = "AAA_aaa_33!"

lista_minuscole = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
                   "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "W", "x", "y", "z"]

lista_maiuscole = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                   "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                   "S", "T", "U", "V", "W", "X", "Y", "Z"]

lista_numeri = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

lista_simboli = ["!", "#"]

lista_pc_classi = []
lista_maestri = []

#####
# Funzione per leggere l'elenco di utenti e pc da un file di testo
def read_file_txt(percorso):
    path = Path(percorso)
    contents = path.read_text()
    lista = contents.splitlines()
    return lista




#####
# Prima versione del metodo random string

def random_string_1(lista, num):
    temp_list = []
    for i in range(num):
        temp_list.append(lista[random.randint(0, len(lista) - 1)])
    return "".join(temp_list)

# password = random_string(lista_maiuscole, 3)
# password += "_" 
# password += random_string(lista_minuscole, 3)
# password += random_string(lista_numeri, 2)
# password += random_string(lista_simboli, 1)
# print(password)
#####

#####
# Seconda versione del metodo random_string

def random_string_2(modello):
    temp_list = []
    for char in modello:
        if char == "a":
            temp_list.append(lista_minuscole[random.randint(0, len(lista_minuscole) - 1)])
        elif char == "A":
            temp_list.append(lista_maiuscole[random.randint(0, len(lista_maiuscole) - 1)])
        elif char == "3":
            temp_list.append(lista_numeri[random.randint(0, len(lista_numeri) - 1)])
        elif char == "!":
            temp_list.append(lista_simboli[random.randint(0, len(lista_simboli) -1)])
        elif char == "_":
            temp_list.append("_")
    password = "".join(temp_list)
    return password


#####
# Metodo per generare una password assolutamente casuale

print("\n*****\n")

def shuffle_string(stringa):
    temp_list = list(stringa)
    # Mescolo la lista
    random.shuffle(temp_list)
    return "".join(temp_list)

lista_pc_classi = read_file_txt("data/lista_pc_classi.txt")
lista_maestri = read_file_txt("data/lista_maestri.txt")

for pc in lista_pc_classi:
    password = random_string_2(modello_password)
    print(f"{pc} ......... {password}\n")

def write_file_txt(nome_file, lista):
    path = Path(nome_file) # verrà salvato nella stessa directory del programma.exe
    
    content = f"Passwords generate in data: {data_odierna}\n\n"
    for element in lista:
        password = random_string_2(modello_password)
        content += element + f" ............ {password}\n\n"

    path.write_text(content)

def write_difficult_passwords(nome_file, lista):
    path = Path(nome_file) # verrà salvato nella stessa directory del programma.exe
    
    content = f"Passwords generate in data: {data_odierna}\n\n"
    for element in lista:
        password = random_string_2(modello_password)
        password = shuffle_string(password)
        content += element + f" ............ {password}\n\n"

    path.write_text(content)

write_file_txt(f"{data_odierna} - passwords_pc_classi.txt", lista_pc_classi)
write_file_txt(f"{data_odierna} - passwords_maestri.txt", lista_maestri)

write_difficult_passwords(f"{data_odierna} - passwords_difficili_pc_classi.txt", lista_pc_classi)
write_difficult_passwords(f"{data_odierna} - passwords_difficili_maestri.txt", lista_maestri)

