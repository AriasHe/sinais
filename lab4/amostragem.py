import math
import numpy as np
import matplotlib.pyplot as plt

""" Rotina que exibe o espectro de magnitude (X(ejw)) de um sinal discreto """
def espectro(y,fs):

    #modulo da transf. de Fourier
    Y = np.abs(np.fft.fft(y))
    #frequencias avaliadas
    
    w = np.linspace(0,2*math.pi,Y.size)
    f = np.linspace(0,fs,Y.size)

    #exibe o grafico do espectro
    """
    plt.figure() 
    #plt.plot(w,Y)
    plt.plot(f,Y)
    plt.xlabel('$\Omega$ [rad]', fontsize=10)
    plt.ylabel('|$Y(e^{j\Omega})$|', fontsize=10)
    plt.grid(True)
    plt.xlim((0,fs))
    plt.show()
    """

    fig, ax = plt.subplots()
    ax.plot(w, Y)

    ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    labels = ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']

    ax.set_title('Espectro de magnitude',fontsize = 10)
    ax.set_xlabel('$\Omega$ [rad]', fontsize=10)
    ax.set_ylabel('|$Y(e^{j\Omega})$|', fontsize=10)

    
    ax.set_xticks(ticks)
    ax.set_xticklabels(labels, fontsize=10)
    
    ax.tick_params(axis='both', which='both', width=1, color='red')
    ax.grid(True, linestyle='-.', linewidth=0.5, color='gray')

    
    plt.show()
    return Y,f  

def decimacao(Y,M):
    ydec = []
    for n in range(int(Y.size/M)):
        ydec.append(Y[M*n])
    return ydec