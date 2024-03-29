import math, random, sys, numpy
import pygame
from pygame.locals import *

pygame.init()

# define display surface
ScrW = 1000
ScrH = 700			
HW, HH = ScrW / 2, ScrH / 2


win =  pygame.display.set_mode((ScrW, ScrH))
pygame.display.set_caption("BommerMan")

vol = 5
FPS = 10
clock = pygame.time.Clock()

# define some colors
black = (0, 0, 0, 255)
white = (255, 255, 255, 255)

CENTER_HANDLE = 4


class spritesheet:
	def __init__(self, filename, cols, rows):
		self.sheet = pygame.image.load(filename).convert_alpha()
		
		self.cols = cols
		self.rows = rows
		self.totalCellCount = cols * rows
		
		self.rect = self.sheet.get_rect()
		w = self.cellWidth = self.rect.width // cols
		h = self.cellHeight = self.rect.height // rows
		hw, hh = self.cellCenter = (w // 2, h // 2)
		
		self.cells = list([(i % cols * w, i // cols * h, w, h) for i in range(self.totalCellCount)])
		self.handle = list([(0, 0), (-hw, 0), (-w, 0), (0, -hh), (-hw, -hh), (-w, -hh), (0, -h), (-hw, -h), (-w, -h),])
		
	def draw(self, surface, cellIndex, x, y, handle = 0):
		surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
	
	def spriteSize (self):
		return self.cellWidth, self.cellHeight, self.totalCellCount ,  self.cols , self.rows

class movement:
	def __init__ (self, spritesheet, intx = HW, inty = HH):	
		self.size = spritesheet.spriteSize()
		
		self.x = intx
		self.y = inty
		self.index = numpy.arange(self.size[3]*self.size[4]).reshape(self.size[4], self.size[3])
		self.i = 0
		self.j = 0

		
	def xyWalk (self, spritesheet, frames):

		self.key = pygame.key.get_pressed()
		if self.key [pygame.K_LEFT]: 
			self.i = 1			
			self.x -= vol 	
		elif self.key [pygame.K_RIGHT]: 
			self.i = 3			
			self.x += vol
		elif self.key [pygame.K_UP]: 
			self.i = 0			
			self.y -= vol
		elif self.key [pygame.K_DOWN]: 
			self.i = 2			
			self.y += vol			 		 							
		else :
			self.i = 2
			self.j = 0	
		
		self.j += 1
		if self.j == frames: self.j = 0

		if self.x > ScrW - self.size[0]: self.x = ScrW - self.size[0]
		if self.x < ScrW : self.x = ScrW
		if self.y > ScrH - self.size[1]: self.y = ScrH - self.size[1]
		if self.y < ScrH : self.x = ScrH

		#if 

		if self.x < HW: circlePosX = self.x
	#	elif self.x > stageWidth - startScrollingPosX: circlePosX = self.x - self.size[0] + W
		else:
			circlePosX = startScrollingPosX
			stagePosX += - vol
	
		self.rel_x = stagePosX % 2000
		spritesheet.draw(win, 0,self.rel_x - 2000,0)
		#DS.blit(bg, (self.rel_x - bgWidth, 0))
		if self.rel_x < W:
			spritesheet.draw(win, 0,self.rel_x,0)
			#DS.blit(bg, (self.rel_x, 0))

		spritesheet.draw(win, self.index [self.i] [self.j] , self.x, self.y,0)			
		pygame.display.update()

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit(0)

def main():
	#s = spritesheet(".\Movement.png", 12, 2)
	b = spritesheet(".\Background.jpg",1,1)
	s = spritesheet(".\FBI.png", 9, 4)
	m = movement(s)
	w = movement(b)

	while True:
		events()
		m.xyWalk(s, 9)		
		clock.tick(FPS)
		
        
if __name__ == "__main__":
	main()
