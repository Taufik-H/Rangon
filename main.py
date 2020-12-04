import pygame,sys,random
from pygame.math import Vector2


# membuat class ular Rangon 
# class RANGON:
#     def __init__(self):
#         self.body = []
# membuat class makanan & reactangle makanan

class MAKANAN:
    def __init__(self):
        self.x = random.randint(0, no_cell - 1)
        self.y = random.randint(0, no_cell - 1)
        self.pos = Vector2(self.x, self.y)
    def gambar_makanan(self):
        makanan_rect = pygame.Rect(int(self.pos.x * ukuran_cell), int(self.pos.y * ukuran_cell), ukuran_cell, ukuran_cell)
        pygame.draw.rect(screen, (214, 103, 103), makanan_rect)


# DISPLAY
pygame.init()
ukuran_cell = 30
no_cell = 20
screen = pygame.display.set_mode((no_cell * ukuran_cell, no_cell * ukuran_cell))
pygame.display.set_caption('RANGON')
clock = pygame.time.Clock()

makanan = MAKANAN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((87, 212, 180))
    makanan.gambar_makanan()
    pygame.display.update()

    clock.tick(60)
