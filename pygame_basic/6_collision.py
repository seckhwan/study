import pygame

pygame.init() #초기화 (반드시 필요한 부분)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height)) 

#화면 타이틀 설정
pygame.display.set_caption('Nado Game')

# FPS 조절
clock = pygame.time.Clock()

#배경이미지 불러오기
background = pygame.image.load('C:\\study\\background.png')

# 캐릭터 불러오기
character = pygame.image.load('C:\\study\\character.png')
character_size = character.get_rect().size #이미지의 크기를 구해옴(rect는 사각형)
character_width = character_size[0] # 케릭터 가로 크기
character_height = character_size[1] # 케릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기의 해당하는 곳에 위치, 왼쪽 오른쪽의 위치 조절 
character_y_pos = screen_height - character_height # 화면의 상하의 위치 조절

# 이동할 좌표 만들어 주기
to_x = 0
to_y = 0

# 캐릭터 이동 속도
character_speed = 0.6

# 적 캐릭터 만들기
enemy = pygame.image.load('C:\study\enemy.png')
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴(rect는 사각형)
enemy_width = enemy_size[0] # 케릭터 가로 크기
enemy_height = enemy_size[1] # 케릭터 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기의 해당하는 곳에 위치, 왼쪽 오른쪽의 위치 조절 
enemy_y_pos = (screen_height /2) - (enemy_height/2) # 화면의 상하의 위치 조절


#이벤트 루프
running = True # 게임이 진행되는가

while running :
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수 설정 (1초 동안에 몇번 동작할래 ?)
    print('fps :' + str(clock.get_fps()))
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였나 ?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했나 ?
            running = False # 게임이 진행중이 아님
        if event.type == pygame.KEYDOWN : # 키가 눌러졌는지 확인 하는것
            if event.key == pygame.K_LEFT : # 캐릭터 왼쪽 이동
                to_x -= character_speed # 왼쪽으로 character_speed만큼 이동
            elif event.key == pygame.K_RIGHT: # 캐릭터 오른쪽 이동
                to_x += character_speed # 오른쪽으로 character_speed만큼 이동
            elif event.key == pygame.K_UP: # 캐릭터 위로 이동
                to_y -= character_speed # 위로 character_speed만큼 이동
            elif event.key == pygame.K_DOWN :# 캐릭터를 아래로 이동
                to_y += character_speed # 아래로 character_speed만큼 이동
        if event.type == pygame.KEYUP : # 방향키를 떼면 멈추는 if문
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y= 0
        
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    #가로로 케릭터 안벗어나게 하기
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
    # 세로로 케릭터 안벗어나게 하기
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height
        
        
        
    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect) : # colliderect 는 충돌을 확인하는 함수
        print('충돌했어요')
        running = False
    
    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 케릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) # 적 그리기
    
    pygame.display.update() # 게임화면을 다시 그리기, 반드시 호출되어야 하는 부분 !!


# pygame 종료

pygame.quit()