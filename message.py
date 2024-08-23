import pygame
pygame.init()

class Message():
    def __init__(self, testo, x, y, width, height):
        self.testo = testo
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.font = pygame.font.SysFont("Arial", 42)
        self.font.set_bold(True)
        self.font_color = (0, 25, 25)

    def draw_text(self, screen):
        # muovo il testo verso destra
        if self.x < 95:
            self.x += 3

        self.banner = self.font.render(self.testo, True, self.font_color)
        screen.blit(self.banner, (self.x, self.y))
        
