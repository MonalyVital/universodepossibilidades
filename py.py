#-*- coding: latin1 -*-

import pygame, sys, os, random, math, time
from pygame.locals import *
from pygame.time import *

pygame.init()
pygame.mixer.init()

### Cores ###
branco = (255, 255, 255)
azul_piscina = (0, 255, 255)
rosa = (255,170,255)
#############

dimensao = (800, 600)
tela = pygame.display.set_mode(dimensao)
tela.fill(azul_piscina)
bomba = pygame.image.load(os.path.join("images", "bomber.png"))
espaco = pygame.image.load(os.path.join("images", "sky.jpg"))
nave = pygame.image.load(os.path.join("images", "nave.png"))
nave.set_colorkey(rosa)

caminho = os.path.join("fontes", "gta.ttf")
fonte = pygame.font.Font(caminho, 32)
fonte2 = pygame.font.Font(caminho, 120)

caminho = os.path.join("sons", "trilha.ogg")
som = pygame.mixer.Sound(caminho)
som.set_volume(0.05)

caminho = os.path.join("sons", "laser.wav")
laser = pygame.mixer.Sound(caminho)
laser.set_volume(0.05)



############ Distancia #############
def distancia(xBomba, yBomba, x2, y2):
	distancia = math.sqrt(((x2 - xBomba)**2) + ((y2 - yBomba) ** 2))
	return distancia

##################################

########## Inimigo ###############

xBomba	= 0
yBomba 	= 0
criar 	= True
raio  = 22.5

def Bomba():
	global criar, yBomba, xBomba
	if criar:
		xBomba = random.randint(20, 780)
		yBomba = 0
		criar = False	
	if yBomba > 600:
		criar = True
	
	yBomba += 2
	tela.blit(bomba, (xBomba - raio, yBomba - raio))
#################################



######### Nave ##################

x2	= 430
y2	= 530
a	= 0
b	= 0
larg	= 93
alt	= 100
frame	= 0.0
nraio  = 50

vida 	= 3
pontos	= 0

def navezinha():
	global x2, a, frame
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		x2 -= 5
	elif key[pygame.K_RIGHT]:
		x2 += 5

	if frame >= 1.0:
		a += 95
		frame = 0.0

	frame += 0.1

	if a >= (95 * 4):
		a = 0
	tela.blit(nave, (x2 - nraio, y2 - nraio), (a, b, larg, alt)) 
########################################

############# Tiro ###########
x3 = 0
y3 = 0
traio = 2.5
shot = pygame.Surface((5, 5))
shot = shot.convert()
shot.fill(branco)
pronto = True

def tiro():
	global x3, y3, pronto
	if pronto:
		x3 = x2
		y3 = 470
	if y3 < 0:
		pronto = True
	key = pygame.key.get_pressed()
	if key[pygame.K_SPACE] and pronto:
		pronto = False
		laser.play(0)
	if not pronto:
		tela.blit(shot, (x3 - traio, y3 - traio))
		y3 -= 6


#################################

def GUI():
	surface = fonte.render("Vidas: " + str(vida), True, branco)
	tela.blit(surface, (10, 10))
	surface = fonte.render("Pontos: " + str(pontos), True, branco)
	tela.blit(surface, (10, 40))

	
counter = True
clock = pygame.time.Clock()
audio = False

while counter:
	clock.tick(60)
	fps = clock.get_fps()
	pygame.display.set_caption("Shazam Caraí ## FPS: %.2f" %fps)
	if not audio:
		som.play(-1)
		audio = True
	for event in pygame.event.get():
		if event.type == QUIT:
			counter = False
	tela.blit(espaco, (0, 0))
	#som()
	Bomba()
	navezinha()
	tiro()
	GUI()

	############## Colisoes ##########
	if distancia(xBomba, yBomba, x2, y2) < (raio + nraio):
		vida -= 1
		criar = True
		print "colidiu"
	if distancia(xBomba, yBomba, x3, y3) < (raio + traio) and not pronto:
		criar = True
		pronto = True
		pontos += 1
	if vida <= 0:
		surface = fonte2.render("Game Over!", True, branco)
		tela.blit(surface, (200, 200))
		counter = False



	pygame.display.flip()
if vida < 1:
	time.sleep(2)
pygame.display.quit()
sys.exit()