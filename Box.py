#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 08:41:50 2019

@author: enrico
"""
import sys
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class box(QPushButton):
    #box signals
    bomb = pyqtSignal(object,object) 
    emptybox = pyqtSignal(object,object)
    flaggeds = pyqtSignal()
    unflaggeds = pyqtSignal()
    revealeds = pyqtSignal()
    
    def __init__(self,id,rowIndex,colIndex,num):
        QPushButton.__init__(self,"")
        QPushButton.setFixedSize(self,QSize(40, 40))
        self.id = id
        self.flagged = -1
        self.rowIndex = rowIndex
        self.colIndex = colIndex
        self.revealed = False
        self.number = num
                
    #set the box number
    def setNumber(self,n):
        self.number = n
    
    #get the box number
    def getNumber(self):
        return self.number
    
    #my left click function
    def myclick(self):
        if(self.revealed==False):
            self.revealed = True
            if (self.number<0):
                self.setText("*")
                self.bomb.emit(self.rowIndex, self.colIndex)
            else:
                if(self.number>0):
                    self.setText(str(self.number))
                    self.revealeds.emit()
                else:
                    self.setStyleSheet("background-color: grey")
                    self.emptybox.emit(self.rowIndex, self.colIndex)
                    self.revealeds.emit()
    
    #function to reveal all boxes 
    def revealAllClick(self):
        if(self.revealed==False):
            self.revealed = True
            if (self.number<0):
                self.setText("*")
            else:
                if(self.number>0):
                    self.setText(str(self.number))
                    #self.revealeds.emit()
                else:
                    self.setStyleSheet("background-color: grey")
                    #self.emptybox.emit(self.rowIndex, self.colIndex)
                    #self.revealeds.emit()

    #my right click function
    def myrightclick(self):
        if(self.revealed == False):
            if(self.flagged<0):
                self.flagged = 1 
                self.setText("!")
                self.flaggeds.emit()
            else:
                self.flagged = -1
                self.setText("")
                self.unflaggeds.emit()        
    
    #click event management
    def mouseReleaseEvent(self,event):
        if(event.button() == Qt.RightButton):
            self.myrightclick()
        elif(event.button()==Qt.LeftButton):
            self.myclick()
            
    def getRevealed(self):
        return self.revealed