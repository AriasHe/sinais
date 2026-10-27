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
        H = 1/(math.sqrt(1 + (e**2*Tn[i]**2*(abs(w_)/wc))))
        Hc.append(H)
        Habs.append(abs(H))
        i = i + 1 
    return Habs

def resposta_frequenciua_Butterworth(w,wc,n):
    i = 0 
    Hc = []
    Habs = []
    for w_ in w:
        H = 1/(math.sqrt(1 + ((w_/wc)**(2*n))))
        Hc.append(H)
        Habs.append(abs(H))
    return Habs

def calcula_coeficientes(w,wc,n):
    
    Tn = np.zeros((w.size,))
    #determina os valores dos coeficientes segundo as express�es padronizadas
    Tn[abs(w) < wc] = np.cos(n*np.arccos(abs(w[abs(w) < wc] / wc)))
    Tn[abs(w) >= wc] = np.cosh(n*np.arccosh(abs(w[abs(w) >= wc] / wc)))
    return Tn

def grafico(w,Habs_vector,title = "titulo",xlable = 'x',ylable = 'y',texto = "",arredondamento = 0):
    nT = len(Habs_vector)
    color = ["blue", "orange", "red","green","purple"]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_title(title)
    ax.set_xlabel(xlable)
    ax.set_ylabel(ylable)
    for i in range(nT):
        ax.plot(w, Habs_vector[nT-i-1],color[i],label =  texto + str(f"{i:.{arredondamento}f}"))

    ax.legend()