import pygame,sys,random
from pygame.math import Vector2


# membuat class ular Rangon 
# class RANGON:
#     def __init__(self):
#         self.body = []
# membuat class makanan & rectangle makanan

class MAKANAN:
    def __init__(self):
        self.pindah_makanan()
    def gambar_makanan(self):
        makanan_rect = pygame.Rect(int(self.pos.x * ukuran_cell), int(self.pos.y * ukuran_cell), ukuran_cell, ukuran_cell)
        pygame.draw.rect(screen, (214, 103, 103), makanan_rect)
    def pindah_makanan(self):
        self.x = random.randint(0, no_cell - 1)
        self.y = random.randint(0, no_cell - 1)
        self.pos = Vector2(self.x, self.y)

# membuat ular & rectangle

class RANGON:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10),  Vector2(7, 10)]
        self.direction = Vector2(1,0)
        self.tambah_ngaceng = False
    def gambar_rangon(self):
        for block in self.body:
            x_pos = int(block.x * ukuran_cell)
            y_pos = int(block.y * ukuran_cell)
            block_rect = pygame.Rect(x_pos, y_pos, ukuran_cell, no_cell)
            pygame.draw.rect(screen, (72, 150, 189), block_rect)
               
    # menggerakan rangon
    def move_rangon(self):

        if self.tambah_ngaceng == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.tambah_ngaceng = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
    def ngaceng(self):
        self.tambah_ngaceng = True

# class main
class MAIN:
    def __init__(self):
        self.rangon = RANGON()
        self.makanan = MAKANAN()
    def update(self):
        self.rangon.move_rangon()
        self.nyepong()
    def draw_element(self):
        self.makanan.gambar_makanan()
        self.rangon.gambar_rangon()

        # kalo rangon nyepong makanan 
        # maka makanan akan berpindah & 
        # tambahkakn blok pada rangon(tambah ngatjeng)
    def nyepong(self):
        if self.makanan.pos == self.rangon.body[0]:
            self.makanan.pindah_makanan()
            self.rangon.ngaceng()

# DISPLAY
pygame.init()
ukuran_cell = 26
no_cell = 26
screen = pygame.display.set_mode((no_cell * ukuran_cell, no_cell * ukuran_cell))
pygame.display.set_caption('RANGON')
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
           main_game.update()
            # rangon keymap 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                main_game.rangon.direction = Vector2(0, -1)
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                 main_game.rangon.direction = Vector2(-1,0)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                 main_game.rangon.direction = Vector2(0, 1)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                main_game.rangon.direction = Vector2(1, 0)

    screen.fill((103, 214, 146))
    main_game.draw_element()
    pygame.display.update()

    clock.tick(60)
