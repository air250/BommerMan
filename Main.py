import math, random, sys
import pygame
from pygame.locals import *

pygame.init()

ScrW = 1000
scrL = 700
win =  pygame.display.set_mode((ScrW, scrL))
pygame.display.set_caption("BommerMan")
FPS = 1

speed = 5
clock = pygame.time.Clock()

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()


def main():
	while True:
		events()
        
if __name__ == "__main__":
	main()
