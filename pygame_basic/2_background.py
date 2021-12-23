import pygame

pygame.init() #초기화 (반드시 필요한 부분)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height)) 

#화면 타이틀 설정
pygame.display.set_caption('Nado Game')

#배경이미지 불러오기

background = pygame.image.load('C:\\study\\background.png')

#이벤트 루프
running = True # 게임이 진행되는가

while running :
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였나 ?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했나 ?
            running = False # 게임이 진행중이 아님
    
    #screen.fill((0,0,255))  # 색깔 채우기       
    screen.blit(background, (0,0)) # 배경 그리기
    
    pygame.display.update() # 게임화면을 다시 그리기, 반드시 호출되어야 하는 부분 !!


# pygame 종료

pygame.quit()