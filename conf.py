import pygame
pygame.init()

char = pygame.image.load('standing.png')
anc = pygame.image.load('ancestor.png')
barr = pygame.image.load('barrier.png')
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (117, 183, 253)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
obscount = 0
x1 = 500
y1 = 820
x2 = 500
y2 = 110
width = 55
height = 60
vel = 5
obs1 = 333
obs2 = 333
obs1v = 7
obs2v = 7
obs3 = 666
obs4 = 666
obs5 = 999
obs6 = 999
jhaal = 0
score1 = 0
score2 = 0
line1 = 0
line2 = 0
line3 = 0
line4 = 0
linee1 = 0
linee2 = 0
linee3 = 0
linee4 = 0
try1 = 5
try2 = 5

font = pygame.font.SysFont('comicsansms', 50)
fonts = pygame.font.SysFont('comicsansms', 90)