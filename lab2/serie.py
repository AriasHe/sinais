import cmath as m
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

xlista = []

def equacao_ck(T,k):
    return (-14 * (m.sin((k * m.pi) / T) * m.sin((m.pi * k) / T)) / (k**2*m.pi**2)) + ((m.sin((4 * m.pi * k) / T) + m.sin((2 * m.pi * k) / T)) / (k* m.pi))

def calcula_ck(T,n,ck0):
    ck_vetor = []
    ck_modulo = []

    nneg = -1*n 
    for k in range(nneg, n + 1):
        if k == 0:
            ck = ck0 
        else:
            ck = equacao_ck(T,k)
        ck_vetor.append(ck)
        ck_modulo.append(abs(ck))
    return ck_vetor,ck_modulo

def series (T,n,ck_veto):
    nneg = n*-1
    t_vetor = np.arange(-(T/2), (T/2), 0.001)
    xlista.clear()
    for t in t_vetor:
        x = 0 + 0j 
        j=0
        for k in range(nneg, n + 1):
            if k == 0:
                e = 1
            else:
                e = m.exp(1j * k * (2 * m.pi / T) * t)
            x = x + ck_veto[j] * e
            j=j+1
        xlista.append(x)
    return xlista,t_vetor
    
def grafico_serie(t_vetor,xlista,x_lista,n):
    grafico = f"graficos/gráfico_{n*2 +1}_harmonicas.jpg"
    
    plt.figure(figsize=(8, 5))
    plt.plot(t_vetor, x_lista, label= f"Aproximação x(t)' com {n*2 +1 } harmônicas", color='blue', linewidth=1.5)
    plt.plot(t_vetor, xlista, label='Entrada do sistema x(t)', color='orange',linewidth=2)
    plt.title('Gráfico da Série de Fourier x(t)')
    plt.xlabel('Tempo (t)')
    plt.ylabel('x(t)')
    plt.text(
        0,
        0,
        f'Potência : {potencia(x_lista,xlista,t_vetor)}',
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=12,
        bbox=dict(facecolor='yellow', alpha=0.5),  # Opcional: caixa de fundo
    )
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.savefig(grafico, dpi=300, bbox_inches='tight')
    plt.show()
        
def potencia(xarray,x_array,t_vetor):
    contagem = 0
    soma = 0
    for t in t_vetor:
        soma = (x_array[contagem]-xarray[contagem])**2 + soma
        contagem = contagem + 1
    soma = soma/len(xarray)
    soma = f"{soma.real:.2e}{soma.imag:+.2e}j"
    return (soma)