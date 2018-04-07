"""
@author James Whitcroft
@file conways.py
An implementation of Conway's Game of Life
"""

'''
A class to represent each cell on the board, alive and dead
@args pos, tuple integer coords representing the location of the cell
	bo, the board object that contains the cells
'''
class Cell():
	def __init__(self,pos, bo):
		self.n=[]
		self.image=' '
		self.p=pos
		self.s=bo.size
		self.b=bo
	
	'''
	function to get neighbors of current node (one at a time)
	'''
	def gN(self):
		self.n=[]
		pn=[
		(self.p[0]-1,self.p[1]-1),
		(self.p[0]-1,self.p[1]),
		(self.p[0]-1,self.p[1]+1),
		(self.p[0],self.p[1]-1),
		(self.p[0],self.p[1]+1),
		(self.p[0]+1,self.p[1]-1),
		(self.p[0]+1,self.p[1]),
		(self.p[0]+1,self.p[1]+1)
		]
		r=[]
		
		#trim the fat
		
		for x in pn:
			if (x[0] >= self.s) or (x[1] >= self.s):
				r.append(x)
			if (x[0] < 0) or (x[1] < 0):
				r.append(x)

		for g in r:
			if g in pn:
				pn.remove(g)
		
		#add if alive
		for h in pn:
			if self.b.b[h[0]][h[1]].image=='O':
				self.n.append(h)
	
'''
a class to contain all cells on the board
@args size, an int representation of n where n is nXn board
'''
class Board():
	def __init__(self, size):
		self.size=size
		self.b=[[ Cell((o,i), self) for i in range(size)] for o in range(size)]
		self.l=[]
				
				
'''
Some predefined configs
'''	
def glider(b):
	mid=b.size//2
	
	
	b.b[mid][mid+1].image='O'
	b.b[mid+2][mid+2].image='O'
	b.b[mid+2][mid].image='O'
	b.b[mid+1][mid+2].image='O'
	b.b[mid+2][mid+1].image='O'

def se(b):
	mid=b.size//2
	b.b[mid][mid].image='O'
	b.b[mid][mid+1].image='O'
	b.b[mid-1][mid].image='O'
	b.b[mid+2][mid].image='O'
	b.b[mid+1][mid+1].image='O'
	b.b[mid+1][mid-1].image='O'
	b.b[mid][mid-1].image='O'

	
def ex(b):
	mid=b.size//2
	b.b[mid][mid].image='O'
	b.b[mid+4][mid+2].image='O'
	b.b[mid+4][mid-2].image='O'
	b.b[mid+4][mid].image='O'
	b.b[mid+1][mid+2].image='O'
	b.b[mid+1][mid-2].image='O'
	b.b[mid+2][mid+2].image='O'
	b.b[mid+2][mid-2].image='O'
	b.b[mid+3][mid+2].image='O'
	b.b[mid+3][mid-2].image='O'
	b.b[mid][mid+2].image='O'
	b.b[mid][mid-2].image='O'

