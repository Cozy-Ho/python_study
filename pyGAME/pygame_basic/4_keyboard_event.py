import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("cozy-ho") # 게임이름

# 배경화면 설정
background = pygame.image.load("/Users/agni/git/python_study/pyGAME/pygame_basic/background.png")

# 캐릭터 불러오기
charactor = pygame.image.load("/Users/agni/git/python_study/pyGAME/pygame_basic/charactor.png")
charactor_size = charactor.get_rect().size # 이미지의 크기 구하기

#캐릭터의 가로세로 크기지정
charactor_width = charactor_size[0]
charactor_height = charactor_size[1]

charactor_x_pos = screen_width/2 - charactor_width/2
charactor_y_pos = screen_height - charactor_height

# 이동할 좌표
to_x = 0
to_y = 0

running = True # 게임이 진행중인지 체크하는 변수.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 처리
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        
    charactor_x_pos += to_x
    charactor_y_pos += to_y

    if charactor_x_pos < 0:
        charactor_x_pos = 0
    elif charactor_x_pos > screen_width - charactor_width:
        charactor_x_pos = screen_width - charactor_width
    elif charactor_y_pos < 0:
        charactor_y_pos = 0
    elif charactor_y_pos > screen_height - charactor_height:
        charactor_y_pos = screen_height - charactor_height

    # screen.fill((136,133,164))
    screen.fill((0,0,0))
    # screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(charactor,(charactor_x_pos, charactor_y_pos))
    pygame.display.update() # 화면 그리기


# 게임 종료
print("게임 종료")
pygame.quit() 