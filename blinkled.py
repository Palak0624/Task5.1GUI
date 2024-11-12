# Importing necessary libraries
import tkinter as tk 
from gpiozero import LED 

# Creating LED objects on GPIO pins 17, 2, and 3
first_led = LED(17) 
second_led = LED(2) 
third_led = LED(3)  

# Function to turn off all LEDs
def deactivate_all_leds():
    first_led.off() 
    second_led.off()  
    third_led.off() 

# Deactivate all LEDs initially when the program starts
deactivate_all_leds()

# Function to activate the LED based on the user's choice
def activate_led(led_number):
    deactivate_all_leds() 
    if led_number == 1:
        first_led.on()  
    elif led_number == 2:
        second_led.on()  
    elif led_number == 3:
        third_led.on() 

# Function to handle the LED selection event (when a user selects a radio button)
def handle_led_selection():
    chosen_led = led_choice.get() 
    activate_led(chosen_led) 

# Function to close the application window and reset LEDs before exiting
def close_application():
    deactivate_all_leds() 
    app_window.quit()  

# Create the main Tkinter window
app_window = tk.Tk()
app_window.title("LED Controller") 

# Variable to store the user's LED choice (1, 2, or 3)
led_choice = tk.IntVar()

# Create a label widget for the title of the application
title_label = tk.Label(app_window, text="LED Controller", font=("Arial", 20))
title_label.pack(pady=10) 

# Create radio buttons to select which LED to activate
led_radio_1 = tk.Radiobutton(app_window, text="Activate LED 1", variable=led_choice, value=1, command=handle_led_selection)
led_radio_2 = tk.Radiobutton(app_window, text="Activate LED 2", variable=led_choice, value=2, command=handle_led_selection)
led_radio_3 = tk.Radiobutton(app_window, text="Activate LED 3", variable=led_choice, value=3, command=handle_led_selection)

# Add the radio buttons to the window, with padding and alignment
led_radio_1.pack(anchor=tk.W, padx=20)
led_radio_2.pack(anchor=tk.W, padx=20)
led_radio_3.pack(anchor=tk.W, padx=20)

# Create a button to reset all LEDs to off state
reset_leds_button = tk.Button(app_window, text="Reset LEDs", command=deactivate_all_leds)
reset_leds_button.pack(pady=10) 

# Create an "Exit" button to close the application
exit_button = tk.Button(app_window, text="Exit", command=close_application)
exit_button.pack(pady=10) 
# Start the Tkinter event loop to run the GUI
app_window.mainloop()
