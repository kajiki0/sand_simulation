import pygame,pymunk,sys
from sand import Sand
from rectangle import Rectangle
pygame.init()
win_size = (400,400)
screen  = pygame.display.set_mode(win_size)

pygame.display.set_caption('Sand simulation')
clock = pygame.time.Clock()
FPS = 120

space = pymunk.Space()
space.gravity = (0,100)

sand_particles = []

sand = Sand(space)


rectangle = Rectangle(space)
horizontal_size =[[10,10],[350,10],[350,60],[10,60]]
rectangle.create(horizontal_size)


mouse_buttom = False

while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_buttom=True
        if event.type==pygame.MOUSEBUTTONUP:
            mouse_buttom=False

    if (mouse_buttom==True):
        sand_particles.append(sand.create(event.pos))
   
    
    rectangle.draw(screen,horizontal_size)
    sand.draw(screen,sand_particles)

    space.step(1/50)
    pygame.display.update()
    clock.tick(FPS)


