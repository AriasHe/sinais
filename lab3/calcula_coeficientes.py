""" Fun��es auxiliares para a resolu��o do exerc�cio """

""" Rotina que calcula os coeficientes do polin�mio de Chebyshev de maneira n�o-recursiva 

Par�metros: w - vetor de frequ�ncias (sugest�o: usar um vetor com amostras de 0 a 20 rad/s)
            wc - freq. de corte do filtro (em rad/s)
            n - ordem do filtro de Chebyshev
Sa�da:      Tn - vetor com os coeficientes calculados do polin�mio de Chebyshev (possui o mesmo tamanho que w)

"""
import numpy as np
import math 
import matplotlib.pyplot as plt




def resposta_frequenciua(w,wc,n,e):
    i = 0 
    Hc = []
    Habs = []
    Tn = calcula_coeficientes(w,wc,n)
    for w_ in w:
        H = 1/(math.sqrt(1 + (e**2*Tn[i]**2*(w_/wc))))
        Hc.append(H)
        Habs.append(abs(H))
        i = i + 1 
    return Habs


def calcula_coeficientes(w,wc,n):
    
    Tn = np.zeros((w.size,))
    #determina os valores dos coeficientes segundo as express�es padronizadas
    Tn[abs(w) < wc] = np.cos(n*np.arccos(w[abs(w) < wc] / wc))
    Tn[abs(w) >= wc] = np.cosh(n*np.arccosh(w[abs(w) >= wc] / wc))
    return Tn

def grafico(nT,title,xlable,ylable,w,Habs_vector):

    color = ["blue", "orange", "red","green","purple"]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_title(title)
    ax.set_xlabel(xlable)
    ax.set_ylabel(ylable)
    for i in range (0,nT,1):
        ax.plot(w, Habs_vector[i],color[i],label = str(i+1) + " harmônica")
        ax.legend()