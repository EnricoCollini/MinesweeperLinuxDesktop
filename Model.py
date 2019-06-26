#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:22:08 2019

@author: enrico
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Box import box
import random

from TextManager import textManager


class model(QObject):
    #model signals
    customsignal = pyqtSignal(object,object,object)
    winsignal = pyqtSignal()
    
    def __init__(self,r=9, c=9, b=10):
        super(QObject,self).__init__(parent=None)
        self.init(r,c,b)
        self.easy = [9,9,10]
        self.intermediate = [10,10,40]
        self.expert = [16,18,99]
        self.custom =[1,1,1]
        self.time = 0
        self.gameMode = "custom"
    
    def init(self, r, c, b):
        self.stringa = "ciao"
        self.numRows= r
        self.numCols = c
        self.maxNumBombs = b
        self.bombs = self.maxNumBombs
        self.bombsRemaining = self.maxNumBombs
        self.boxesRevealed =0
        self.boxes= []
        self.createBoxes() 
        #creating a manager
        self.manager = textManager()

    #getting the manager 
    def getManager(self):
        return self.manager

    def getGameMode(self):
        return self.gameMode
    
    def setGameMode(self, mode):
        self.gameMode = mode
    
    def manageWin(self,nome):
        if(self.gameMode=="custom"):
            print("customMode")
            #level = self.manager.beginner
            #self.manager.setData(level,nome,self.time)
        elif(self.gameMode == "Intermediate"):
            level = self.manager.intermediate
            self.manager.setData(level,nome,self.time)
        elif(self.gameMode == "Expert"):
            level = self.manager.expert
            self.manager.setData(level,nome,self.time)
        else:
            print("easyMode")
            level = self.manager.beginner
            self.manager.setData(level,nome,self.time)
            

    #custom clicked
    def customF(self,r,c,b):
        self.custom=[r,c,b]
        self.customsignal.emit(r,c,b)
    
    #function to increase the time count
    def increaseTime(self):
        self.time = self.time +1
    
    #when restarting a game to init the time count
    def restartTime(self):
        self.time = 0
    
    #get time
    def getTime(self):
        return self.time
    
    #get bombs remaining
    def getBombsRemaining(self):
        return self.bombsRemaining
        
    #when a box is flagged 
    def flagF(self):
        self.bombsRemaining = self.bombsRemaining -1
            
    #when a box is unflagged
    def unflagF(self):
        self.bombsRemaining = self.bombsRemaining + 1
    
    #when a box is revealed
    def revealF(self):
        self.boxesRevealed = self.boxesRevealed + 1
        if(self.boxesRevealed == (self.numRows*self.numCols) - self.maxNumBombs):
            self.winsignal.emit()
            for i in range(self.numRows):
                for j in range(self.numCols):
                    self.boxes[i*self.numCols + j].revealAllClick()
            
    #set the number of rows
    def setNumRows(self,num):
        self.numRows = num
    
    def getNumBombs(self):
        return self.maxNumBombs
    
    #get the number of rows
    def getNumRows(self):
        return self.numRows
    
    #set the number of columns
    def setNumCols(self,num):
        self.numCols = num
        
    #get the number of columns
    def getNumCols(self):
        return self.numCols
    
    #method for creating the boxes
    def createBoxes(self):
        self.createBombs()
        self.assignNumbs()
                        
    #assign randomly bombs in the grid
    def createBombs(self):
        while(self.bombs>=1):
            for i in range(self.numRows):
                for j in range(self.numCols):
                    if(self.bombs>=1 and random.randint(0, self.numCols*self.numRows)<self.maxNumBombs):
                        self.boxes.append(box(i*self.numCols + j,i,j,-1))
                        self.bombs = self.bombs -1
                    else:
                        self.boxes.append(box(i*self.numCols + j,i,j,0))
            if(self.bombs>0):
                self.bombs = self.maxNumBombs
                #del self.boxes[:]
            else:
                self.bombs = -1
    
    #calculate the number of bombs near a box that is not a bomb
    def assignNumbs(self):
        for i in range(self.numRows):
            for j in range(self.numCols):
                if(self.boxes[i*self.numCols + j].getNumber()==-1):
                    print("log")
                else:
                    count = 0
                    for xoff in range(-1,2):
                        for yoff in range(-1,2):
                            k = i + xoff
                            l = j + yoff
                            if(k>-1 and l>-1 and k<self.numRows and l <self.numCols):
                                if(self.boxes[k*self.numCols + l].getNumber() ==-1):
                                    count = count +1
                                    self.boxes[i*self.numCols + j].setNumber(count)
     
    #easyMode configuration
    def setEasyMode(self):
        self.boxes= []
        self.numRows= 11
        self.numCols = 11
        self.maxNumBombs = 2
        self.bombs = self.maxNumBombs
        self.rateBombGenerator = (self.numCols * self.numCols)/self.bombs
        self.createBoxes()
        
    #get boxes    
    def getBoxes(self):
        return self.boxes
    
    #get the i-th box
    def getIBox(self,i):
        return self.boxes[i]
    
    #bomb clicked
    def bombClicked(self,r,c):
        for i in range(len(self.boxes)):
            if(self.boxes[i].getRevealed()==False):
                self.boxes[i].revealAllClick()
    
    #function to show the neighbors cells with 0 bombs in the near by
    def emptyNeighbors(self,i,j):
        self.functiontocall(i,j)
    #function to call recursiveli to obtain the above function
    def functiontocall(self,i,j):
        for xoff in range(-1,2):
            for yoff in range(-1,2):
                if(xoff == 0 and yoff == 0):
                    print("log1")
                else:
                    k = i + xoff
                    l = j + yoff
                    if(k>-1 and l>-1 and k<self.numRows and l <self.numCols):
                        if(self.boxes[k*self.numCols + l].getNumber()>=0 and self.boxes[k*self.numCols + l].getRevealed()==False):
                            self.boxes[k*self.numCols + l].myclick()
                                    
    #getStringa
    def getstringa(self):
        return self.stringa    