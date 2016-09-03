#-*- coding: latin1 -*-

import pygame, sys, os, random, math, time
from pygame.locals import *
from pygame.time import *
from pygame.display import *

##### Cores ######
preto = (0, 0, 0)
branco = (255, 255, 255)
##################

##### Cobra ######
x = 400
y = 300
corpo = pygame.Surface((15, 15))
corpo.fill(branco)
def cobrinha():
	global x, y, corpo
	key = pygame.key.get_pressed()
	if key[pygame.K_RIGHT]:
		x += 3
	elif key[pygame.K_LEFT]:
		x -= 3
	elif key[pygame.K_UP]:
		y -= 3
	elif key[pygame.K_DOWN]:
		y += 3
	tela.blit(corpo, (x, y))

##################

dimensao = (800, 600)
tela = pygame.display.set_mode(dimensao)
tela.fill(preto)


counter = True
clock = pygame.time.Clock()

while counter:
	clock.tick(60)
	fps = clock.get_fps()
	pygame.display.set_caption("Shazam Caraí II ## FPS: %.2f" %fps)
	for event in pygame.event.get():
		if event.type == QUIT:
			counter = False
	cobrinha()

	pygame.display.flip()
sys.exit()