import math, random, sys
import pygame
from pygame.locals import *

pygame.init()

ScrW = 1000
scrH = 700
# define display surface			
W, H = 1920, 1080
HW, HH = ScrW / 2, scrH / 2
AREA = W * H

win =  pygame.display.set_mode((ScrW, scrH))
pygame.display.set_caption("BommerMan")
FPS = 5

index = 1
CENTER_HANDLE = 4

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

speed = 5
clock = pygame.time.Clock()

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

class spritesheet:
	def __init__(self, filename, cols, rows):
		self.sheet = pygame.image.load(filename).convert_alpha()
		
		self.cols = cols
		self.rows = rows
		self.totalCellCount = cols * rows
		
		self.rect = self.sheet.get_rect()
		w = self.cellWidth = int(self.rect.width / cols)
		h = self.cellHeight = int(self.rect.height / rows)
		hw, hh = self.cellCenter = (int(w / 2), int(h / 2))
		
		self.cells = list([(i % cols * w, int(i / cols) * h, w, h) for i in range(self.totalCellCount)])
		print(self.cells)
		self.handle = list([(0, 0), (-hw, 0), (-w, 0), (0, -hh), (-hw, -hh), (-w, -hh), (0, -h), (-hw, -h), (-w, -h),])
		
	def draw(self, surface, cellIndex, x, y, handle = 0):
		surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])

#s = spritesheet("E:\Aaron\Downloads\RainbowIslandsCharacter.png", 7, 4)

s = spritesheet("E:\Aaron\Documents\GitHub\BommerMan\FBI.png", 9, 4)

def main():
	index = 1 
	while True:
		events()

		s.draw(win, index % s.totalCellCount, HW, HH, CENTER_HANDLE)
		index += 1
	
		pygame.draw.circle(win, WHITE, (int(HW), int(HH)), 2, 0)
	
		pygame.display.update()
		clock.tick(FPS)
		win.fill(BLACK)
        
if __name__ == "__main__":
	main()
