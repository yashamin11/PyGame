import pygame
import math
import time
from conf import *
pygame.init()

win = pygame.display.set_mode((1000, 1000))

clock = pygame.time.Clock()
var = pygame.time.get_ticks()

run = True
time1 = 0
time2 = 0


def colldet(obsx, obsY, px, py):
    distance = math.sqrt(math.pow(px - obsx, 2) + math.pow(py - obsY, 2))
    if distance < 55:
        return True
    else:
        return False


while run:

    if jhaal == 0:
        time1 = (-var + pygame.time.get_ticks()) // 1000
    if jhaal == 1:
        time2 = (-var + pygame.time.get_ticks()) // 1000

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    win.fill(BLUE)
    pygame.draw.rect(win, YELLOW, (0, 900, 1000, 100))
    pygame.draw.rect(win, YELLOW, (0, 0, 1000, 100))
    pygame.draw.line(win, WHITE, (0, 260), (1000, 260))
    pygame.draw.line(win, WHITE, (0, 420), (1000, 420))
    pygame.draw.line(win, WHITE, (0, 580), (1000, 580))
    pygame.draw.line(win, WHITE, (0, 740), (1000, 740))
    win.blit(win, (0, 0))

    movingX = [obs1, obs2, obs3, obs4, obs5, obs6]
    movingY = [540, 380, 540, 380, 540, 380]

    win.blit(anc, (obs1, 540))
    win.blit(anc, (obs2, 380))
    win.blit(anc, (obs3, 540))
    win.blit(anc, (obs4, 380))
    win.blit(anc, (obs5, 540))
    win.blit(anc, (obs6, 380))
    win.blit(barr, (200, 220))
    win.blit(barr, (800, 220))
    win.blit(barr, (200, 700))
    win.blit(barr, (800, 700))
    win.blit(barr, (500, 220))
    win.blit(barr, (500, 700))

    fixedx = [200, 800, 200, 800, 500, 500]
    fixedY = [220, 220, 700, 700, 220, 700]

    i = 0
    text1 = font.render("Player 1:  " + str(score1), True, BLACK, YELLOW)
    t1 = font.render("No. of tries left:  " + str(try1), True, BLACK, YELLOW)
    text1rec = text1.get_rect()
    t1rec = t1.get_rect()
    t1rec.center = (800, 950)
    text1rec.center = (120, 950)
    win.blit(text1, text1rec)
    win.blit(t1, t1rec)
    time1tex = font.render("Time taken: " + str(time1), True, BLACK, YELLOW)
    time1texrec = time1tex.get_rect()
    time1texrec.center = (470, 950)
    win.blit(time1tex, time1texrec)

    if jhaal == 0 and try1 > 0:

        win.blit(char, (x1, y1))
        if keys[pygame.K_LEFT] and x1 > 0:
            x1 -= vel

        elif keys[pygame.K_RIGHT] and x1 < 1000 - vel - width:
            x1 += vel

        elif keys[pygame.K_UP] and y1 > 100:
            y1 -= vel

        elif keys[pygame.K_DOWN] and y1 < 900 - vel - width:
            y1 += vel

        if obs1 < 999:
            obs1 = obs1 + obs1v
        else:
            obs1 = 0

        if obs2 > 0:
            obs2 = obs2 - obs1v
        else:
            obs2 = 999

        if obs3 < 999:
            obs3 = obs3 + obs1v
        else:
            obs3 = 0

        if obs4 > 0:
            obs4 = obs4 - obs1v
        else:
            obs4 = 999

        if obs5 < 999:
            obs5 = obs5 + obs1v
        else:
            obs5 = 0

        if obs6 > 0:
            obs6 = obs6 - obs1v
        else:
            obs6 = 999

        if y1 < 740 and line1 == 0:
            score1 = score1 + 50 - time1 + 50
            line1 = 1

        if y1 < 580 and line2 == 0:
            score1 = score1 + 50 - time1 + 50
            line2 = 1

        if y1 < 420 and line3 == 0:
            score1 = score1 + 50 - time1 + 50
            line3 = 1

        if y1 < 260 and line4 == 0:
            score1 = score1 + 50 - time1 + 50
            line4 = 1
            jhaal = 1
            line1 = 0
            line2 = 0
            line3 = 0
            line4 = 0
            x1 = 500
            y1 = 820
            x2 = 500
            y2 = 110
            var = pygame.time.get_ticks()
            obs1v = obs1v + 2
            try1 = try1 - 1

        for i in range(6):
            wow = colldet(fixedx[i], fixedY[i], x1, y1)
            if wow:
                jhaal = 1
                try1 = try1 - 1
                line1 = 0
                line2 = 0
                line3 = 0
                line4 = 0
                x1 = 500
                y1 = 820
                x2 = 500
                y2 = 110
                var = pygame.time.get_ticks()
                break

            for i in range(6):
                wow = colldet(movingX[i], movingY[i], x1, y1)
                if wow:
                    jhaal = 1
                    try1 = try1 - 1
                    line1 = 0
                    line2 = 0
                    line3 = 0
                    line4 = 0
                    x1 = 500
                    y1 = 820
                    x2 = 500
                    y2 = 110
                    var = pygame.time.get_ticks()
                    break

    text2 = font.render("Player 2:  " + str(score2), True, BLACK, YELLOW)
    text2rec = text2.get_rect()
    t2 = font.render("No. of tries left:  " + str(try2), True, BLACK, YELLOW)
    t2rec = t1.get_rect()
    t2rec.center = (800, 50)
    text2rec.center = (120, 50)
    win.blit(text2, text2rec)
    win.blit(t2, t2rec)
    time2tex = font.render("Time taken: " + str(time2), True, BLACK, YELLOW)
    time2texrec = time2tex.get_rect()
    time2texrec.center = (470, 50)
    win.blit(time2tex, time2texrec)

    if jhaal == 1 and try2 > 0:

        win.blit(win, (0, 0))
        win.blit(char, (x2, y2))

        if keys[pygame.K_a] and x2 > 0:
            x2 -= vel

        elif keys[pygame.K_d] and x2 < 1000 - vel - width:
            x2 += vel

        elif keys[pygame.K_w] and y2 > 100:
            y2 -= vel

        elif keys[pygame.K_s] and y2 < 900 - vel - width:
            y2 += vel

        if obs1 < 999:
            obs1 = obs1 + obs2v
        else:
            obs1 = 0

        if obs2 > 0:
            obs2 = obs2 - obs2v
        else:
            obs2 = 999

        if obs3 < 999:
            obs3 = obs3 + obs2v
        else:
            obs3 = 0

        if obs4 > 0:
            obs4 = obs4 - obs2v
        else:
            obs4 = 999

        if obs5 < 999:
            obs5 = obs5 + obs2v
        else:
            obs5 = 0

        if obs6 > 0:
            obs6 = obs6 - obs2v
        else:
            obs6 = 999
        i = 0

        if y2 > 260 and linee4 == 0:
            score2 = score2 + 50 - time2 + 50
            linee4 = 1

        elif y2 > 420 and linee3 == 0:
            score2 = score2 + 50 - time2 + 50
            linee3 = 1

        elif y2 > 580 and linee2 == 0:
            score2 = score2 + 50 - time2 + 50
            linee2 = 1

        elif y2 > 740 and linee1 == 0:
            score2 = score2 + 50 - time2 + 50
            linee1 = 1
            jhaal = 0
            x1 = 500
            y1 = 820
            x2 = 500
            y2 = 120
            linee1 = 0
            linee2 = 0
            linee3 = 0
            linee4 = 0
            obs2v = obs2v + 2
            var = pygame.time.get_ticks()
            try2 = try2 - 1

        for i in range(6):
            kt = colldet(fixedx[i], fixedY[i], x2, y2)
            if kt:
                x2 = 500
                x1 = 500
                y1 = 820
                y2 = 120
                linee1 = 0
                linee2 = 0
                linee3 = 0
                linee4 = 0
                try2 = try2 - 1
                jhaal = 0
                var = pygame.time.get_ticks()
                break
        i = 0
        for i in range(6):
            kt = colldet(movingX[i], movingY[i], x2, y2)
            if kt:
                x2 = 500
                x1 = 500
                y1 = 820
                y2 = 120
                linee1 = 0
                linee2 = 0
                linee3 = 0
                linee4 = 0
                try2 = try2 - 1
                jhaal = 0
                var = pygame.time.get_ticks()
                break

    if try1 < 1 and try2 < 1:

        win.fill(GREEN)
        if score1 > score2:
            t3 = fonts.render("Player1 Wins", True, BLACK, GREEN)
        elif score2 > score1:
            t3 = fonts.render("Player2 Wins", True, BLACK, GREEN)
        else:
            t3 = fonts.render("The match is Tied", True, BLACK, GREEN)

        t3rec = t3.get_rect()
        t3rec.center = (500, 500)

        win.blit(t3, t3rec)

    pygame.display.update()
pygame.quit()
