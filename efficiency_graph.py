import matplotlib.pyplot as plt
import numpy as np


def efficiency_graph(mass_flow_rate, temperature_rise):
    efficiency = (mass_flow_rate * temperature_rise) / (mass_flow_rate + temperature_rise)  # Hypothetical efficiency equation.

    plt.figure(figsize=(10, 6))
    plt.plot(mass_flow_rate, efficiency, label='Efficiency Variation', color='b')
    plt.title('Efficiency Variation with Mass Flow Rate and Temperature Rise')
    plt.xlabel('Mass Flow Rate')
    plt.ylabel('Efficiency')
    plt.grid(True)
    plt.legend()
    plt.show()


# Example usage
if __name__ == '__main__':  
    flow_rate = np.linspace(0, 10, 100)
    temp_rise = 5
    efficiency_graph(flow_rate, temp_rise)
