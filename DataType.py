#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 06:50:29 2019

@author: enrico
"""

class dataType:
    def __init__(self):
        self.nome = "nome"
        self.tempo = 10000
    
    def setNome(self,nome):
        self.nome = nome
        
    def getNome(self):
        return self.nome
    
    def setTempo(self, tempo):
        self.tempo = tempo
        
    def getTempo(self):
        return self.tempo
       