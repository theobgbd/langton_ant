# -*- coding: utf-8 -*-
"""
Fourmi de Langton à elements multiples
@author: theogenius
"""
#=============================================================
# Import des bibliotheques
#=============================================================
from __future__ import (division, unicode_literals)
from scipy import *
#from pylab import *
from libgenius import *
import random
import os
#from PIL.Image import *
import PIL.Image as imagelib

#Définition des constantes
grid_size=200
CI=[int(floor(grid_size/2)),int(floor(grid_size/2))]
Vect=[0,1]
etapes=5000
path='/tmp/fourmi/imageTemp'

grid = [[0 for x in range(grid_size)] for x in range(grid_size)]
os.system('rm /tmp/fourmi/imageTemp*.png') # destruction des fichiers temporaires (utiliser rem sous Linux)
os.system('mkdir /tmp/fourmi')
os.system('mkdir /tmp/fourmi/full')

#=============================================================
# Définition des classes
#=============================================================

### Classe de la fourmi ###
class Fourmi:
    def __init__(self,CI,Vect): # Notre méthode constructeur
        self.position = CI
        self.vecteur=Vect

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
    
    def black(self):
        self.newgrid=[[0 for x in range(len(self.grid[0]))] for x in range(len(self.grid[0]))]
        for i in range(1,len(self.newgrid[0])-2):
            for j in range(1,len(self.newgrid[0])-2):
                self.newgrid[i][j]=1
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
    image=imagelib.new("RGB",(len(grid.grid[0]),len(grid.grid[1])))
    for n in range(len(grid.grid)):
        for p in range(len(grid.grid[0])):
            #print(n,p,len(grid.grid))
            if grid.grid[n][p]==0:
                imagelib.Image.putpixel(image,(n,p),(255,255,255))
            elif grid.grid[n][p]==1:
                imagelib.Image.putpixel(image,(n,p),(0,0,0))
    #print(image.size,fourmi.position)
    #imagelib.Image.putpixel(image,(fourmi.position[0],fourmi.position[1]),(255,0,0))
    #Image.putpixel(image,(fourmi.position[0],fourmi.position[1]),(255,0,0))
    return image

def placerFourmi(image,fourmi):
    imagelib.Image.putpixel(image,(fourmi.position[0],fourmi.position[1]),(255,0,0))
    return image

#=============================================================
# Test du code
#=============================================================
 
#print(fourmi.position)
grille=Grid(grid_size)
#grille.black()
#ant=Fourmi(CI)

#fourmitest=Fourmi(CI)
n=0

def simulation(etapes,tableau_fourmis,grille):
    for i in range(etapes):
        if i==0:
            for fourmi in tableau_fourmis:
                image=gridToImage(grille,fourmi)
                image_finale=placerFourmi(image,fourmi)            
            filename = path+str('%05d' %i)+'.png'            
            imagelib.Image.save(image_finale,filename)
            
        print("\n \nEtape:",i)
        print("Grille: ",len(grille.grid),len(grille.grid[0]))
        n=0
        for fourmi in tableau_fourmis:
            print("\n--Fourmi N°: ",n%len(tableau_fourmis)+1," --")
            [pas,grille]=mvtFourmi(fourmi,grille)
            n=n+1
        image=gridToImage(grille,fourmi)
        for fourmi in tableau_fourmis:
            image_finale=placerFourmi(image,fourmi)            
        filename = path+str('%05d' %i)+'.png' 
        imagelib.Image.save(image_finale,filename)
        command_convert='convert -scale 1000% ' + filename +  '\t' +filename
        os.system(command_convert)    
#=============================================================
# Entrées
#=============================================================
infile=open("./input_fourmi",'r')
fourmi_tab=[]
#new_fourmi=Fourmi(CI)
l=0
for line in infile:
    elems=line.split()
    x=int(elems[0])
    y=int(elems[1])    
    vect=elems[2]
    if vect=="up":
        vect_x=[0,1]
    elif vect=="down":
            vect_x=[0,-1]
    elif vect=="left":
            vect_x=[-1,0]
    elif vect=="right":
            vect_x=[1,0]
    fourmi_tab.insert(l,Fourmi([x,y],vect_x))
    #print(new_fourmi.position)
    #print(new_fourmi.vecteur)
    #print(fourmi_tab[0].position,"\n")
    print(x,y,vect)
    l=l+1
    
    
#=============================================================
# Processing
#=============================================================
grille=Grid(grid_size)

for i in fourmi_tab:
    print (i.position,i.vecteur)

simulation(etapes,fourmi_tab,grille)


#for i in range(etapes):
#        print("\n--- Frame",i,"---\n")
#        #printArray(grille.grid)
#        #print(pas[0])
#        #printArray(grille.grid)
#        
#        image=gridToImage(grille,fourmitest)
#        filename_image = '/tmp/fourmi/imageTemp'+str('%05d' %n)+'.png'
#        print(filename_image)
#        Image.save(image,filename_image)
#        command='convert -scale 1000% ' + filename_image +  '\t' +filename_image
#        os.system(command)
#
#        
#        #filename = '/tmp/fourmi/tab/tab-temp'+str('%05d' %n)+'.csv'
#        #os.system(str('touch '+filename))
#        #file=file_open(filename,'r')
#        #file.write(str(grille.grid))
#  
#        [pas,grille]=mvtFourmi(fourmitest,grille)
#        n=n+1
        
print("\nConversion...")
#os.system('convert -scale 1000% /tmp/fourmi/imageTemp%05d.png /tmp/fourmi/image*.png ')
os.system('ffmpeg  -i /tmp/fourmi/imageTemp%05d.png -r 24 -vcodec mpeg4 -b 15000k /tmp/fourmi/Fourmi.mp4')
print("Conversion terminée.")
#os.system('convert -delay 2 -loop 0 /tmp/fourmi/imageTemp*.png Fourmi.gif')


print("Done")
#printArray(pas[1])
#printArray(grille.grid)
#NP.insert(grille.grid,0,[0 for x in range(len(grille.grid[0]))],axis=1)
#grille.addRowDown()
#grille.addRowDown()

#printArray(grille.grid)
#print(fourmi.position)
