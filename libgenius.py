# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:13:43 2015

@author: tbeigbeder
"""
from __future__ import division
from scipy import *


#Fonction potentiel de morse
def morse(Req,De,beta,R):
    V=De*(1-exp(-beta*(R-Req)))**2
    return V
    
#plot(arange(1,6,0.2),morse(.256,232,25,linspace(0,10,400)),label="Graph")

def printArray(array):
    print("\n")
    for i in array:
        print(i,"\n")

def testspectre(l):
    s=0
    c=3.0*10**8
    h=6.62*10**(-34)
    unite=""
    if (10<l<390):
        s=1/(l*10**(-7))
        unite="cm-1"
    elif (390<l<750):
        s=l
        unite="nm"
    elif(750<l<100000):
        s=(h*c)/(l*10**-9)
        unite="eV"

    return s,unite

def degtorad(alpha):
    alpharad=alpha*(pi/180)
    return alpharad

def importcolumn(file,column):
    n=0
    tab=[]
    for line in file:
        mot=line.split()
        print(type(mot[column]))        
        if (mot != []) or (type(mot[column]) != type("")):
           x=float(mot[column])
           print()
        tab.insert(n,x)
        n=n+1
    return tab
    
def nbreColFile(file):
    for line in file:
            nbrecol=len(line.split())
    return nbrecol

def importFileTab(file):
    tab=[]
    for c in range(nbreColFile(open(file, 'r'))):
        f=open(file, 'r')
        f.readline()
        tab.insert(c,importcolumn(f,c))
    return tab

def sommetab(tab):
    s=0
    for i in tab:
        s=s+i
    return s

def sommecarres(tab):
    s=0
    for i in tab:
        s=s+(i)**2
    return s

def sommeProduitstab(tab1,tab2):
    somme=0
    for i in tab1:
        for j in tab2:
            somme=somme+i*j
    return somme


def moyennetab(tab):
    s=0
    for i in tab:
        s=s+i
    moy=s/len(tab)
    return moy
        