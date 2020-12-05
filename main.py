import pygame,sys,random
from pygame.math import Vector2


# membuat class ular Rangon 
# class RANGON:
#     def __init__(self):
#         self.body = []
# membuat class makanan & rectangle makanan

class MAKANAN:
    def __init__(self):
        self.x = random.randint(0, no_cell - 1)
        self.y = random.randint(0, no_cell - 1)
        self.pos = Vector2(self.x, self.y)
    def gambar_makanan(self):
        makanan_rect = pygame.Rect(int(self.pos.x * ukuran_cell), int(self.pos.y * ukuran_cell), ukuran_cell, ukuran_cell)
        pygame.draw.rect(screen, (214, 103, 103), makanan_rect)

# membuat ular & rectangle

class RANGON:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10),  Vector2(7, 10)]
        self.direction = Vector2(1,0)
    def gambar_rangon(self):
        for block in self.body:
            x_pos = int(block.x * ukuran_cell)
            y_pos = int(block.y * ukuran_cell)
            block_rect = pygame.Rect(x_pos, y_pos, ukuran_cell, no_cell)
            pygame.draw.rect(screen, (72, 150, 189), block_rect)
               
    # menggerakan rangon
    def move_rangon(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]


# DISPLAY
pygame.init()
ukuran_cell = 26
no_cell = 26
screen = pygame.display.set_mode((no_cell * ukuran_cell, no_cell * ukuran_cell))
pygame.display.set_caption('RANGON')
clock = pygame.time.Clock()

makanan = MAKANAN()
rangon = RANGON()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            rangon.move_rangon()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                 rangon.direction = Vector2(0,-1)
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                 rangon.direction = Vector2(-1,0)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                 rangon.direction = Vector2(0, 1)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                 rangon.direction = Vector2(1, 0)

    screen.fill((103, 214, 146))
    makanan.gambar_makanan()
    rangon.gambar_rangon()
    pygame.display.update()

    clock.tick(60)
