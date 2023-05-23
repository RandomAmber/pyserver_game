import pygame
from network import Network
from player import Player
import world

width = world.width
height = world.height
win = world.win
# pygame.display.set_caption("Client") ?

#define game variables
tile_size = world.tile_size


#load images
# sun_img = pygame.image.load('img/sun.png')
bg_img = world.bg_img


#design grid:
def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(win, (255, 255, 255), (0, line * tile_size), (width, line * tile_size))
        pygame.draw.line(win, (255, 255, 255), (line * tile_size, 0), (line * tile_size, height))


world = world.world

def redrawWindow(win,player, player2):
    win.blit(bg_img, (0, 0))
    world.draw()
    player.draw(win)
    player2.draw(win)

    #draw_grid()
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    fps = 60

    while run:
        clock.tick(fps)
        #p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()

        p.move()

        p.apply_gravity()

        p2 = n.send(p)

        redrawWindow(win, p, p2)
        pygame.display.flip()

main()