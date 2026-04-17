# Reactor Thermal Analysis using Python

## Overview

This project models the thermal behavior of a nuclear reactor cooling system by calculating the heat removed by the coolant. It provides a simplified analysis of reactor heat transfer and cooling efficiency, which are critical for safe reactor operation.

## Objectives

* Calculate heat removal from reactor core using coolant flow
* Analyze temperature rise in coolant
* Estimate cooling efficiency of the reactor system
* Understand basic thermal-hydraulic principles in nuclear reactors

## Theory

The heat removed by the coolant is calculated using:

Q = m × c × ΔT

Where:

* Q = Heat transfer rate (W)
* m = Mass flow rate of coolant (kg/s)
* c = Specific heat capacity (J/kg·K)
* ΔT = Temperature rise (K)

## Methodology

* Assumed water as coolant
* Used standard thermodynamic relation for heat transfer
* Defined reactor operating parameters (flow rate, temperature rise)
* Computed total heat removal and compared with reactor power

## Results

* Calculated heat removal capacity of coolant system
* Estimated cooling efficiency relative to reactor thermal power
* Demonstrated importance of coolant flow in reactor safety

## Tools & Technologies

* Python
* NumPy

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the program:
   python main.py

## Sample Output

Heat removed by coolant: 63.00 MW
Cooling efficiency: 2.10 %

## Applications

* Nuclear reactor thermal analysis
* Cooling system design
* Safety analysis in power plants
* Energy system modeling

## Future Improvements

* Add graphical visualization (temperature vs flow rate)
* Include different coolants (liquid sodium, helium)
* Extend to transient heat transfer analysis
* Integrate with reactor simulation models

## Author

Shivang Arora
B.Tech Energy Engineering
Interest: Nuclear Energy Systems & Reactor Analysis
