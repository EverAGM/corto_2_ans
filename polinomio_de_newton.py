import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

class PolinomioDeNewton():
    
    def __init__(self):
        self.x = sp.symbols('x')  # Convertir la x en un símbolo
    
     # Calcular los coeficientes b0, b1, b2... usando diferencias divididas
    def calcular_bn(self, x_list, y_list):
        n = len(x_list)
        coef = y_list.copy()
        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                coef[i] = (coef[i] - coef[i - 1]) / (x_list[i] - x_list[i - j])
        return coef               
    
    # Calcular factores de la forma (x - x0), (x-x0)(x-x1), .... 
    def calcular_factores(self, x_list):
        factores = [1]
        
        for factor in range((len(x_list)-1)):
            factores.append(((factores[factor]) * (self.x - x_list[factor])))
    
        return factores
    
    # Creación del polinomio
    def polinomio_de_newton(self, x_list, y_list):
        bn = self.calcular_bn(x_list, y_list)
        factores = self.calcular_factores(x_list)
        polinomio = sum(bn[i] * factores[i] for i in range(len(bn)))        
        return polinomio
    
    # Interpolar el valor n en el polinomio de Newton
    def interpolacion(self, x_list, y_list):
       # Hacer el polinomio de Newton en una función lambda evaluable. 
        polinomio_lambda = sp.lambdify((self.x), self.polinomio_de_newton(x_list, y_list))
        
        new_x = [new_x_ for new_x_ in range(0, 100, 2)]
        new_y = [polinomio_lambda(xi) for xi in new_x]
        
        return new_x, new_y