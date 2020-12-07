import pygame,sys,random
from pygame.math import Vector2



class MAKANAN:
    def __init__(self):
        self.pindah_makanan()
    def gambar_makanan(self):
        makanan_rect = pygame.Rect(int(self.pos.x * ukuran_cell), int(self.pos.y * ukuran_cell), ukuran_cell, ukuran_cell)
        screen.blit(food, makanan_rect)
    def pindah_makanan(self):
        self.x = random.randint(0, no_cell - 1)
        self.y = random.randint(0, no_cell - 1)
        self.pos = Vector2(self.x, self.y)

# membuat ular & rectangle

class RANGON:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10),  Vector2(3, 10)]
        self.direction = Vector2(1,0)
        self.tambah_ngaceng = False

        # kepala
        self.head_up = pygame.image.load('assets/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('assets/head_down.png').convert_alpha()
        self.head_left = pygame.image.load('assets/head_left.png').convert_alpha()
        self.head_right = pygame.image.load('assets/head_right.png').convert_alpha()

        # ekor
        self.tail_up = pygame.image.load('assets/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('assets/tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('assets/tail_left.png').convert_alpha()
        self.tail_right = pygame.image.load('assets/tail_right.png').convert_alpha()

        # body

        self.body_vertical = pygame.image.load('assets/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('assets/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('assets/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('assets/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('assets/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('assets/body_bl.png').convert_alpha()

    def gambar_rangon(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
            x_pos = int(block.x * ukuran_cell)
            y_pos = int(block.y * ukuran_cell)
            block_rect = pygame.Rect(x_pos, y_pos, ukuran_cell, no_cell)

            if index == 0:
                screen.blit(self.head,block_rect)

            elif index == len(self.body) -1:
                screen.blit(self.tail, block_rect)
            else: 
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)

                    # sudut:
                    # tl == top left/ atas kiri
                else: 

                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
           
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
           
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)
           
    def update_head_graphics(self):

        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down
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
        self.check_fail()
    def draw_element(self):
        self.makanan.gambar_makanan()
        self.rangon.gambar_rangon()
    def check_fail(self):
        # jika rangon menabrak screen maka quit window
        if not 0 <= self.rangon.body[0].x < no_cell or not 0 <= self.rangon.body[0].y < no_cell:
            self.game_over()
        # jika menabrak body dari rangon maka quit
        for block in self.rangon.body[1:]:
            if block == self.rangon.body[0]:
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()
        # kalo rangon nyepong makanan 
        # maka makanan akan berpindah & 
        # tambahkakn blok pada rangon(tambah ngatjeng)
    def nyepong(self):
        if  self.makanan.pos == self.rangon.body[0]:
            self.makanan.pindah_makanan()
            self.rangon.ngaceng()

# DISPLAY
pygame.init()
ukuran_cell = 35
no_cell = 20
screen = pygame.display.set_mode((700, 700))
logo = pygame.image.load('assets/logo.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('𝕽𝖆𝖓𝖌𝖔𝖓')
clock = pygame.time.Clock()
food = pygame.image.load('assets/food.png').convert_alpha()

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
                if main_game.rangon.direction.y !=1:
                    main_game.rangon.direction = Vector2(0, -1)
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if main_game.rangon.direction.x != 1:
                    main_game.rangon.direction = Vector2(-1,0)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if main_game.rangon.direction.y != -1:
                    main_game.rangon.direction = Vector2(0, 1)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if main_game.rangon.direction.x !=-1:
                    main_game.rangon.direction = Vector2(1, 0)

    screen.fill((103, 214, 146))
    main_game.draw_element()
    pygame.display.update()

    clock.tick(60)
