import pygame

############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()
# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
# 화면 타이틀 설정
pygame.display.set_caption("cozy-ho")
# FPS
clock = pygame.time.Clock()
############################################################

# 사용자 게임 초기화

running = True
while running:
    dt = clock.tick(120) # FPS 설정

    # 이벤트 처리 (키보드 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 처리
            running = False
        if event.type == pygame.KEYDOWN:
    # 캐릭터 위치 정의
    
    # 충돌 처리
    
    # 화면에 그리기

    # 충돌 체크

    # 화면에 그리기
    pygame.display.update() # 화면 그리기


# 게임 종료
print("게임 종료")
pygame.quit() 