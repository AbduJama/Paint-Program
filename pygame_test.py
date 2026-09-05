import pygame

print("Starting")
pygame.init()

print("Creating window")
screen = pygame.display.set_mode((800, 600))

print("Window created")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
