import random
import pygame
import sys


def to_screen_pos(x, y, surf_size=1000):
    pos_x = int(surf_size * (x + 1) / 2)
    pos_y = int(surf_size * (y + 1) / 2)
    return pos_x, pos_y


if __name__ == "__main__":
    pygame.init()
    sc = pygame.display.set_mode((800, 800))
    font = pygame.font.SysFont('monospace', 20)
    sc.fill((55, 55, 55))

    n = m = 0
    while True:
        x = random.uniform(-1., 1.)
        y = random.uniform(-1., 1.)
        n += 1
        if x * x + y * y < 2. / 3:
            # set the radius to 2/3, which can make the probability of random
            # points locate in circle very close to 0.5
            # I think this can accellarate the convergence, not proved yet
            m += 1
            sc.set_at(to_screen_pos(x, y, 800), (255, 0, 0))
        else:
            sc.set_at(to_screen_pos(x, y, 800), (0, 0, 255))
        if n % 1000 == 0:
            hint = "{:10d}k rounds, pi ~ {:1.10f}".format(n//1000, 6 * m/n)
            text = font.render(hint, True, (255, 255, 255))
            pygame.draw.rect(sc, (55, 55, 55), text.get_rect())
            sc.blit(text, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
