import pygame

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('똥 피하기')

clock = pygame.time.Clock()

background = pygame.image.load('C:\\study\\background.png')

character = pygame.image.load('C:\\study\\character.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height




running = True
while running :
    dt = clock.tick(30)
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    
    
    screen.blit(background,(0,0))
    
    pygame.display.update()

pygame.quit()
