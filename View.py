#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:17:40 2019

@author: enrico
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class view(object):

    def __init__(self,controller):
        self.controller = controller
        widget = QWidget() #define widget to inser the layout
        self.mainlayout = QBoxLayout(QBoxLayout.TopToBottom) #create mainlayout
        widget.setLayout(self.mainlayout) #set the layout
        controller.setCentralWidget(widget) #set to the controller the widget
        self.grid = QGridLayout() #create grid layout
        
        #horizontal layout controls
        self.horizLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.mainlayout.addLayout(self.horizLayout)
        
        #Game status and restart button
        self.vertLayout = QBoxLayout(QBoxLayout.TopToBottom)
        
        
        #grid creation
        self.boxes = controller.model.getBoxes() 
        for i in range(controller.model.getNumRows()):
            for j in range(controller.model.getNumCols()):
                self.grid.addWidget(self.boxes[i*controller.model.getNumCols()+j],i,j)
 
        #bombs label
        self.numBombsRemaining = QLabel('')
        self.numBombsRemaining.setAlignment(Qt.AlignCenter)
        self.numBombsRemaining.setStyleSheet("font: 30pt Arial")
        self.horizLayout.addWidget(self.numBombsRemaining)
        
        #roba sulla label
        self.label = QLabel('Game On')
        self.label.setAlignment(Qt.AlignCenter)
        self.vertLayout.addWidget(self.label)
        
        #restart button
        self.restartButton = QPushButton('Restart')
        self.restartButton.setFixedSize(QSize(100, 40))
        self.vertLayout.addWidget(self.restartButton)
        
        #adding to the horizontal control the vertical layout
        self.horizLayout.addLayout(self.vertLayout)

        
        #timer
        self.timelabel = QLabel('')
        self.timelabel.setStyleSheet("font: 30pt Arial")
        self.timelabel.setAlignment(Qt.AlignCenter)
        self.timelabel.move(20, 0)  
        self.horizLayout.addWidget(self.timelabel)
        self.timer= QTimer()      
        self.timer.start(1000)      
        
        

        #menu initialization
        self.menuBar = QMenuBar(controller)
        self.menuBar.setGeometry(0,0,600,40)
        self.fileMenu = self.menuBar.addMenu('&File')
        
        #easy mode configuration
        self.easyMode = QAction(controller)
        self.easyMode.setText("&Easy")
        #intermediate mode configuration
        self.intermediateMode = QAction(controller)
        self.intermediateMode.setText("&Intermediate")
        #expert mode configuration
        self.expertMode=QAction(controller)
        self.expertMode.setText("&Expert")
        #custom mode configuration
        self.customMode=QAction(controller)
        self.customMode.setText("&Custom")
        
        #Adding Actions to the menu
        self.fileMenu.addAction(self.easyMode)
        self.fileMenu.addAction(self.intermediateMode)
        self.fileMenu.addAction(self.expertMode)
        self.fileMenu.addAction(self.customMode)
        
        controller.setMenuBar(self.menuBar)    #set the menu to the controller
        self.mainlayout.addLayout(self.grid) #add to the mainlayout the grid
        
        
        #Creating the leaderboard Layout
        self.leadLayout = QBoxLayout(QBoxLayout.LeftToRight)

        #leaderboard label
        self.beginnerLeaderboard = QLabel('')
        self.leadLayout.addWidget(self.beginnerLeaderboard)
        
        #leaderboard label
        self.intermediateLeaderboard = QLabel('')
        self.leadLayout.addWidget(self.intermediateLeaderboard)
        
        #leaderboard label
        self.expertLeaderboard = QLabel('')
        self.leadLayout.addWidget(self.expertLeaderboard)

        #Adding the leaderboard to the main layout
        self.mainlayout.addLayout(self.leadLayout)

        