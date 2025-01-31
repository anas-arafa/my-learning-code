import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
red=(255,0,0)
black=(0,0,0)
end = False
x1_change=0
y1_change=0
x1=195
y1=145
snake_block=10
clock=pygame.time.Clock()
white=(255,255,255)
while not end:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type==pygame.quit():
            end=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                x1_change=0
                y1_change=-snake_block

            if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change =+snake_block
            if event.key == pygame.K_RIGHT:
                x1_change =+ snake_block
                y1_change =0
            if event.key == pygame.K_LEFT:
                x1_change =- snake_block
                y1_change =0
                pygame.draw.rect(screen, black, ([x1, y1,5,5]))
    x1+=x1_change
    y1 += y1_change
    pygame.draw.rect(screen,red,([x_food,y_food ,10,10]))
    pygame.display.update()
    clock.tick(15)
pygame.quit()
quit()