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
        self.direction = Vector2(0,0)
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
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

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
    def play_crunch_sound(self):
        self.crunch_sound.play()
    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10),  Vector2(3, 10)]
        self.direction = Vector2(0, 0)


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
        self.papan_catur()
        self.makanan.gambar_makanan()
        self.rangon.gambar_rangon()
        self.draw_score()
    def check_fail(self):
    
        if not 0 <= self.rangon.body[0].x < no_cell or not 0 <= self.rangon.body[0].y < no_cell:
            self.game_over()
      
        for block in self.rangon.body[1:]:
            if block == self.rangon.body[0]:
                self.game_over()
    def game_over(self):
        self.rangon.reset()
    def papan_catur(self):
        warna_papan = (142, 204, 57)
        for row in range (no_cell):
            if row % 2 ==0:
                for col in range(no_cell):
                    if col % 2 == 0:
                        papan_rect = pygame.Rect(col * ukuran_cell, row * ukuran_cell,ukuran_cell,ukuran_cell)
                        pygame.draw.rect(screen,warna_papan,papan_rect)
            else:
                for col in range(no_cell):
                    if col % 2 != 0:
                        papan_rect = pygame.Rect(col * ukuran_cell, row * ukuran_cell,ukuran_cell,ukuran_cell)
                        pygame.draw.rect(screen,warna_papan,papan_rect)
        # kalo rangon nyepong makanan 
        # maka makanan akan berpindah & 
        # tambahkakn blok pada rangon(tambah ngatjeng)
    def nyepong(self):
        if  self.makanan.pos == self.rangon.body[0]:
            self.makanan.pindah_makanan()
            self.rangon.ngaceng()
            self.rangon.play_crunch_sound()

        for block in self.rangon.body[1:]:
            if block == self.makanan.pos:
                self.makanan.pindah_makanan()
    def draw_score(self):
        score_text = str(len(self.rangon.body) -3 )
        score_surface = game_font.render(score_text, True, (57,74, 12))
        score_x = int(ukuran_cell * no_cell - 660)
        score_y = int(ukuran_cell * no_cell - 680)
        score_rect = score_surface.get_rect( center = (score_x, score_y))
        score_icon = food.get_rect(midright = (score_rect.left, score_rect.centery))

        bg_rect = pygame.Rect(score_icon.left -5, score_icon.top, score_icon.width + score_rect.width + 10, score_icon.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)

        screen.blit(score_surface,score_rect)
        screen.blit(food, score_icon)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)
# DISPLAY
#atasi delay dari sound = mixer.pre_init
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
ukuran_cell = 35
no_cell = 20
screen = pygame.display.set_mode((700, 700))
logo = pygame.image.load('assets/logo.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('Rangon kamu hebat Taufik ❤️❤️❤️')
clock = pygame.time.Clock()
food = pygame.image.load('assets/food.png').convert_alpha()
game_font = pygame.font.Font(None, 30)

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

    screen.fill((167, 217, 72))
    main_game.draw_element()
    pygame.display.update()

    clock.tick(60)
