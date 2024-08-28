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

# Carico la sigla del programma e i suoni
pygame.mixer.music.load("sounds/sigla.wav")
pygame.mixer.music.play(1) # -1 = play the music forever; 1 = only one time

dot_printer_1 = pygame.mixer.Sound("sounds/dot_printer_1.wav")
dot_printer_2 = pygame.mixer.Sound("sounds/dot_printer_2.wav")


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

text1 = "[1] Crea una sola password"
text2 = "[2] Crea la lista di passwords per gli insegnanti"
text3 = "[3] Crea la lista di passwords per l'aula di informatica"
text4 = "[4] Crea la lista di passwords per i PC delle classi"
text5 = "[5] Crea la lista di passowords per gli altri PC"
text6= "[ESC] Esci dal programma"

rect1 = pygame.Rect(-500, 10, 500, 50)

messaggio1 = message.Message(text1, rect1.x, rect1.y, rect1.width, rect1.height)
messaggio2 = message.Message(text2, -500, 60, 500, 50)
messaggio3 = message.Message(text3, -500, 110, 500, 50)
messaggio4 = message.Message(text4, -500, 160, 500, 50)
messaggio5 = message.Message(text5, -500, 210, 500, 50)
messaggio6 = message.Message(text6, -500, 310, 500, 50)


gameloop = True
while gameloop:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                print("1")
                dot_printer_1.play()
                wf.write_one_password("password_singola.txt")
            elif event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                print("2")
                dot_printer_1.play()
                wf.write_simple_list("lista_maestri_simple.txt", rf.lista_maestri)
                wf.write_difficult_list("lista_maestri_difficult.txt", rf.lista_maestri)
            elif event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                print("3")
            elif event.key == pygame.K_4 or event.key == pygame.K_KP_4:
                print("4")
                dot_printer_1.play()
                wf.write_simple_list("lista_pc_classi_simple.txt", rf.lista_pc_classi)
                wf.write_difficult_list("lista_pc_classi_difficult.txt", rf.lista_pc_classi)
            elif event.key == pygame.K_5 or event.key == pygame.K_KP_5:
                print("5")
            elif event.key == pygame.K_ESCAPE:
                gameloop = False

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == pygame.BUTTON_LEFT:
        #         pos = pygame.mouse.get_pos() # thanks to https://youtu.be/7LeFPozRprU
        #         # print(f"left button pressed, {mx, my}")
        #         if rect1.collidepoint(pos):
        #             print("collidepoint!")

    # screen.fill((255, 255, 255))
    
    screen.blit(bg_img, (-10, -10))
    
    
    messaggio1.draw_text(screen)
    messaggio2.draw_text(screen)
    messaggio3.draw_text(screen)
    messaggio4.draw_text(screen)
    messaggio5.draw_text(screen)
    messaggio6.draw_text(screen)
    

    pygame.display.update()