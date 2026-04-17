import numpy as np

# Inputs
mass_flow_rate = 500  # kg/s (coolant flow)
specific_heat = 4200  # J/kg-K (water)
delta_T = 30  # temperature rise (K)

# Heat removal
Q = mass_flow_rate * specific_heat * delta_T  # Watts

print(f"Heat removed by coolant: {Q/1e6:.2f} MW")

# Reactor power assumption
reactor_power = 3000  # MW thermal

efficiency = (Q / (reactor_power * 1e6)) * 100

print(f"Cooling efficiency: {efficiency:.2f}%")
