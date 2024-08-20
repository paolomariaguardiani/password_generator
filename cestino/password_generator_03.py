# Password Generator
# Author: Paolo Maria Guardiani
import random
from pathlib import Path

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
    print(temp_list)
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


for i in range(10):
    new_password = random_string_2(modello_password)
    print(new_password)     


#####
# Metodo per generare una password assolutamente casuale

print("\n*****\n")

def shuffle_string(stringa):
    temp_list = list(stringa)
    # Mescolo la lista
    random.shuffle(temp_list)
    return "".join(temp_list)

for i in range(10):
    normal_password = random_string_2(modello_password)
    shuffled_password = shuffle_string(normal_password)
    print(shuffled_password)

lista_pc_classi = read_file_txt("data/lista_pc_classi.txt")
print(lista_pc_classi)

for pc in lista_pc_classi:
    password = random_string_2(modello_password)
    print(f"{pc} ......... {password}\n")

def write_file_txt(nome_file, lista):
    path = Path(nome_file) # verrà salvato nella stessa directory del programma.exe
    
    content = ""
    for element in lista:
        password = random_string_2(modello_password)
        content += element + f" ............ {password}\n\n"

    path.write_text(content)

write_file_txt("password_pc_classi.txt", lista_pc_classi)

