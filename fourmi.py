# -*- coding: utf-8 -*-
"""
Fourmi de Langton
@author: genius
"""
from __future__ import (division, unicode_literals)
from scipy import *
#from pylab import *
from libgenius import *
import random
from PIL.Image import *

#Définition des constantes
grid_size=75
CI=[int(floor(grid_size/2)),int(floor(grid_size/2))]

grid = [[0 for x in range(grid_size)] for x in range(grid_size)]
os.system('rm /tmp/fourmi/imageTemp*.png') # destruction des fichiers temporaires (utiliser rem sous Linux)
os.system('mkdir /tmp/fourmi')
os.system('mkdir /tmp/fourmi/tab')

#=============================================================
#Définition des classes
#=============================================================

### Classe de la fourmi ###
class Fourmi:
    def __init__(self,CI): # Notre méthode constructeur
        self.position = CI
        self.vecteur=[0,1]

    def turnRight(self):    
        up=[0,1]
        down=[0,-1]
        right=[1,0]
        left=[-1,0]
        if self.vecteur==up:
            self.position[0]=self.position[0]+1
            self.vecteur=right    
            print("up")
        elif self.vecteur==down:
            self.position[0]=self.position[0]-1
            self.vecteur=left
            print("down")
        elif self.vecteur==right:
            self.position[1]=self.position[1]+1
            self.vecteur=down
            print("right")
        elif self.vecteur==left:
            self.position[1]=self.position[1]-1
            self.vecteur=up
            print("left")
        
    def turnLeft(self):    
        up=[0,1]
        down=[0,-1]
        right=[1,0]
        left=[-1,0]
        if self.vecteur==up:
            self.position[0]=self.position[0]-1
            self.vecteur=left    
            print("up")
        elif self.vecteur==down:
            self.position[0]=self.position[0]+1
            self.vecteur=right
            print("down")
        elif self.vecteur==right:
            self.position[1]=self.position[1]-1
            self.vecteur=up
            print("right")
        elif self.vecteur==left:
            self.position[1]=self.position[1]+1
            self.vecteur=down
            print("left")

### Classe de la grille ###
class Grid:
    def __init__(self,size):
        self.grid=[[0 for x in range(size)] for x in range(size)]
   
   #Méthodes d'agrandissement    
    def addRowUp(self):
        self.newgrid=[[0 for x in range(len(self.grid[0]))] for x in range(len(self.grid[0])+1)]
        #printArray(newgrid)
        #Copie de la grille
        for i in range(1,len(self.newgrid[0])-1):
            for j in range(len(self.newgrid[0])-1):
                self.newgrid[i][j]=self.grid[i][j]
        self.grid=self.newgrid
        return self.grid
    
    def addRowDown(self):
        self.newgrid=[[0 for x in range(len(self.grid[0]))] for x in range(len(self.grid[0])+1)]
        #Copie de la grille
        for i in range(len(self.newgrid[0])-1):
            for j in range(len(self.newgrid[0])-1):
                self.newgrid[i][j]=self.grid[i][j]
        self.grid=self.newgrid
        return self.grid
    
    def addRowLeft(self):
        self.newgrid=[[0 for x in range(len(self.grid[0])+1)] for x in range(len(self.grid[0]))]
        #Copie de la grille
        for i in range(1,len(self.newgrid[0])-2):
            for j in range(1,len(self.newgrid[0])-2):
                self.newgrid[i][j]=self.grid[i][j]
        self.grid=self.newgrid
        return self.grid

    
    def addRowRight(self):
        self.newgrid=[[0 for x in range(len(self.grid[0])+1)] for x in range(len(self.grid[0]))]
        #Copie de la grille
        for i in range(1,len(self.newgrid[0])-2):
            for j in range(1,len(self.newgrid[0])-2):
                self.newgrid[i][j]=self.grid[i+1][j]
        self.grid=self.newgrid
        return self.grid 
        
#=============================================================
#Fonctions utiles
#=============================================================

### Mouvement élémentaire de la fourmi ###
def mvtFourmi(fourmi,grid):
    x=fourmi.position[0]
    y=fourmi.position[1]
    print('[',x,y,']',":",grid.grid[x][y])      
    #On fait avancer la fourmi  
    if (grid.grid[x][y]==0):
       fourmi.turnRight()
       grid.grid[x][y]=1
       print('Right-->',grid.grid[x][y])
    elif (grid.grid[x][y]==1):
        fourmi.turnLeft()
        grid.grid[x][y]=0
        print('Left-->',grid.grid[x][y])
        #print(grid.grid[x][y])
    #On agrandit la grille si nécéssaire
    #cas où x dépasse
    if (fourmi.position[0] < 0):
        grid.addRowLeft()
    elif (fourmi.position[0] > len(grid.grid[0])):
        grid.addRowRight()
    if (fourmi.position[1] < 0):
        grid.addRowUp()
    elif (fourmi.position[1] > len(grid.grid[1])):
        grid.addRowDown()
    return [fourmi.position,grid]

### Génération de la grille ###
def genGrid(grid,n_color):
    n=0    
    for i in grid:        
        p=0
        for j in i:
            grid[n][p]=random.randint(0,n_color)  
            p=p+1
        n=n+1
    return grid

#Traduction en image
def gridToImage(grid,fourmi):
    image=new("RGB",(len(grid.grid[0]),len(grid.grid[1])))
    for n in range(len(grid.grid)):
        for p in range(len(grid.grid[0])):
            #print(n,p,len(grid.grid))
            if grid.grid[n][p]==0:
                Image.putpixel(image,(n,p),(255,255,255))
            elif grid.grid[n][p]==1:
                Image.putpixel(image,(n,p),(0,0,0))
    #print(image.size,fourmi.position)
    Image.putpixel(image,(fourmi.position[0],fourmi.position[1]),(255,0,0))
    #Image.putpixel(image,(fourmi.position[0],fourmi.position[1]),(255,0,0))
    return image
    

#=============================================================
# Test du code
#=============================================================
 
#print(fourmi.position)
grille=Grid(grid_size)
#ant=Fourmi(CI)

fourmitest=Fourmi(CI)
n=0
def simulation(etapes):
    for i in range(etapes):
        print(i)
        image=gridToImage(grille,fourmitest)
        filename = '/tmp/fourmi/imageTemp'+str('%000002d' %n)+'.png'
        Image.save(image,filename)
        [pas,grille]=mvtFourmi(fourmitest,grille)
        n=n+1

for i in range(11000):
        print(i)
        print(grille.grid,"\n")
        #print(pas[0])
        #printArray(grille.grid)
        
        image=gridToImage(grille,fourmitest)
        filename_image = '/tmp/fourmi/imageTemp'+str('%05d' %n)+'.png'
        Image.save(image,filename_image)
        
        #filename = '/tmp/fourmi/tab/tab-temp'+str('%05d' %n)+'.csv'
        #os.system(str('touch '+filename))
        #file=file_open(filename,'r')
        #file.write(str(grille.grid))
  
        [pas,grille]=mvtFourmi(fourmitest,grille)
        n=n+1

os.system('convert -delay 5 -loop 0 /tmp/fourmi/imageTemp*.png Fourmi.gif')
os.system('convert -delay 2 -loop 0 /tmp/fourmi/imageTemp*.png Fourmi.gif')

print("Done")
#printArray(pas[1])
#printArray(grille.grid)
#NP.insert(grille.grid,0,[0 for x in range(len(grille.grid[0]))],axis=1)
#grille.addRowDown()
#grille.addRowDown()

#printArray(grille.grid)
#print(fourmi.position)





