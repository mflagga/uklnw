# pyright: reportUndefinedVariable=false
import numpy as np
import matplotlib.pyplot as plt
import time

t0 = time.time()

def wczytaj(*nazwy): # funkcja do wczytywania plikow od clauda
    for nazwa in nazwy:
        globals()[nazwa] = np.loadtxt(nazwa + ".csv", delimiter=',')

# wczytanie danych
wczytaj("p1psi", "p1E", "p1V", "p2E", "p3E", "p3psi", "p2psi", "misc")
x = p1psi[:,0]
p1_psi = p1psi[:,1]
p1_E = p1E[:,0]
p1_T = p1E[:,1]
p1V0=np.max(p1V)
p2_E = p2E[:,0]
p2_T = p2E[:,1]
p3_E = p3E[:,0]
p3_T = p3E[:,1]
p3_psi = p3psi[:,0]
p3_V = p3psi[:,1]
p2_psi = p2psi[:,0]
p2_V = p2psi[:,1]

# ==1==

# psi(x)
plt.figure(figsize=(8,8))
plt.plot(x,p1_psi,label=rf'$|\Psi|^2$',c='r')
for i in range(len(x)-1):
    plt.axvspan(x[i],x[i+1],color="black",alpha=0.5*p1V[i]/(np.max(p1V)),lw=0)
plt.legend()
plt.grid(ls=':')
plt.xlabel(rf'$x\ [nm]$')
plt.tight_layout()
plt.savefig("p1psi.png")
plt.close()

# T(E)
idx = p1_E==misc[0] # illegal floating point comparison
plt.figure(figsize=(8,8))
plt.axvline(p1V0, ls="--",color="black",label=rf'$V_0$')
plt.plot(p1_E,p1_T)
plt.scatter(p1_E[idx],p1_T[idx],c='r')
plt.xlabel(rf'$E\ [eV]$')
plt.ylabel(rf'T(E)')
plt.legend()
plt.grid(ls=':')
plt.tight_layout()
plt.savefig("p1E.png")
plt.close()

# ==2==

# T(E)
idx = p2_E==misc[1]
plt.figure(figsize=(8,8))
plt.plot(p2_E,p2_T)
plt.xlabel(rf'$E\ [eV]$')
plt.ylabel(rf'T(E)')
plt.scatter(p2_E[idx],p2_T[idx],c='r')
# plt.axvline(p1V0, ls="--",color="black",label=rf'$V_0$')
# plt.legend()
plt.grid(ls=':')
plt.tight_layout()
plt.savefig("p2E.png")
plt.close()

# psi(x)
plt.figure(figsize=(8,8))
plt.plot(x,p2_psi,label=rf'$|\Psi|^2$',c='r')
for i in range(len(x)-1):
    plt.axvspan(x[i],x[i+1],color="black",alpha=0.5*p2_V[i]/(np.max(p2_V)),lw=0)
plt.legend()
plt.xlabel(rf'$x\ [nm]$')
plt.grid(ls=':')
plt.tight_layout()
plt.savefig("p2psi.png")
plt.close()

# ==3==

# T(E)
idx = p3_E==misc[2]
plt.figure(figsize=(8,8))
plt.axvline(p1V0, ls="--",color="black",label=rf'$V_0$')
plt.plot(p3_E,p3_T)
plt.xlabel(rf'$E\ [eV]$')
plt.scatter(p3_E[idx],p3_T[idx],c='r')
plt.ylabel(rf'T(E)')
plt.legend()
plt.tight_layout()
plt.grid(ls=':')
plt.savefig("p3E.png")
plt.close()

# psi(x)
plt.figure(figsize=(8,8))
plt.plot(x,p3_psi,label=rf'$|\Psi|^2$',c='r')
for i in range(len(x)-1):
    plt.axvspan(x[i],x[i+1],color="black",alpha=0.5*p3_V[i]/(np.max(p3_V)),lw=0)
plt.legend()
plt.xlabel(rf'$x\ [nm]$')
plt.grid(ls=':')
plt.tight_layout()
plt.savefig("p3psi.png")
plt.close()

t1 = time.time()
print(f'Czas wykreslania: {t1-t0:.4f}s')
