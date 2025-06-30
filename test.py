import pygame


# class grid():
#     grid = [[0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0]]


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    screen.fill("black")
    print(player_pos)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    

    pygame.draw.circle(screen, "dark green", player_pos, 40)
    
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 1000 * dt
        
    if keys[pygame.K_s]:
        player_pos.y += 1000 * dt
        
    if keys[pygame.K_a]:
        player_pos.x -= 1000 * dt
        
    if keys[pygame.K_d]:
        player_pos.x += 1000 * dt

    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(144) / 1000

pygame.quit()




# self.image = pygame.image.load("assets/Tiles/tile_0002.png")
# self.scaled_image = pygame.transform.scale(self.image, (40, 40))
#self.screen.blit(self.image, ((self.w//2) - self.image.get_width(), (self.h//2) + self.image.get_height()))
