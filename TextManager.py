#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 05:57:51 2019

@author: enrico
"""

from DataType import dataType

import csv

class textManager:
    def __init__(self):
        self.beginner = "./beginner.txt"
        self.intermediate = "./intermediate.txt"
        self.expert = "./expert.txt"
    
    def getDatas(self,level):
        f=open(level, "r")
        dati = []
        i=0
        for s in f.read().splitlines():
            dt = dataType()
            for idx, value in enumerate(s.split(",")):
                if(idx==0):
                    dt.setNome(value)
                else:
                    dt.setTempo(int(value))
            dati.append(dt)
            print(dati[i].getNome() + "tempo " +str(dati[i].getTempo()))
            i = i + 1
        return dati
    
    def printDatas(self,level, nameLevel):
        f=open(level, "r")
        string =nameLevel + " \nName, Time \n"
        for s in f.read().splitlines():
            for idx, value in enumerate(s.split(",")):
                if(idx==0):
                    string = string + value + " "
                else:
                    string = string + value + "\n"
        return string
    
    def setData(self,level,nome,tempo):
        dati = self.getDatas(level)
        position = 0        
        for i in dati:
            if(tempo>i.getTempo()):
                position = position + 1
        dt =dataType()
        dt.setNome(nome)
        dt.setTempo(tempo)
        dati.insert(position, dt)
        w = open(level,'w')
        stri = ""
        for d in dati:
            stri = stri + d.getNome() + ","+ str(d.getTempo()) + "\n"
        w.write(stri)            
       