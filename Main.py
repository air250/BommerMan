import math, random, sys
import pygame
from pygame.locals import *

pygame.init()

# define display surface
ScrW = 1000
scrH = 700			
HW, HH = ScrW / 2, scrH / 2


win =  pygame.display.set_mode((ScrW, scrH))
pygame.display.set_caption("BommerMan")

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

class movement (spritesheet):
	def __init__ (self, intx = HW, inty = HH):
		self.x = intx
		self.y = inty
		
		self.wl = 9
		self.wr = 27
		self.wu = 0
		self.wd = 18

	def keys (self, spritesheet, frames):
		self.key = pygame.key.get_pressed()
		self.size = spritesheet.spriteSize()
		
		if self.key [pygame.K_LEFT]:
			if self.wl < frames + 9 :
				self.x -= 5
				spritesheet.draw(win, (self.wl) , self.x, self.y, CENTER_HANDLE)
				self.wl += 1
				if self.wl == frames + 9:
					self.wl = 9					 
		elif self.key [pygame.K_RIGHT]:
			if self.wr < frames + 27 :
				self.x += 5
				spritesheet.draw(win, (self.wr) , self.x, self.y, CENTER_HANDLE)
				self.wr += 1
				if self.wr == frames + 27:
					self.wr = 27	
		elif self.key [pygame.K_UP]:
			if self.wu < frames  :
				self.y -= 5
				spritesheet.draw(win, (self.wu) , self.x, self.y, CENTER_HANDLE)
				self.wu += 1
				if self.wu == frames:
					self.wu = 0
		elif self.key [pygame.K_DOWN]:
			if self.wd < frames + 18 :
				self.y += 5
				spritesheet.draw(win, (self.wd) , self.x, self.y, CENTER_HANDLE)
				self.wd += 1
				if self.wd == frames +18:
					self.wd = 18
		else:
			spritesheet.draw(win, 18 , self.x, self.y, CENTER_HANDLE)	
	
		#spritesheet.draw(win, 1 % index, HW, HH, CENTER_HANDLE)
		#index += 1
		pygame.display.update()
		win.fill(black)

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit(0)



#s = spritesheet(".\Movement.png", 12, 2)
s = spritesheet(".\FBI.png", 9, 4)
m = movement()


def main():
	index = 1 
	while True:
		events()
		m.keys( s,9)
		
		clock.tick(FPS)

		#m = movement(s)
		
	
		#pygame.draw.circle(win, white, (int(HW), int(HH)), 2, 0)
	
		
        
if __name__ == "__main__":
	main()
