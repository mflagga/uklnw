# pyright: reportUndefinedVariable=false
import numpy as np
import matplotlib.pyplot as plt

def wczytaj(*nazwy): # funkcja do wczytywania plikow od clauda
    for nazwa in nazwy:
        globals()[nazwa] = np.loadtxt(nazwa + ".csv", delimiter=',')

# wczytanie danych
wczytaj("p1psi", "p1E", "p1V")
x = p1psi[:,0]
p1_psi = p1psi[:,1]
p1_E = p1E[:,0]
p1_T = p1E[:,1]
p1V0=np.max(p1V)

plt.figure(figsize=(8,8))
plt.plot(x,p1_psi)
for i in range(len(x)-1):
    plt.axvspan(x[i],x[i+1],color="black",alpha=p1V[i]/(np.max(p1V)),lw=0)
plt.savefig("p1psi.png")
plt.close()

plt.figure(figsize=(8,8))
plt.plot(p1_E,p1_T)
plt.xlabel(rf'$E\ [eV]$')
plt.ylabel(rf'T(E)')
plt.axvline(p1V0, ls="--",color="black")
plt.grid(ls=':')
plt.savefig("p1E.png")
plt.close()
