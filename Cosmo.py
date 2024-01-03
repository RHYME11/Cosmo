import numpy as np
import re
import matplotlib.pyplot as plt


class Cosmo:
    def __init__(self, isotope, npnh, J, pi, E, orbitals, arrN, arrZ):
        self.isotope  = isotope
        self.npnh     = npnh
        self.J        = J
        self.pi       = pi
        self.E        = E         # binding energy
        self.orbitals = orbitals  # shell model
        self.arrN     = arrN      # N for each orbitals
        self.arrZ     = arrZ      # Z for each orbitals

    def Draw(self,rangex=(-1,1),rangey=(-1,1)):
        bar_width = 0.2
        index = np.arange(len(self.orbitals))
        fig, ax = plt.subplots()
        ax.bar(index,             self.arrN, width=bar_width, label='N', color='skyblue')
        ax.bar(index + bar_width, self.arrZ, width=bar_width, label='Z', color='orangered')
        ax.set_title(f'{self.isotope} {self.npnh} Jpi={self.J}{self.pi} at E={self.E}')
        ax.legend()
        ax.set_xticks(index + bar_width/2, self.orbitals)
        ax.set_yticks(np.arange(0, 9, 1))
        if rangex[0] >= 0 and rangex[1]>=0:
            ax.set_xlim(rangex[0],rangex[1])
        if rangey[0] >= 0 and rangey[1]>=0:
            ax.set_ylim(rangey[0],rangey[1])
        
        for tick in np.arange(0, 9, 1):
            ax.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5)
        plt.show(block=False)
        return fig, ax
