import sys

import pygame
from Constants import ConstantsMides
from Constants import ConstantsColors
from Jugador import Jugador
from Pelota import Pelota

pygame.init()


pantalla = (800, 600)

Jugador1 = Jugador(15,250,(79, 186, 249))
Jugador2 = Jugador(770,250,(252, 93, 77))
pelota = Pelota(375,275,5,5,(255,255,255))

finestraJoc = pygame.display.set_mode(pantalla)
rellotge = pygame.time.Clock()
fontText = pygame.font.SysFont("monospace", 35)

gameOver = False
def pintar():
    finestraJoc.fill(ConstantsColors.tuplaColorFondo)
    pygame.draw.rect(finestraJoc,ConstantsColors.tuplaColorMargenes,ConstantsMides.tuplaMargenSuperior)
    pygame.draw.rect(finestraJoc,ConstantsColors.tuplaColorMargenes, ConstantsMides.tuplaMargenInferior)
    pygame.draw.rect(finestraJoc, Jugador1.color, (Jugador1.posX, Jugador1.posY, Jugador1.midaX, Jugador1.midaY))
    pygame.draw.rect(finestraJoc, Jugador2.color, (Jugador2.posX, Jugador2.posY, Jugador2.midaX, Jugador2.midaY))
    pygame.draw.circle(finestraJoc,pelota.color,(pelota.posicioX, pelota.posicioY), pelota.medida)

    textoJugador1 = "Jugador 1: " + str(Jugador1.puntos)
    etiquetaJugador1 = fontText.render(textoJugador1, 1, (0,0,0))
    finestraJoc.blit(etiquetaJugador1, (35, 50))

    textoJugador2= "Jugador 2: " + str(Jugador2.puntos)
    etiquetaJugador2 = fontText.render(textoJugador2, 1, (0, 0, 0))
    finestraJoc.blit(etiquetaJugador2, (500, 50))


def detectarEventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            a = pygame.key.get_pressed()
    if pygame.key.get_pressed()[pygame.K_w] == True:
        Jugador1.posY = Jugador1.posY - Jugador1.velocidad
        if Jugador1.posY == 20:
            Jugador1.posY = 25

    if pygame.key.get_pressed()[pygame.K_s] == True:
        Jugador1.posY = Jugador1.posY + Jugador1.velocidad
        if Jugador1.posY == 500:
            Jugador1.posY = 495

    if pygame.key.get_pressed()[pygame.K_UP] == True:
        Jugador2.posY = Jugador2.posY - Jugador2.velocidad
        if Jugador2.posY == 20:
            Jugador2.posY = 25
    if pygame.key.get_pressed()[pygame.K_DOWN] == True:
        Jugador2.posY = Jugador2.posY + Jugador2.velocidad
        if Jugador2.posY == 500:
            Jugador2.posY = 495
    moverPelota()

def moverPelota():
    pelota.posicioY += pelota.velY
    pelota.posicioX += pelota.velX

    if (pelota.posicioY >= 567):
        pelota.velY *= -1
    if(pelota.posicioY <= 40):
        pelota.velY *= -1
    if(pelota.posicioX >= 800):
        pelota.posicioY = 275
        pelota.posicioX = 375
        pelota.velX *= -1
        Jugador1.puntos = Jugador1.puntos + 1
    if(pelota.posicioX <= 0):
        pelota.posicioY = 275
        pelota.posicioX = 375
        pelota.velX *= -1
        Jugador2.puntos = Jugador2.puntos + 1

    if(pelota.posicioX + pelota.velX - pelota.medida <= Jugador1.posX + Jugador1.midaX):
        if(pelota.posicioY >= Jugador1.posY and pelota.posicioY < Jugador1.posY + Jugador1.midaY ):
            pelota.velX *= -1
            pelota.velY = pelota.velY + 1
            pelota.velX = pelota.velX + 1
            print(str(pelota.velX) + "-" + str(pelota.velY))
    if (pelota.posicioX + abs(pelota.velX) + pelota.medida >= Jugador2.posX):
        if (pelota.posicioY >= Jugador2.posY and pelota.posicioY < Jugador2.posY + Jugador2.midaY):
            pelota.velX *= -1
            pelota.velY = pelota.velY + 1
            pelota.velX = pelota.velX + 1
            print(str(pelota.velX)+"-"+str(pelota.velY))


while (gameOver == False):
    rellotge.tick(30)
    pygame.display.update()
    pintar()
    detectarEventos()




