'''Imports'''

#Global Imports
import csv
import pygame
from pygame.constants import FULLSCREEN

#Local Imports
import moleculeInfo as mi
import formuleDevelopee as fd


'''Main'''
 

moleculeInput = "C2H5NO" #C2H5NO

#Infos de Molecules

moleculeBrute = mi.rewriter(moleculeInput)

moleculeDecomposee = mi.decomposer(moleculeBrute)

moleculeAtomes = mi.atoms(moleculeBrute)

moleculeZ = mi.numAtomique(moleculeAtomes)

moleculeValence = mi.valence(moleculeAtomes)

moleculeCovalente = mi.covalente(moleculeZ, moleculeValence)

#Formule Semi-Développée 

moleculePossible = fd.possible(moleculeDecomposee)

liaisonsPossible, liaisonsTotalP = fd.liaisons(moleculePossible, moleculeAtomes, moleculeCovalente)

moleculeFinale = fd.final(liaisonsTotalP, moleculeDecomposee, moleculePossible[0])

liaisonsFinale, liaisonsTotalF = fd.liaisons(moleculeFinale, moleculeAtomes, moleculeCovalente)

semiDeveloppe = fd.hydrogene(moleculeFinale, liaisonsFinale, moleculeAtomes)

print("semi developpé", semiDeveloppe)


'''Pygame'''

#Init
pygame.init()
clock = pygame.time.Clock()
loop = True

#Screen
pygame.display.set_caption("PyAtomic")
pygame.display.set_icon(pygame.image.load("assets/logo.jpg"))

monitor = [pygame.display.Info().current_w, pygame.display.Info().current_h]
display = pygame.display.set_mode(((768, 432)), pygame.RESIZABLE)
fullscreen = False

#Text
font = pygame.font.SysFont(name, size, bold=False, italic=False)

#GameLoop
while loop :
    
    display.fill((220,220,220))

    w, h = pygame.display.get_surface().get_size()

    for event in pygame.event.get() :
        #Quit App
        if event.type == pygame.QUIT : 
            loop = False

        #Resize App
        if event.type == pygame.VIDEORESIZE :
            if not fullscreen :
                display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        
    #mala
    pygame.draw.line(display, (0, 0, 0), (w//5, 0), (w//5, h), 3)
    pygame.draw.line(display, (0, 0, 0), (w//5, 3*(h//4)), (w, 3*(h//4)), 3)

    pygame.draw.lines(display, (0, 0, 0), True, [(0, 0), (w, 0), (w, h), (0,h)], 5)


                
        
    

    
    







    pygame.display.update()
    clock.tick(60)