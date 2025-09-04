import pygame
import math

pygame.init()
width, height = 800, 300
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


ROCKET_X = width / 2
rocket_y = height / 2

running = True

d = 0

down = True

lines = []

while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if down:
                down = False
                x1 = ROCKET_X
                y1 = rocket_y

                x2 = x1 + d * math.cos(math.radians(-45)) 
                y2 = y1 + d * math.sin(math.radians(-45))

            else:
                down = True
                x1 = ROCKET_X
                y1 = rocket_y
                x2 = x1 + abs(d) * math.cos(math.radians(225))
                y2 = y1 + abs(d) * math.sin(math.radians(225))


            lines.append([[x1, y1], [x2, y2]])

            d = 0


    d -= 1.4


    # rocket move
    pygame.draw.circle(screen, (255, 0, 0), (ROCKET_X, rocket_y), 5)

    if down:
        rocket_y -= 1

    else:
        rocket_y += 1

    if rocket_y <= 0 or rocket_y >= height: 
        exit()


    # lines move
    for i in range(len(lines)):
        for ii in range(len(lines[i])):
            first_point = lines[i][0]
            second_point = lines[i][1]

            lines[i][ii][0] -= 1

        pygame.draw.line(screen, (0, 255, 0), first_point, second_point)

    if lines != [] and lines[0][0][0] <= 0 :
        lines.pop(0)

    pygame.display.flip()
    clock.tick(180)

    print(lines)


pygame.quit() 