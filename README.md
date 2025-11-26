
# RLC System Response Visualizer

## Overview
This Python program provides an interactive GUI to visualize the time-domain response of an **RLC circuit** to a sinusoidal input signal. Users can adjust **frequency (f)**, **inductance (L)**, and **resistance (R)** using **text boxes** or **sliders**, and see the plot update in real time. It also displays key theoretical equations and computed values for damping and resonant frequency.

<img width="1914" height="1014" alt="image" src="https://github.com/user-attachments/assets/812196d6-1176-4acf-a6b9-464efe249533" />

---

## Features
- **Interactive Plot**: Shows input signal and RLC response.
- **Live Updates**: Plot and equations update instantly when sliders or text boxes change.
- **Reset Button**: Restores default values (f = 1.0 Hz, L = 1.0 H, R = 1.0 Ω).
- **Save Plot Button**: Exports the current plot as a PNG file with a timestamped filename.
- **Equation Display**: Shows formulas and computed values for:
  - Damping coefficient:  
    $\[
    \alpha = \frac{R}{2L}
    \]$
  - Resonant frequency:  
    $\[
    f_0 = \frac{1}{2\pi\sqrt{LC}}
    \]$
What it means:
f₀ is the natural frequency at which the circuit would oscillate if there were no resistance (ideal LC circuit).
High f₀ (small L or C):

Faster oscillations.


Low f₀ (large L or C):

Slower oscillations.

Interpretation in the plot:

f₀ is not directly the input frequency (f), but it tells you where resonance occurs.
If the input frequency f ≈ f₀, the circuit would normally exhibit maximum amplitude (in a lightly damped system).


Practical Insight

α controls energy dissipation (how fast the system loses energy).
f₀ controls natural oscillation speed (how fast the system would oscillate without damping).    

---

## Operation
1. **Run the program**:
   ```bash
   python codea.py
