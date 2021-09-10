#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:03:59 2021

@author: macbookair2013
"""

import numpy as np
from scipy.linalg import solve

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
    
    def agregar_nodo(self, x, y, z=0):
	

        print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos
        if self.Nnodos+1 > Reticulado.__NNodosInit__:
    		self.xyz.resize((self.Nnodos+1,3))
    		self.xyz[self.Nnodos,:] = [x, y, z]
    		self.Nnodos += 1
    		if z != 0.:
    			self.Ndimensiones = 3
    
    def agregar_barra(self, barra):
        
        self.barras.append(barra)        
        
        return 0

    def obtener_coordenada_nodal(self, n):
        
        if n >= self.Nnodos:
			return 
		return self.xyz[n, :]	
        
        return 0

    def calcular_peso_total(self):
        
        peso = 0.
		for b in self.barras:
			peso += b.calcular_peso(self)
		return peso	
        
        return 0

    def obtener_nodos(self):
        
        return self.xyz

    def obtener_barras(self):
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        
        """Implementar"""	
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        """Implementar"""	
        
        return 0


    def ensamblar_sistema(self):
        
        """Implementar"""	
        
        return 0



    def resolver_sistema(self):
        
        """Implementar"""	
        
        return 0

    def obtener_desplazamiento_nodal(self, n):
        
        """Implementar"""	
        
        return 0


    def obtener_fuerzas(self):
        
        """Implementar"""	
        
        return 0


    def obtener_factores_de_utilizacion(self, f):
        
        """Implementar"""	
        
        return 0

    def rediseñar(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0







    def __str__(self):

        s = "Soy un reticulado :)"

        s += "\n"
        
        s += str(self.xyz[0 : self.Nnodos,:])
        def __str__(self):
		s = "nodos:\n"
		for n in range(self.Nnodos):
			s += f"  {n} : ( {self.xyz[n,0]}, {self.xyz[n,1]}, {self.xyz[n,2]}) \n "
		s += "\n\n"

		s += "barras:\n"
		for i, b in enumerate(self.barras):
			n = b.obtener_conectividad()
			s += f" {i} : [ {n[0]} {n[1]} ] \n"
		s += "\n\n"
        return s
