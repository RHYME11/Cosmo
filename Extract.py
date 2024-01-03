import numpy as np
import re
import matplotlib.pyplot as plt
from Cosmo import Cosmo


##############################################################
# Extract: extract orbital occupation for a specific state in one isotope 
#          with a certain npnh configuration + spin + binding energy
# input: isotope(string), npnh(string), spin(string), (binding) energy(double)
# return a variable in "Cosmo" class
def Extract(isotope='31Na', npnh='0p0h', spin='5/2', energy=0):
  orbitals = []
  N = np.array([])
  Z = np.array([])

  state_begin = '<state J="'
  state_end   = '</state>'
  occupation = 'occupation'
    
  file = open(f"/Users/yiyizhu/Desktop/e18035/CoSMo/{isotope}/{isotope}-{npnh}.txt","r")
  while True:
    content = file.readline()     
    if state_end in content:            
      if J == spin:
        if energy >= 0 or E == energy:
          break
      else:
        orbitals = []
        N = []
        Z = []
    if state_begin in content:
      matches = re.findall(r'"(.*?)"', content)
      J = matches[0]
      pi = matches[1]
      E = float(matches[3])
      #print(f"Jpi = {matches[0]}{matches[1]}")
    if occupation in content:
      matches = re.findall(r'"(.*?)"', content)
      orbitals.append(matches[0])
      N = np.append(N,float(matches[1]))
      Z = np.append(Z,float(matches[2]))
  file.close

  shell = Cosmo(
      isotope,
      npnh,
      J,
      pi,
      E,
      orbitals,
      N,
      Z
  )

  return shell


##############################################################
# Draw: draw orbital occupation for a specific state in one isotope 
#       with a certain npnh configuration + spin + binding energy
def Draw():
  isotope = input("isotope(eg. 31Na): ")
  npnh    = input("npnh(eg. 0p0h): ")
  spin    = input("spin(eg. 5/2) =  ")
  energy  = input("binding energy (MeV): ")
  
  if len(isotope) == 0:
    isotope = '31Na'
  if len(npnh) == 0:
    npnh = '0p0h'
  if len(spin) == 0:
    spin = '5/2'
  if len(energy) == 0:
    energy = '0'
  energy = float(energy)

  state = Extract(isotope, npnh, spin, energy)
  state.Draw()
  


    
