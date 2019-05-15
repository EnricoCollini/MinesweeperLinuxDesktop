#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:25:37 2019

@author: enrico
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

from View import view
from Model import model



class Controllore(QMainWindow):
        
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.init(9,9,20)
    
    def init(self,r,c,b):
        self.model = model(r,c,b)
        self.view = view(self)
        self.view.numBombsRemaining.setText(str(self.model.getBombsRemaining()))
        self.view.restartButton.clicked.connect(self.restart)
        self.view.timer.timeout.connect(self.every_second)        
        
        #print the actual value
        self.view.beginnerLeaderboard.setText(self.model.getManager().printDatas(self.model.getManager().beginner,"Beginner"))
        self.view.intermediateLeaderboard.setText(self.model.getManager().printDatas(self.model.getManager().intermediate,"Intermediate"))
        self.view.expertLeaderboard.setText(self.model.getManager().printDatas(self.model.getManager().expert,"Expert"))
        
        
        #connecting the signals for the game rules
        for i in range(self.model.getNumRows() * self.model.getNumCols()):
            self.model.getIBox(i).bomb.connect(self.model.bombClicked)
            self.model.getIBox(i).bomb.connect(self.endgame)
            self.model.getIBox(i).flaggeds.connect(self.model.flagF)
            self.model.getIBox(i).flaggeds.connect(self.updateBombsLabel)
            self.model.getIBox(i).unflaggeds.connect(self.model.unflagF)
            self.model.getIBox(i).unflaggeds.connect(self.updateBombsLabel)
            self.model.getIBox(i).flaggeds.connect(self.updateBombsLabel)
            self.model.getIBox(i).revealeds.connect(self.model.revealF)
            self.model.getIBox(i).emptybox.connect(self.model.emptyNeighbors)
                
        #connecting the signals for the menu actions
        self.view.easyMode.triggered.connect(self.easy)
        self.view.intermediateMode.triggered.connect(self.intermediate)
        self.view.expertMode.triggered.connect(self.expert)
        self.view.customMode.triggered.connect(self.showDialog)
        self.model.customsignal.connect(self.custom)
        
        #connecting the win game signal
        self.model.winsignal.connect(self.win)      
    
    #end game label management
    def endgame(self):
        self.view.label.setText("Game Over")
        self.view.timer.stop()
    
    #to stop the timer view
    def win(self):
        self.view.timer.stop()
        self.view.label.setText("You Win!")
        text, okPressed = QInputDialog.getText(self, "Get text","Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.model.manageWin(text)
        
        
    #to update the bombs count label
    def updateBombsLabel(self):
        self.view.numBombsRemaining.setText(str(self.model.getBombsRemaining()))
    
    #when restarting the game
    def restart(self):
        self.init(self.model.getNumRows(),self.model.getNumCols(),self.model.getNumBombs())
        self.model.restartTime()
        self.view.timer.start(1000)
        
    #easy mode initialization
    def easy(self):
        self.init(self.model.easy[0],self.model.easy[1],self.model.easy[2])
        self.model.setGameMode("Easy")
    
    #intermediate mode initialization
    def intermediate(self):
        self.init(self.model.intermediate[0],self.model.intermediate[1],self.model.intermediate[2])
        self.model.setGameMode("Intermediate")
    
    #expert mode initialization
    def expert(self):
        self.init(self.model.expert[0],self.model.expert[1],self.model.expert[2])
        self.model.setGameMode("Expert")
        
    #custom mode initialization
    def custom(self):
        self.init(self.model.custom[0],self.model.custom[1],self.model.custom[2])
    
    def every_second(self):
        self.model.increaseTime()
        self.view.timelabel.setText(str(self.model.getTime()))
        
        
    #show dialog 
    def showDialog(self):
        self.getInteger()
    #managing the value input from the dialog    
    def getInteger(self):
        a, okPresseda = QInputDialog.getInt(self, "Rows number","Rows Num:", 7, 0, 100, 1)
        b, okPressedb = QInputDialog.getInt(self, "Cols number","Cols Num:", 7, 0, 100, 1)
        c, okPressedc = QInputDialog.getInt(self, "Bomb number","Bomb Num:", 40, 0, 100, 1)
        if okPresseda:
            if(a>0):
                if okPressedb:
                    if(b>0):
                        if okPressedc:
                            if(c>0 and c<a*b):
                                self.model.customF(a,b,c)
                            else:
                                c = a*b
                                self.model.customF(a,b,c)
    

                
        
    
        
        

        
        
            
        
        
        
        