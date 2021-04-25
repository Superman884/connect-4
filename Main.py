import pygame
from random import randrange
import keyboard
from time import sleep
run=True
win=pygame.display.set_mode((534,534))
wid=7
won=None
hei=6
board=[]
image=pygame.image.load('img.png')
win.blit(image,(0,0))
for i in range(hei):
	stuff=[]
	for j in range(wid):
		stuff.append(0)
	board.append(stuff)
disk_gap=65
start=40
turn=1
def gravity(arr):
	for i in range(len(arr[0])):
		for j in range(len(arr)):
			if arr[j][i]==0 or  j==len(arr)-1:
				pass
			else:
				if arr[j+1][i]==0:
					arr[j+1][i]=arr[j][i]
					arr[j][i]=0
	return arr
def draw(arr, gap,x,y):
	for i in arr:
		for j in i:
			if j==0:
				color=(255,255,255)
			elif j==1:
				color=(255,0,0)
			else:
				color=(255,242,0)
			pygame.draw.ellipse(win, color,(x+8,y+8,gap-16,gap-16))
			x+=gap
		x=start
		y+=gap
	pygame.display.update()
x=start
y=start-10
notation=''
draw(board,disk_gap,x,y)
xranko=None
yranko=None
while run:
	pos=pygame.mouse.get_pos()
	xpos=(pos[0]-start)
	xrank=xpos//disk_gap
	yrank=hei-1
	if xrank!=7:
		for i in board[::-1]:
			if i[xrank]==0:
				break
			else:
				yrank-=1
	if xrank==xranko and yrank==yranko:
		pass
	else:
		xp=xrank*disk_gap+start
		yp=yrank*disk_gap+(start-10)
		if xranko!=None and xranko>=0 and xranko<wid:
			xpo=xranko*disk_gap+start
			ypo=yranko*disk_gap+(start-10)
			pygame.draw.ellipse(win, (255,255,255),(xpo+8,ypo+8,disk_gap-16,disk_gap-16))
		if xrank>=0 and xrank<wid:
			if turn%2==0:
				color=(200,25,25)
			else:
				color=(183,173,0)
			pygame.draw.ellipse(win, color,(xp+8,yp+8,disk_gap-16,disk_gap-16))
		xranko=xrank
		yranko=yrank
		pygame.display.update()
	up=False
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		if event.type==pygame.MOUSEBUTTONUP:
			up=True
	if up or (turn%2!=0 and False):
		if turn%2!=0 or True:
			pos=pygame.mouse.get_pos()
			xpos=(pos[0]-start)
			xrank=xpos//disk_gap
		else:
			xrank=randrange(wid)
		yrank=0
		if xrank<0 or xrank>len(board[0])-1:
			fine=False
		else:
			fine=True
		if fine:
			if board[yrank][xrank]==0:
				xranko=xrank
				yranko=yrank
				notation+=str(xrank-1)
				board[yrank][xrank]=turn%2+1
				turn+=1
				board=gravity(board)
				draw(board,disk_gap,x,y)
				s0=False
				for i in board:
					for j in i:
						if j==0:
							s0=True
							break
					if s0:
						break
				if not s0:
					won=3
					break
				for p in range(len(board)):
					i=board[p]
					thing=i[0]
					count=0
					thefour=[]
					for k in range(len(i)):
						j=i[k]
						if j==thing and j!=0:
							count+=1
							thefour.append((k,p))
							if count==4:
								won=thing
						else:
							count=1
							thing=j
						if won!=None:
							break
					if won!=None:
						break
				if won==None:
					for i in range(wid):
						thing=board[0][i]
						thefour=[]
						for j in range(hei):
							curr=board[j][i]
							if curr==thing and curr!=0:
								count+=1
								thefour.append((i,j))
								if count==4:
									won=thing
							else:
								count=1
								thing=curr
				if won==None:
					things=[]
					for xx in range(wid):
						for yy in range(hei):
							stuff=[]
							x1=xx
							y1=yy
							runy=True
							while runy:
								if keyboard.is_pressed('ctrl'):
									runy=False
								try:
									curr=board[y1][x1]
									stuff.append(curr)
									x1+=1
									y1+=1
								except:
									runy=False
							things.append(stuff)
					thefour=[]
					for i in things:
						if len(i)<4:
							continue
						things=i[0]
						count=0
						for j in i:
							if j==thing and j!=0:
								count+=1
								if count==4:
									won=thing
									break
							else:
								thing=j
								count=1
				if won==None:
					things=[]
					for xx in range(wid):
						for yy in range(hei):
							stuff=[]
							x1=xx
							y1=yy
							runy=True
							while runy:
								if keyboard.is_pressed('ctrl'):
									runy=False
								try:
									curr=board[y1][x1]
									stuff.append(curr)
									x1-=1
									y1+=1
								except:
									runy=False
							things.append(stuff)
					for i in things:
						if len(i)<4:
							continue
						things=i[0]
						count=0
						for j in i:
							if j==thing and j!=0:
								count+=1
								if count==4:
									won=thing
									break
							else:
								thing=j
								count=1
	if won!=None:
		run=False
if won==1:
	print('Red Won!')
elif won==2:
	print('Yellow Won!')
else:
	print('DRAW')
sleep(2)