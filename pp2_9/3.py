import pygame
import sys
 
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Red Ball Game")
red = (255,0,0)
white = (255,255,255)
radius = 25
x = 800//2
y = 600//2
running = True
move = 20
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                x+=move
                if x>800-radius:
                    x=800-radius
            elif event.key==pygame.K_LEFT:
                x-=move
                if x<radius:
                    x=radius
            elif event.key==pygame.K_UP:
                y-=move
                if y<radius:
                    y=radius
            elif event.key==pygame.K_DOWN:
                y+=move
                if y>600-radius:
                    y=600-radius

    screen.fill(white)
    pygame.draw.circle(screen,red,(x,y), radius)
    pygame.display.flip()

pygame.quit()
sys.exit()