import numpy as np

nx = 100
ny = 100
nu = .0004
dx = 1
dy = 1
sigma = .25
dt = sigma * dx * dy / nu

x = np.linspace(0, nx, nx)
y = np.linspace(0, ny, ny)

u = np.ones((ny, nx)) 
u[:,:]=50
un = np.ones((ny, nx))

X, Y = np.meshgrid(x, y)

u[int(30):int(55),int(20):int(45)] = 100

def caso1(u,nt,condicion):
    for n in range(nt + 1): 
        un = u.copy()
        u[1:-1, 1:-1] = (un[1:-1,1:-1] + 
                        nu * dt / dx**2 * 
                        (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                        nu * dt / dy**2 * 
                        (un[2:,1: -1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1]))
        if condicion == "abierta":
            u[0, :]=u[1, :]
            u[99, :] =u[98, :] 
            u[:, 0] = u[:, 1]
            u[:, 99] = u[:, 98]

        elif condicion == "fijas":
            u[0, :]=50
            u[-1, :] =50
            u[:, 0] = 50
            u[:, -1] = 50
        elif condicion == "periodicas":
            u[0, :]=u[1, :]
            u[-1, :] =u[0, :]
            u[:, 0] =u[:, 1]
            u[:, -1] = u[:, 0]
    return u[:]

def caso2(u,nt,condicion):
    for n in range(nt + 1): 
        un = u.copy()
        u[1:-1, 1:-1] = (un[1:-1,1:-1] + 
                        nu * dt / dx**2 * 
                        (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                        nu * dt / dy**2 * 
                        (un[2:,1: -1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1]))
        if condicion == "abierta":
            u[0, :]=u[1, :]
            u[99, :] =u[98, :] 
            u[:, 0] = u[:, 1]
            u[:, 99] = u[:, 98]

        elif condicion == "fijas":
            u[0, :]=50
            u[-1, :] =50
            u[:, 0] = 50
            u[:, -1] = 50

        elif condicion == "periodicas":
            u[0, :]=u[1, :]
            u[-1, :] =u[0, :]
            u[:, 0] =u[:, 1]
            u[:, -1] = u[:, 0]
        u[int(30):int(55),int(20):int(45)] = 100
    return u[:]

np.savetxt('X.txt', X)
np.savetxt('Y.txt', Y)

uc1a0 =caso1(u,0, "abiertas")
np.savetxt('Tc1a0.txt', uc1a0)
uc1a100=caso1(u,100, "abiertas")
np.savetxt('Tc1a100.txt', uc1a100)
uc1a2500=caso1(u,2500, "abiertas")
np.savetxt('Tc1a2500.txt', uc1a2500)


uc1f0=caso1(u,0, "fijas")
np.savetxt('Tc1f0.txt', uc1f0)
uc1f100=caso1(u,100, "fijas")
np.savetxt('Tc1f100.txt', uc1f100)
uc1f2500=caso1(u,2500, "fijas")
np.savetxt('Tc1f2500.txt', uc1f2500)

uc1p0=caso1(u,0, "periodicas")
np.savetxt('Tc1p0.txt', uc1p0)
uc1p100=caso1(u,100, "periodicas")
np.savetxt('Tc1p100.txt', uc1p100)
uc1p2500=caso1(u,2500, "periodicas")
np.savetxt('Tc1p2500.txt', uc1p2500)

uc2a0 =caso1(u,0, "abiertas")
np.savetxt('Tc2a0.txt', uc2a0)
uc2a100=caso1(u,100, "abiertas")
np.savetxt('Tc2a100.txt', uc2a100)
uc2a2500=caso1(u,2500, "abiertas")
np.savetxt('Tc2a2500.txt', uc2a2500)

uc2f0=caso1(u,0, "fijas")
np.savetxt('Tc2f0.txt', uc2f0)
uc2f100=caso1(u,100, "fijas")
np.savetxt('Tc2f100.txt', uc2f100)
uc2f2500=caso1(u,2500, "fijas")
np.savetxt('Tc2f2500.txt', uc2f2500)

uc2p0=caso2(u,0, "periodicas")
np.savetxt('Tc2p0.txt', uc2p0)
uc2p100=caso2(u,100, "periodicas")
np.savetxt('Tc2p100.txt', uc2p100)
uc2p2500=caso2(u,2500, "periodicas")
np.savetxt('Tc2p2500.txt', uc2p2500)


#caso2(u,100, "periodica")
#plt.show()
