import math
import numpy as np
import matplotlib.pyplot as plt

""" Rotina que exibe o espectro de magnitude (X(ejw)) de um sinal discreto """
def espectro(y):

    #modulo da transf. de Fourier
    Y = np.abs(np.fft.fft(y))
    return Y

def grafico(Y,fs,c='w',titulo = 'Espectro de magnitude'):
    
    w = np.linspace(0,2*math.pi,Y.size)
    f = np.linspace(0,fs,Y.size)

    fig, ax = plt.subplots(figsize=(6, 5))

    if(c == 'w'):

        ax.plot(w, Y)
        ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
        labels = ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']

        
        ax.set_xlabel('$\Omega$ [rad]', fontsize=10)
        ax.set_ylabel('|$Y(e^{j\Omega})$|', fontsize=10)
        ax.set_xticks(ticks)
        ax.set_xticklabels(labels, fontsize=10)
    ax.set_title(titulo,fontsize = 10)    
    ax.tick_params(axis='both', which='both', width=1, color='red')
    ax.grid(True, linestyle='-.', linewidth=0.5, color='gray')

    return ax,fig 

def decimacao(Y,M):
    ydec = []

    for n in range(int(Y.size/M)):
        ydec.append(Y[M*n])
    return ydec

def kaiser(wp,wr):

    wc = (wp + wr)/2
    d = 0.01
    Ap = 20*math.log10((1+d)/(1-d))
    Ar = -20*math.log10(d)


    if Ar < 21:
        b = 0
        D = .9222
    elif Ar < 50:
        b = 0.5842*(Ar-21)**0.4+0.07886*(Ar-21)
        D = (Ar - 7.95)/14.36
    else:
        b = .1102*(Ar-8.7)
        D = (Ar - 7.95)/14.36

    k = math.ceil(math.pi*D/(wr-wp)-.5)
    M = 2*k+1
    n = np.arange(-k,k+1,1)
    
    w = np.i0(b*np.sqrt(1-(4/M**2)*n**2))
    w = np.divide(w,np.i0(b))

    h = wc/math.pi*np.sinc(wc*n/math.pi)*w

    return h
    