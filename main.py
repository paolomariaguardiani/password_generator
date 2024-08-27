# Password Generator
# Author: Paolo Maria Guardiani
import pygame
import random
import time
from pathlib import Path

import message
import set_time
import read_file
import generator
import write_file


pygame.init()
w_width = 920
w_height = 500

screen = pygame.display.set_mode((w_width, w_height))
bg_img = pygame.image.load("images/bg_img.jpg")
bg_img = pygame.transform.scale(bg_img, (w_width, w_height))
pygame.display.set_caption("Password generator")
clock = pygame.time.Clock()






rf = read_file.ReadFile()
wf = write_file.WriteFile()



generate_password = generator.Generator()

# def write_file_txt(nome_file, lista):
    # path = Path(nome_file) # verrà salvato nella stessa directory del programma.exe
    # content = ""
    # # content = f"Passwords generate in data: {data_odierna}\n\n"
    # for element in lista:
    #     password = generate_password.generate_simple_password()
    #     numero_puntini = 35 - len(element)
    #     content += f"{element} {numero_puntini * '.'} {password}\n\n"

    # path.write_text(content) # write the file and close it!!!
    

# def write_difficult_passwords(nome_file, lista):
#     path = Path(nome_file) # verrà salvato nella stessa directory del programma.exe
    
#     content = ""
#     # content = f"Passwords generate in data: {data_odierna}\n\n"
#     for element in lista:
#         password = generate_password.generate_simple_password()
#         password = generate_password.shuffle_string(password)
#         numero_puntini = 35 - len(element)
#         content += f"{element} {numero_puntini * '.'} {password}\n\n"

#     path.write_text(content) # write the file and close it!!!

# write_file_txt(f"{data_odierna} - passwords_pc_classi.txt", lista_pc_classi)
# write_file_txt(f"{data_odierna} - passwords_maestri.txt", lista_maestri)

# write_difficult_passwords(f"{data_odierna} - passwords_difficili_pc_classi.txt", lista_pc_classi)
# write_difficult_passwords(f"{data_odierna} - passwords_difficili_maestri.txt", lista_maestri)

text1 = "[1] Crea una sola password"
text2 = "[2] Crea la lista di passwords per gli insegnanti"
text3 = "[3] Crea la lista di passwords per l'aula di informatica"
text4 = "[4] Crea la lista di passwords per i PC delle classi"
text5 = "[5] Crea la lista di passowords per gli altri PC"
text6= "[ESC] Esci dal programma"


messaggio1 = message.Message(text1, -500, 10, 500, 50)
messaggio2 = message.Message(text2, -500, 60, 500, 50)
messaggio3 = message.Message(text3, -500, 110, 500, 50)
messaggio4 = message.Message(text4, -500, 160, 500, 50)
messaggio5 = message.Message(text5, -500, 210, 500, 50)
messaggio6 = message.Message(text6, -500, 310, 500, 50)

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
                wf.write_one_password("password_singola.txt")
            elif event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                print("2")
                wf.write_simple_list("lista_maestri_simple.txt", rf.lista_maestri)
                wf.write_difficult_list("lista_maestri_difficult.txt", rf.lista_maestri)
            elif event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                print("3")
            elif event.key == pygame.K_4 or event.key == pygame.K_KP_4:
                print("4")
                wf.write_simple_list("lista_pc_classi_simple.txt", rf.lista_pc_classi)
                wf.write_difficult_list("lista_pc_classi_difficult.txt", rf.lista_pc_classi)
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
    messaggio6.draw_text(screen)
    

    pygame.display.update()