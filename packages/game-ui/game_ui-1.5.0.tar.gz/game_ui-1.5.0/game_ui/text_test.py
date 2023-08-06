import pygame
from text import Text
from input import Input

pygame.init()

width, height = 1280, 720
fps = 60

win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

tx = Text(win, x = 100, y = 100, width = 500, height = 300, fontSize = 50, color = (120, 120, 120))
ip = Input(win, x = 100, y = 450, maxChars = 32)

while 1:
    clock.tick(fps)
    win.fill((0, 0, 0))
    tx.Scroll()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            tx.Press(event.unicode)
            ip.Press(event.unicode)
    
    tx.update()
    ip.update()
    
    pygame.display.update()