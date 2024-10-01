

import matplotlib.pyplot as plt
from miniCodes import *

def draw_level_schemes(nuclei, A, energy, jpi):
    num_nuclei = len(nuclei)
    
    fig_width = 4 * num_nuclei  # Increase the width based on the number of nuclei
    fig, ax = plt.subplots(figsize=(fig_width, 8))  # Adjust figure size based on number of nuclei
    
    # x_positions: Centers of the x-axis regions for each nucleus
    x_positions = [(i + .5) / num_nuclei for i in range(num_nuclei)]
    
    for i in range(num_nuclei):
        xmin = x_positions[i] - 0.05  # Adjust to ensure space around each nucleus
        xmax = x_positions[i] + 0.05  # Width for each level scheme
        
        # Draw the level scheme for each nucleus
        for j, e in enumerate(energy[i]):
            ax.hlines(e, xmin=xmin, xmax=xmax, color='black', lw=2)
            
            # Label energy on the left
            ax.text(xmin - 0.01, e, f'{e:.0f}', verticalalignment='center', horizontalalignment='right', fontsize=12)
            
            # Label spin-parity on the right
            ax.text(xmax + 0.01, e, jpi[i][j], verticalalignment='center', horizontalalignment='left', fontsize=12)
        
        # Label nucleus at the bottom center of its section
        ax.text((xmin + xmax) / 2, -100, f'{A[i]}{nuclei[i]}', verticalalignment='top', horizontalalignment='center', fontsize=18)

    # Remove x and y ticks, adjust plot limits
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Calculate global min and max energy to scale the y-axis
    global_min_energy = min(min(e) for e in energy)
    global_max_energy = max(max(e) for e in energy)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(global_min_energy - 250, global_max_energy + 250)

    # Show the plot
    plt.show()


#===========================================================================================================================#
def split_array_by_none(arr):
    sub_arrays = []
    current_sub_array = []

    for item in arr:
        if item is None:
            # If we encounter None, we append the current sub-array to the list and reset it
            if current_sub_array:
                sub_arrays.append(current_sub_array)
                current_sub_array = []
        else:
            # Otherwise, keep adding items to the current sub-array
            current_sub_array.append(item)
    
    # Add the last sub-array if it exists
    if current_sub_array:
        sub_arrays.append(current_sub_array)

    return sub_arrays


#=======================================================================================#
def Input():
  isotope_symbol = []
  isotope_A = []
  energy = []
  jpi = []

  nnuc = 1
  nstate = 1

  isotope_str = input("Enter isotope (e.g., 16O): ")
  symbol, A = get_isotope_details(isotope_str)
  isotope_symbol.append(symbol)
  isotope_A.append(A)
  print(f"Generate states in {ordinal(nnuc)} nucleus")

  while True:
    add_state = input("Do you want to generate a new state, y(default)/n: ").strip().lower()
    if not add_state:
      add_state = 'yes'
  
    if 'y' in add_state:
      state_energy = get_float_input(f"Enter the energy of {ordinal(nstate)} state in {ordinal(nnuc)} nucleus (unit: keV): ")
      state_jpi = input(f"Enter the spin-parity of {ordinal(nstate)} state in {ordinal(nnuc)} nucleus (e.g. 1/2+): ")
      energy.append(state_energy)
      jpi.append(state_jpi)
      nstate += 1
    elif 'n' in add_state:
      nnuc += 1
      add_nucleus = input(f"Do you want to generate {ordinal(nnuc)} nucleus, y(default)/n: ").strip().lower()
      if not add_nucleus:
        add_nucleus = 'yes'
      if 'y' in add_nucleus:
        energy.append(None)
        jpi.append(None)
        nstate = 1
        isotope_str = input("Enter isotope (e.g., 16O): ")
        symbol, A = get_isotope_details(isotope_str)
        isotope_symbol.append(symbol)
        isotope_A.append(A)
        print(f"Generate states for {ordinal(nnuc)} nucleus NOW!")
        continue
      elif 'n' in add_nucleus:      
        break;
      else:
        print("Please answer with 'y' or 'n'.")  
    else:
      print("Please answer with 'y' or 'n'.")  
    
  return isotope_symbol, isotope_A, energy, jpi


#def Draw_LS():
isotope, A, energy, jpi = Input()
sort_energy = split_array_by_none(energy)
sort_jpi = split_array_by_none(jpi)
draw_level_schemes(isotope, A, sort_energy, sort_jpi)