def nRow(b):
	i=input('N => ')
	n=int(i)
	j=0
	mid=(b.size//2)-(n//2)
	if n <1 or mid+n>=b.size:
		nRow(b)
	for c in range(n):
		b.b[(mid+n//2)][mid+j].image='O'
		j+=1
		
def ls(b):
	mid=b.size//2
	
	b.b[mid][mid].image='O'
	b.b[mid+1][mid].image='O'
	b.b[mid+2][mid].image='O'
	b.b[mid+3][mid-1].image='O'
	b.b[mid][mid-1].image='O'
	b.b[mid][mid-2].image='O'
	b.b[mid][mid-3].image='O'
	b.b[mid+1][mid-4].image='O'
	b.b[mid+3][mid-4].image='O'
	
def tum(b):
	mid=b.size//2
	
	b.b[mid][mid].image='O'
	b.b[mid+1][mid].image='O'
	b.b[mid+2][mid].image='O'
	b.b[mid+3][mid].image='O'
	b.b[mid+4][mid].image='O'
	b.b[mid+5][mid+1].image='O'
	b.b[mid+1][mid-2].image='O'
	b.b[mid+2][mid-2].image='O'
	b.b[mid+3][mid-2].image='O'
	b.b[mid+4][mid-2].image='O'
	b.b[mid+5][mid-3].image='O'
	b.b[mid][mid-2].image='O'
	b.b[mid][mid-3].image='O'
	b.b[mid][mid+1].image='O'
	b.b[mid+1][mid+1].image='O'
	b.b[mid+3][mid+2].image='O'
	b.b[mid+4][mid+2].image='O'
	b.b[mid+5][mid+2].image='O'
	b.b[mid+1][mid-3].image='O'
	b.b[mid+3][mid-4].image='O'
	b.b[mid+4][mid-4].image='O'
	b.b[mid+5][mid-4].image='O'
	
def heart(b):
	mid=b.size//2

	b.b[mid][mid].image='O'
	b.b[mid+1][mid].image='O'
	b.b[mid+3][mid].image='O'
	b.b[mid+3][mid-1].image='O'
	b.b[mid+3][mid+1].image='O'
	b.b[mid+2][mid-2].image='O'
	b.b[mid+2][mid+2].image='O'
	
def custom(b):
	l=[]
	print('\nEnter coords as ints seperated by commas\n'+
		'Seperate each coord by a semicolon ";"'+
		'\nSpaces are OK\n'
		'\nExample (2,10),(0,1),(0,2): 2,10;0,1 ; 0, 2\n')
	x=input('>>> ')
	t=x.split(';')
	g=[]
	for h in range(len(t)):
		g.append(t[h].split(','))
	for h in g:
		if int(h[0]) <0 or int(h[1]) <0:
			custom(b)
		if int(h[0]) >= b.size or int(h[1]) >=b.size:
			custom(b)
		b.b[int(h[0])][int(h[1])].image='O'
	
'''
End of predefined configs
'''	

'''
Main function handles user input
'''
def main():
	try:
		print("////////////////////////////////\n//// Conway's Game of Life ////\n//////////////////////////////\n")
		p=input("\nEnter single int board size: ")
		
		if len(p) > 2 or len(p)<1:
			main()
		s=int(p)
		if s < 6:
			input("\nNo boards smaller than 6x6... Try again buckaroo")
			main()
		
		b=Board(s)
		sup=input("1. Glider\n2. Small Exploder\n3. Exploder\n4. N Cell Row\n"
		+ "5. Lightweight Spaceship\n6. Tumble\n"
		+ "7. Muh Heart\n8. Custom\n\n>>> ")
		
		if sup=='1':
			glider(b)
		elif sup=='2':
			se(b)
		elif sup=='3':
			ex(b)
		elif sup=='4':
			nRow(b)
		elif sup=='5':
			ls(b)
		elif sup=='6':
			tum(b)
		elif sup=='7':
			heart(b)
		elif sup=='8':
			custom(b)
		else:
			main()
		go(b)	
	except:
		main()
		
'''
Main game loop, iterated manually by the user
'''
def go(b):
	go=True
	while(go):
		rm=[]
		ad=[]
		for i in range(b.size):
			for l in range(b.size):
				b.b[i][l].gN()	
		i=0
		l=0
		for i in range(b.size):
			for l in range(b.size):
				print(b.b[i][l].image,end=' ')
				#dead
				if b.b[i][l].image==' ':
					if len(b.b[i][l].n)==3:
						b.b[i][l].image='O'
				#alive
				elif b.b[i][l].image=='O':
					if len(b.b[i][l].n) < 2:
						b.b[i][l].image=' '
					if len(b.b[i][l].n) > 3:
						b.b[i][l].image=' '
			print()
		i=input("\nEnter q to quit, else ENTER to step\n>>>")
		if (i=='q'):
			go=False
main()