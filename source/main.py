import sys, pygame, os
from sprites.ball import Ball

pygame.init() #initializing pygame

def create_path_list(folder_dir):
    path_list = []
    for file in os.listdir(folder_dir):
        file_path = folder_dir + os.sep + file
        path_list.append(file_path)
    return path_list

path_list = create_path_list("./assets/logos/")
width, height = 1000, 600                        #Adjust size of screen
size = (width, height)
speed = [2,2]                                    #Adjust x and y axis speed here
black = (0, 0, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
logo = Ball(path_list, 80, 50, speed, width, height)
allsprites = pygame.sprite.RenderPlain((logo))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT : sys.exit()
        
    clock.tick(60)                                #Keeps window at 60 fps
    allsprites.update()
    screen.fill(black)
    allsprites.draw(screen)
    pygame.display.flip()