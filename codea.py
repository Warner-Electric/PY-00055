
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Slider, Button
import datetime

# Constants and defaults
A = 1.0  # Amplitude
C = 0.000010  # Capacitance

# Time array
t = np.linspace(0, 10, 1000)

# Default parameters
frequency_default = 1.0
inductance_default = 1.0
resistance_default = 1.0

frequency = frequency_default
inductance = inductance_default
resistance = resistance_default

# Create figure with sections: plot, inputs, sliders, buttons, equations
fig = plt.figure(figsize=(10, 12))
ax_plot = plt.axes([0.1, 0.55, 0.85, 0.4])  # Plot area
ax_equation = plt.axes([0.1, 0.05, 0.85, 0.15])  # Equation display area
ax_equation.axis('off')

# Function to draw plot and update equations
def draw_plot_and_equations():
    ax_plot.clear()
    f = frequency
    L = inductance
    R = resistance
    alpha = R / (2 * L)
    f0 = 1 / (2 * np.pi * np.sqrt(L * C))

    # Plot signals
    input_signal = A * np.sin(2 * np.pi * f * t)
    rlc_response = input_signal * np.exp(-alpha * t)
    ax_plot.plot(t, input_signal, label='Input Signal')
    ax_plot.plot(t, rlc_response, label=f'RLC Response (α={alpha:.2f})', linestyle='--')
    ax_plot.set_xlabel('Time (s)')
    ax_plot.set_ylabel('Amplitude')
    ax_plot.set_title('RLC System Response')
    ax_plot.legend()
    ax_plot.grid(True)

    # Update equation text
    ax_equation.clear()
    ax_equation.axis('off')
    equation_text = (
        f"Input Signal: A * sin(2πft)\n"
        f"RLC Response: A * sin(2πft) * exp(-αt)\n"
        f"α = R / (2L)\n"
        f"f₀ = 1 / (2π√(LC))\n\n"
        f"Current Values:\n"
        f"f = {f:.2f}, L = {L:.2f}, R = {R:.2f}\n"
        f"α = {alpha:.4f}, f₀ = {f0:.4f}"
    )
    ax_equation.text(0.5, 0.5, equation_text, fontsize=12,
                     verticalalignment='center', horizontalalignment='center',
                     bbox=dict(facecolor='white', alpha=0.7))

    fig.canvas.draw_idle()

# Initial draw
draw_plot_and_equations()

# Update functions for TextBoxes and Sliders
def update_frequency(text):
    global frequency
    try:
        frequency = float(text)
        slider_f.set_val(frequency)
        draw_plot_and_equations()
    except ValueError:
        print("Invalid frequency")

def update_inductance(text):
    global inductance
    try:
        inductance = float(text)
        slider_L.set_val(inductance)
        draw_plot_and_equations()
    except ValueError:
        print("Invalid inductance")

def update_resistance(text):
    global resistance
    try:
        resistance = float(text)
        slider_R.set_val(resistance)
        draw_plot_and_equations()
    except ValueError:
        print("Invalid resistance")

def slider_update_frequency(val):
    global frequency
    frequency = val
    text_box_f.set_val(str(val))
    draw_plot_and_equations()

def slider_update_inductance(val):
    global inductance
    inductance = val
    text_box_L.set_val(str(val))
    draw_plot_and_equations()

def slider_update_resistance(val):
    global resistance
    resistance = val
    text_box_R.set_val(str(val))
    draw_plot_and_equations()

# Reset button callback
def reset_defaults(event):
    global frequency, inductance, resistance
    frequency = frequency_default
    inductance = inductance_default
    resistance = resistance_default
    text_box_f.set_val(str(frequency_default))
    text_box_L.set_val(str(inductance_default))
    text_box_R.set_val(str(resistance_default))
    slider_f.set_val(frequency_default)
    slider_L.set_val(inductance_default)
    slider_R.set_val(resistance_default)
    draw_plot_and_equations()

# Save Plot button callback
def save_plot(event):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"rlc_plot_{timestamp}.png"
    fig.savefig(filename)
    print(f"Plot saved as {filename}")

# TextBoxes
text_box_f_ax = plt.axes([0.3, 0.49, 0.4, 0.04])
text_box_f = TextBox(text_box_f_ax, 'Frequency:', initial=str(frequency_default))
text_box_f.on_submit(update_frequency)

text_box_L_ax = plt.axes([0.3, 0.45, 0.4, 0.04])
text_box_L = TextBox(text_box_L_ax, 'Inductance:', initial=str(inductance_default))
text_box_L.on_submit(update_inductance)

text_box_R_ax = plt.axes([0.3, 0.41, 0.4, 0.04])
text_box_R = TextBox(text_box_R_ax, 'Resistance:', initial=str(resistance_default))
text_box_R.on_submit(update_resistance)

# Sliders
slider_f_ax = plt.axes([0.3, 0.36, 0.4, 0.02])
slider_f = Slider(slider_f_ax, 'Freq Slider', 0.1, 10.0, valinit=frequency_default)
slider_f.on_changed(slider_update_frequency)

slider_L_ax = plt.axes([0.3, 0.33, 0.4, 0.02])
slider_L = Slider(slider_L_ax, 'Induct Slider', 0.1, 10.0, valinit=inductance_default)
slider_L.on_changed(slider_update_inductance)

slider_R_ax = plt.axes([0.3, 0.30, 0.4, 0.02])
slider_R = Slider(slider_R_ax, 'Resist Slider', 0.1, 10.0, valinit=resistance_default)
slider_R.on_changed(slider_update_resistance)

# Buttons
reset_button_ax = plt.axes([0.35, 0.26, 0.12, 0.04])
reset_button = Button(reset_button_ax, 'Reset Defaults')
reset_button.on_clicked(reset_defaults)

save_button_ax = plt.axes([0.52, 0.26, 0.12, 0.04])
save_button = Button(save_button_ax, 'Save Plot')
save_button.on_clicked(save_plot)

plt.show()
