# Password Generator
# Author: Paolo Maria Guardiani
import pygame
import random
import time
from pathlib import Path

import message
import set_time


# prova di set_time
# st = set_time.SetTime()
# print(st.data_odierna)
# print(st.data_per_titolo)




pygame.init()
w_width = 920
w_height = 500

screen = pygame.display.set_mode((w_width, w_height))
bg_img = pygame.image.load("images/bg_img.jpg")
bg_img = pygame.transform.scale(bg_img, (w_width, w_height))
pygame.display.set_caption("Password generator")
clock = pygame.time.Clock()

anno = time.strftime('%Y')
mese = time.strftime('%m')
if len(mese) == 1: # se il mese è 8 diventa 08
    mese = "0" + mese
giorno = time.strftime('%d')

data_odierna = f"{anno}-{mese}-{giorno}"

# modello_password = "AAA_aaa_33!"
modello_password = ""


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
lista_dati = []

#####
# Funzione per leggere l'elenco di utenti e pc da un file di testo
def read_file_txt(percorso):
    path = Path(percorso)
    contents = path.read_text()
    lista = contents.splitlines()
    return lista

lista_pc_classi = read_file_txt("dati/lista_pc_classi.txt")
lista_maestri = read_file_txt("dati/lista_maestri.txt")
lista_dati = read_file_txt("dati/dati_importanti.txt")
modello_password = lista_dati[0]
percorso_di_scrittura = lista_dati[3]

#####
# Prima versione del metodo random string
# def random_string_1(lista, num):
#     temp_list = []
#     for i in range(num):
#         temp_list.append(lista[random.randint(0, len(lista) - 1)])
#     return "".join(temp_list)
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


def shuffle_string(stringa):
    temp_list = list(stringa)
    # Mescolo la lista
    random.shuffle(temp_list)
    return "".join(temp_list)


def write_file_txt(nome_file, lista):
    path = Path(nome_file) # verrà salvato nella stessa directory del programma.exe
    
    content = f"Passwords generate in data: {data_odierna}\n\n"
    for element in lista:
        password = random_string_2(modello_password)
        numero_puntini = 35 - len(element)
        content += f"{element} {numero_puntini * "."} {password}\n\n"

    path.write_text(content)

def write_difficult_passwords(nome_file, lista):
    path = Path(nome_file) # verrà salvato nella stessa directory del programma.exe
    
    content = f"Passwords generate in data: {data_odierna}\n\n"
    for element in lista:
        password = random_string_2(modello_password)
        password = shuffle_string(password)
        numero_puntini = 35 - len(element)
        content += f"{element} {numero_puntini * "."} {password}\n\n"

    path.write_text(content)

# write_file_txt(f"{data_odierna} - passwords_pc_classi.txt", lista_pc_classi)
# write_file_txt(f"{data_odierna} - passwords_maestri.txt", lista_maestri)

# write_difficult_passwords(f"{data_odierna} - passwords_difficili_pc_classi.txt", lista_pc_classi)
# write_difficult_passwords(f"{data_odierna} - passwords_difficili_maestri.txt", lista_maestri)

text1 = "[1] Crea una sola password"
text2 = "[2] Crea la lista di passwords per gli insegnanti"
text3 = "[3] Crea la lista di passwords per l'aula di informatica"
text4 = "[4] Crea la lista di passwords per i PC delle classi"
text5 = "[5] Crea la lista di passowrds per gli altri PC"
text56= "[ESC] Esci dal programma"


messaggio1 = message.Message(text1, -500, 10, 500, 50)
messaggio2 = message.Message(text2, -500, 60, 500, 50)
messaggio3 = message.Message(text3, -500, 110, 500, 50)
messaggio4 = message.Message(text4, -500, 160, 500, 50)
messaggio5 = message.Message(text5, -500, 210, 500, 50)

# button_rect_1 = messaggio1.get_rect()
# button_rect_2 = messaggio2.get_rect()
# button_rect_3 = messaggio3.get_rect()
# button_rect_4 = messaggio4.get_rect()
# button_rect_5 = messaggio5.get_rect()

gameloop = True
while gameloop:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                print("1")
            elif event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                print("2")
            elif event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                print("3")
            elif event.key == pygame.K_4 or event.key == pygame.K_KP_4:
                print("4")
            elif event.key == pygame.K_5 or event.key == pygame.K_KP_5:
                print("5")
            elif event.key == pygame.K_ESCAPE:
                gameloop = False

    # screen.fill((255, 255, 255))
    
    screen.blit(bg_img, (-10, -10))
    
    messaggio1.draw_text(screen)
    messaggio2.draw_text(screen)
    messaggio3.draw_text(screen)
    messaggio4.draw_text(screen)
    messaggio5.draw_text(screen)
    

    pygame.display.update()