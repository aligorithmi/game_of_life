import os,random

def set_init_cell_position():
 for c in range(0,init_cell_number):
  x,y=(random.randint(0,grid_rows-1),random.randint(0,grid_cols-1))  
  grid[x][y]=True

def display_grid():
 global generation_counter
 print 'Generation counter:',generation_counter
 print
 for r in range(0,grid_rows):
    for c in range(0,grid_cols):
        if grid[r][c]:
         print 'o',
        else:
         print '.',
    print

def get_neighbours(r,c):
 for row in r-1,r,r+1:
  if row in range(0,grid_rows):
   for col in c-1,c,c+1:
    if col in range(0,grid_cols) and not (col==c and row==r):
      neighbours.append(grid[row][col])
 evolution(r,c,neighbours)

def evolution(x,y,neighbours):
 neighbour_counter=0
 for i in range(0,len(neighbours)):
  if neighbours[i]:
   neighbour_counter+=1
 if grid[x][y] and (neighbour_counter<2 or neighbour_counter>3):
  grid[x][y]=False  
 elif not grid[x][y] and neighbour_counter==3:
  grid[x][y]=True
  
grid_rows=20
grid_cols=20
grid=[[False] * grid_cols for r in range(0,grid_rows)]

init_cell_number=int(raw_input('Enter initial random cell number: '))
set_init_cell_position()
generation_counter=0

while True:
 generation_counter+=1
 for i in range(0,grid_rows):
  for j in range(0,grid_cols):
   neighbours=[]
   get_neighbours(i,j)
 os.system('clear')
 display_grid()    