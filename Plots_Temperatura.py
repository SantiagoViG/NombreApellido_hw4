import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


X=np.loadtxt('X.txt')
Y=np.loadtxt('Y.txt')
Tc1a0=np.loadtxt('Tc1a0.txt')
Tc1a100=np.loadtxt('Tc1a100.txt')
Tc1a2500=np.loadtxt('Tc1a2500.txt')

Tc1f0=np.loadtxt('Tc1f0.txt')
Tc1f100=np.loadtxt('Tc1f100.txt')
Tc1f2500=np.loadtxt('Tc1f2500.txt')

Tc1p0=np.loadtxt('Tc1p0.txt')
Tc1p100=np.loadtxt('Tc1p100.txt')
Tc1p2500=np.loadtxt('Tc1p2500.txt')

Tc2a0=np.loadtxt('Tc2a0.txt')
Tc2a100=np.loadtxt('Tc2a100.txt')
Tc2a2500=np.loadtxt('Tc2a2500.txt')

Tc2f0=np.loadtxt('Tc2f0.txt')
Tc2f100=np.loadtxt('Tc2f100.txt')
Tc2f2500=np.loadtxt('Tc2f2500.txt')

Tc2p0=np.loadtxt('Tc2p0.txt')
Tc2p100=np.loadtxt('Tc2p100.txt')
Tc2p2500=np.loadtxt('Tc2p2500.txt')

def grafica(T, titulo):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, T)
    ax.set_xlim(0, 100)
    ax.set_ylim(0,100)
    #ax.set_zlim(40, 150)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title(titulo)
    fig.savefig(titulo)

grafica(Tc1a0,"Caso1 Condiciones abiertas 0s")
grafica(Tc1a100,"Caso1 Condiciones abiertas 100s")
grafica(Tc1a2500,"Caso1 Condiciones abiertas 2500s")

grafica(Tc1a0,"Caso1 Condiciones fijas 0s")
grafica(Tc1a100,"Caso1 Condiciones fijas 100s")
grafica(Tc1a2500,"Caso1 Condiciones fijas 2500s")

grafica(Tc1p0,"Caso1 Condiciones periodicas 0s")
grafica(Tc1p100,"Caso1 Condiciones periodicas 100s")
grafica(Tc1p2500,"Caso1 Condiciones periodicas 2500s")

grafica(Tc2a0,"Caso2 Condiciones abiertas 0s")
grafica(Tc2a100,"Caso2 Condiciones abiertas 100s")
grafica(Tc2a2500,"Caso2 Condiciones abiertas 2500s")

grafica(Tc2a0,"Caso2 Condiciones fijas 0s")
grafica(Tc2a100,"Caso2 Condiciones fijas 100s")
grafica(Tc2a2500,"Caso2 Condiciones fijas 2500s")

grafica(Tc2p0,"Caso2 Condiciones periodicas 0s")
grafica(Tc2p100,"Caso2 Condiciones periodicas 100s")
grafica(Tc2p2500,"Caso2 Condiciones periodicas 2500s")
