import pygame


pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Move image with mouse')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('ball.bmp').convert ()

def car(x, y):
    x -= carImg.get_width() / 2
    y -= carImg.get_height() / 2
    gameDisplay.blit(carImg, (x, y))

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(black)
    car(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
