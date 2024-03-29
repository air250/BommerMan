import math, random, sys, numpy, pygame
from pygame.locals import *

pygame.init()

# define display surface
ScrW = 1280
ScrH = 720			
HW, HH = ScrW / 2, ScrH / 2


win =  pygame.display.set_mode((ScrW, ScrH))
pygame.display.set_caption("BommerMan")

w, h = pygame.display.get_surface().get_size()

vol = 10
FPS = 30
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
		return self.cellWidth, self.cellHeight, self.totalCellCount ,  self.cols , self.rows , self.sheet.get_rect().size

class movement:
	def __init__ (self, spritesheet, background, intx = HW, inty = HH):	
		self.size = spritesheet.spriteSize() # Spritesheet data
		self.BgSize = background.spriteSize()
		self.BgPosX = 0
		self.panLock = False
		self.x = intx #Sprite x posittion
		self.y = inty #Sprite y Position 
		self.index = numpy.arange(self.size[3]*self.size[4]).reshape(self.size[4], self.size[3]) # Array to handle all sprites on sprite sheet 
		self.i = 0 # Select which drirection to cycle on sprite sheet
		self.j = 0 # The sprite movement cycel 

	def xyWalk (self, spritesheet, frames, panLock = False):

		self.key = pygame.key.get_pressed()
		if self.key [pygame.K_LEFT]: 
			self.i = 1
			if panLock:
				self.x = HW	
				print("PanL")			
			else:				
				self.x -= vol 	
		elif self.key [pygame.K_RIGHT]: 
			self.i = 3	
			if panLock:
				self.x = HW	
				print("PanR")				
			else:		
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
		if self.x < 0 : self.x = ScrW
		if self.y > ScrH - self.size[1]: self.y = ScrH - self.size[1]
		if self.y < 0 : self.y = ScrH

		print (self.x,self.y)
		spritesheet.draw(win, self.index [self.i] [self.j] , self.x, self.y,0)				
		pygame.display.update()
		win.fill(black)	

	def background (self, background):
		
		self.bgWidth, self.bgHeight = self.BgSize[5]

		# background movement
		if self.x < HW:
			self.panLock = False
			print ("Flag 1 ", self.x)
		elif self.x > self.BgSize[0] - HW:
			self.panLock = False
			print ("Flag 2 ", self.x)
		else:
			print ("Flag 3 ", self.x ," ", HW)
			self.panLock = True
			self.BgPosX += -vol
		
		self.rel_x = self.BgPosX % self.bgWidth
		background.draw(win, 0 , self.rel_x - self.bgWidth, 0)
		if self.rel_x < ScrW:
			background.draw(win, 0, self.rel_x, 0)
			self.panLock = False
		
		return self.panLock

		pygame.display.update()
		win.fill(BLACK)
		
	def spriteData (self):
		return self.x, self.y, self.size	

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit(0)

def main():
	#s = spritesheet(".\Movement.png", 12, 2)
	#b = spritesheet(".\Background.jpg",1,1)
	s = spritesheet(".\FBI.png", 9, 4 )
	b = spritesheet(".\Background.jpg",1,1)
	m = movement(s,b,20,20)
	#w = movement(b,0,0)

	while True:
		events()
		center =  m.background(b)
		m.xyWalk(s, 9, center)
		#background(b)
		#w.background (b)		
		clock.tick(FPS)
		
        
if __name__ == "__main__":
	main()
