import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("cozy-ho") # 게임이름

# FPS
clock = pygame.time.Clock()

# 배경화면 설정
background = pygame.image.load("/Users/agni/git/python_study/pyGAME/pygame_basic/image/background.png")

# 캐릭터 불러오기
charactor = pygame.image.load("/Users/agni/git/python_study/pyGAME/pygame_basic/image/charactor.png")
charactor_size = charactor.get_rect().size # 이미지의 크기 구하기

#캐릭터의 가로세로 크기지정
charactor_width = charactor_size[0]
charactor_height = charactor_size[1]

charactor_x_pos = screen_width/2 - charactor_width/2
charactor_y_pos = screen_height - charactor_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
speed = 0.6

# 적 캐릭터
# 적 캐릭터 불러오기
enemy = pygame.image.load("/Users/agni/git/python_study/pyGAME/pygame_basic/image/enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기 구하기

#캐릭터의 가로세로 크기지정
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

enemy_x_pos = screen_width/2 - enemy_width/2
enemy_y_pos = screen_height/2 - enemy_height/2


# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
tot_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()


running = True # 게임이 진행중인지 체크하는 변수.
while running:
    dt = clock.tick(120) # FPS 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 처리
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= speed
            elif event.key == pygame.K_RIGHT:
                to_x += speed
            elif event.key == pygame.K_UP:
                to_y -= speed
            elif event.key == pygame.K_DOWN:
                to_y += speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        
    charactor_x_pos += to_x * dt
    charactor_y_pos += to_y * dt

    if charactor_x_pos < 0:
        charactor_x_pos = 0
    elif charactor_x_pos > screen_width - charactor_width:
        charactor_x_pos = screen_width - charactor_width
    elif charactor_y_pos < 0:
        charactor_y_pos = 0
    elif charactor_y_pos > screen_height - charactor_height:
        charactor_y_pos = screen_height - charactor_height
    
    # 충돌처리
    charactor_rect = charactor.get_rect()
    charactor_rect.left = charactor_x_pos
    charactor_rect.top = charactor_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if charactor_rect.colliderect(enemy_rect):
        print("충돌!!!")
        running=False

    # screen.fill((136,133,164))
    screen.fill((0,0,0))
    # screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(charactor,(charactor_x_pos, charactor_y_pos))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s 로 변환

    timer = game_font.render(str(int(tot_time - elapsed_time)), True, (0,0,255))

    screen.blit(timer, (10,10))

    if tot_time - elapsed_time <= 0:
        print("타임 오버!!")
        running=False


    pygame.display.update() # 화면 그리기


# 게임 종료
print("게임 종료")
pygame.quit() 