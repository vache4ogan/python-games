import pygame

pygame.init()

size = (1000, 700)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

FPS = 60
speed1 = 12
speed2 = 12
y2 = 350
y1 = 350
x1 = 10
x2 = 973

BLACK = (0, 0, 0)

flup2 = fldown2 = False
flup1 = fldown1 = False

gamerun = True

ballspeedx = 9
ballspeedy = 9

ballx = 500
bally = 350

t1 = "0"
t2 = "0"

ball = pygame.Rect(ballx, bally, 30, 30)

#главный цикл
while gamerun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            gamerun = False
            quit()
    me = pygame.Rect(x1, y1, 17, 100)
    you = pygame.Rect(x2, y2, 17, 100)

    #Счет

    t1 = str(t1)
    t2 = str(t2)

    font1 = pygame.font.SysFont("arial", 50)
    text1 = font1.render(t1, 1, (255, 255, 255))

    font2 = pygame.font.SysFont("arial", 50)
    text2 = font2.render(t2, 1, (255, 255, 255))

 #передвижение мячика
    ball.x += ballspeedx
    ball.y += ballspeedy
    t1 = int(t1)
    t2 = int(t2)
    ii = True

    #Столкновение со стенами
    if ball.top <= 0 or ball.bottom >= 700:
        ballspeedy *= -1
    if ball.left <= 0:
        ballspeedx *= -1
        t2 = t2 + 1
    if ball.right >= 1000:
        ballspeedx *= -1
        t1 = t1 +1

    #столкновение с ракетками
    if ball.colliderect(me) or ball.colliderect(you):
        ballspeedx *= -1


    if ball.x <= 400 or ball.y >= 0:
        y2 = ball.y


    #управление
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y1 -= speed1
    elif keys[pygame.K_s]:
        y1 += speed1

    if y1 >= 600:
        y1 = 600
    elif y1 <= 0:
        y1 = 0
    if y2 >= 600:
        y2 = 600
    elif y2 <= 0:
        y2 = 0


    screen.fill(BLACK)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), me)
    pygame.draw.rect(screen, (255, 255, 255), you)
    pygame.draw.rect(screen, (255, 255, 255), (492, 0, 10, 700))

    screen.blit(text1, (430, 30))
    screen.blit(text2, (550, 30))


    pygame.display.update()

    clock.tick(FPS)
