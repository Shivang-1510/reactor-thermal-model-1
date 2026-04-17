# Configuration
CONFIG = {
    'mass_flow_rate': 500,      # kg/s (coolant flow)
    'specific_heat': 4200,      # J/kg-K (water)
    'delta_T': 30,              # K (temperature rise)
    'reactor_power': 3000,      # MW thermal
}

def calculate_heat_removal(mass_flow_rate, specific_heat, delta_T):
    """
    Calculate heat removed by coolant.
    
    Args:
        mass_flow_rate: kg/s
        specific_heat: J/kg-K
        delta_T: K
    
    Returns:
        Heat in Watts
    """
    return mass_flow_rate * specific_heat * delta_T

def calculate_efficiency(heat_removal_w, reactor_power_mw):
    """
    Calculate cooling efficiency.
    
    Args:
        heat_removal_w: Watts
        reactor_power_mw: MW
    
    Returns:
        Efficiency as percentage
    """
    return (heat_removal_w / (reactor_power_mw * 1e6)) * 100

def main():
    Q = calculate_heat_removal(
        CONFIG['mass_flow_rate'],
        CONFIG['specific_heat'],
        CONFIG['delta_T']
    )
    
    efficiency = calculate_efficiency(Q, CONFIG['reactor_power'])
    
    print("=" * 50)
    print("Reactor Thermal Model Results")
    print("=" * 50)
    print(f"Heat removed by coolant: {Q/1e6:.2f} MW")
    print(f"Cooling efficiency: {efficiency:.2f}%")
    print("=" * 50)

if __name__ == '__main__':
    main()