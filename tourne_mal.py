# Author: Giraudo Anthony                     
# 27 avril 2018
# tourne_mal.py

import pygame
from pygame.locals import *
pygame.init()
from conversions import *
from classes_tourne_mal import *
import time

# images
image_roue = "champi.png"
image_capteur = "r2d2.jpg"
dimensions_image_roue = (75, 75)
dimensions_image_capteur = (49, 49)

# parametres
largeur_chemin = 40

l = 4 * largeur_chemin # distance entre les deux roues en pixels

d = (12 * largeur_chemin) // 10 # distance entre les capteurs gauche droite en pixels

r = largeur_chemin # distance entre milieu entre les roues et milieu entre les capteurs gauche droite en pixels

coeff = 100
vitesse_de_marche = pixel(0.2)
choix = "droite"

robot = Robot(image_roue, image_capteur, dimensions_image_roue, dimensions_image_capteur, l, d, r, vitesse_de_marche, coeff, largeur_chemin)

# placement initial du robot
robot.placer(390, 692)
robot.rotation(264)

# rend le noir transparent sur les images correspondant aux roues et aux capteurs
robot.roue_gauche.image.set_colorkey((0,0,0))
robot.roue_droite.image.set_colorkey((0,0,0))
robot.capteur_interieur_droit.image.set_colorkey((255, 255, 255))
robot.capteur_interieur_gauche.image.set_colorkey((255, 255, 255))

continuer = True
rotation = False
stop = False
pas_demi_tour = False
t = time.clock()
while continuer: # boucle principale

    t_i = time.clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # arreter le programme en cas de fermeture de la fenetre
            continuer = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s: # stopper le robot en cas d appui sur la touche s
                stop = True
            if event.key == K_m: # rotation du robot en cas d appui sur la touche m
                rotation = True
            if event.key == K_d: # empeche le demi tour en cas d appui sur la touche d
                pas_demi_tour = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s: # arreter de stopper le robot en cas de relachement de la touche s
                stop = False
            if event.key == pygame.K_m: # arret de la rotation du robot en cas de relachement de la touche m
                rotation = False
            if event.key == pygame.K_d: # arret de l empechement de faire demi tour en cas de relachement de la touche d
                pas_demi_tour = False

    if stop:
        robot.stop()

    elif rotation:
        robot.rotation(3)

    elif robot.capteur_interieur_gauche.est_dans_le_noir() and not robot.capteur_interieur_droit.est_dans_le_noir():
        robot.tourner_gauche()

    elif robot.capteur_interieur_droit.est_dans_le_noir() and not robot.capteur_interieur_gauche.est_dans_le_noir():
        robot.tourner_droite()
    else:
        robot.tout_droit()

    # affichage des images
    fenetre.blit(fond, (0, 0))
    robot.afficher()
    pygame.display.flip()

    robot.mouvement(time.clock() - t_i) # deplacement du robot


pygame.quit()
