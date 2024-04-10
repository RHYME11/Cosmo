import numpy as np
import Extract as ex
import matplotlib.pyplot as plt
from State import State


#Compare two states;
#They can be from different files;
#Currently, files must be saved in the same folder;
def Comparison(state0='', state1='', opt=True):

  #Input info for two states
  if(opt):
    print(f"\033[1mInitial state:\033[0m")
    isotope0 = input("    " + "isotope(eg. 31Na): ")
    npnh0    = input("    " + "npnh(eg. 0p0h): ")
    spin0    = input("    " + "spin(eg. 5/2) =  ")
    energy0  = input("    " + "binding energy (MeV): ")
    print(f"\033[1mFinal state:\033[0m")
    isotope1 = input("    " + "isotope(eg. 31Na): ")
    npnh1    = input("    " + "npnh(eg. 0p0h): ")
    spin1    = input("    " + "spin(eg. 5/2) =  ")
    energy1  = input("    " + "binding energy (MeV): ")
    if len(isotope0) == 0:
      isotope0 = '31Na'
    if len(npnh0) == 0:
      npnh0 = '0p0h'
    if len(spin0) == 0:
      spin0 = '5/2'
    if len(energy0) == 0:
      energy0 = '0'
    state0 = ex.Extract(isotope0, npnh0, spin0, energy0,0)
    if len(isotope1) == 0:
      isotope1 = '31Na'
    if len(npnh1) == 0:
      npnh1 = '0p0h'
    if len(spin1) == 0:
      spin1 = '5/2'
    if len(energy1) == 0:
      energy1 = '0'
    state1 = ex.Extract(isotope1, npnh1, spin1, energy1,0)



  # Draw orbital occupation for state0 and state1 left and right  
  bar_width = 0.2
  index = np.arange(len(state0.orbitals))
  
  fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(12, 4))
  
  ZbarsI = ax_left.bar(index - bar_width/2, state0.arrZ, bar_width, label='Z', color='orangered')
  NbarsI = ax_left.bar(index + bar_width/2, state0.arrN, bar_width, label='N', color='skyblue')
  ax_left.set_title(f'Initial State: {state0.isotope} {state0.npnh} Jpi = {state0.J}{state0.pi} at E = {state0.E}')
  ax_left.set_xticks(index)
  ax_left.set_xticklabels(state0.orbitals)
  ax_left.set_yticks(np.arange(0, 9, 1))
  for tick in np.arange(0, 9, 1):
      ax_left.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5)
  ax_left.legend()

  ZbarsF = ax_right.bar(index - bar_width/2, state1.arrZ, bar_width, label='Z', color='orangered')
  NbarsF = ax_right.bar(index + bar_width/2, state1.arrN, bar_width, label='N', color='skyblue')
  ax_right.set_title(f'Final State: {state1.isotope} {state1.npnh} Jpi = {state1.J}{state1.pi} at E = {state1.E}')
  ax_right.set_xticks(index)
  ax_right.set_xticklabels(state1.orbitals)
  ax_right.set_yticks(np.arange(0, 9, 1))
  
  for tick in np.arange(0, 9, 1):
      ax_right.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5)
  ax_right.legend()

  for bar in ZbarsI:
    height = bar.get_height()
    ax_left.text(bar.get_x() + bar.get_width() / 2, height+0.1, str(height), ha='center', va='bottom', rotation=90, fontsize=8, color="orangered")
  for bar in NbarsI:
    height = bar.get_height()
    ax_left.text(bar.get_x() + bar.get_width() / 2, height+0.1, str(height), ha='center', va='bottom', rotation=90, fontsize=8, color="skyblue")
  for bar in ZbarsF:
    height = bar.get_height()
    ax_right.text(bar.get_x() + bar.get_width() / 2, height+0.1, str(height), ha='center', va='bottom', rotation=90, fontsize=8, color="orangered")
  for bar in NbarsF:
    height = bar.get_height()
    ax_right.text(bar.get_x() + bar.get_width() / 2, height+0.1, str(height), ha='center', va='bottom', rotation=90, fontsize=8, color="skyblue")


  # Draw the difference between state0 and state1 on neutron and proton occupation
  dN = state1.arrN - state0.arrN
  dZ = state1.arrZ - state0.arrZ
  dfig, dax = plt.subplots()
  ZbarsD = dax.bar(index,             dZ, width=bar_width, label='Z', color='orangered')
  NbarsD = dax.bar(index + bar_width, dN, width=bar_width, label='N', color='skyblue')
  dax.set_title(f'Final State({state1.isotope} {state1.npnh} {state1.J}{state1.pi}) - Initial State({state0.isotope} {state0.npnh} {state0.J}{state0.pi})')
  dax.legend()
  dax.set_xticks(index + bar_width/2, state0.orbitals)        
  for tick in plt.yticks()[0]:
      dax.axhline(y=tick, color='gray', linestyle='--', linewidth=0.5)

  #for bar in ZbarsD:
  #  height = bar.get_height()
  #  dax.text(bar.get_x() + bar.get_width() / 2, height*1.1, str(height), ha='center', va='bottom', rotation=90, fontsize=8, color="orangered")
  #for bar in NbarsD:
  #  height = bar.get_height()
  #  dax.text(bar.get_x() + bar.get_width() / 2, height*1.1, str(height), ha='center', va='bottom', rotation=90, fontsize=8, color="skyblue")

  plt.show(block=False)


