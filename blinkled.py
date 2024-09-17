import tkinter as tk
from gpiozero import LED

first_led = LED(17)
second_led = LED(2)
third_led = LED(3)

def deactivate_all_leds():
    first_led.off()
    second_led.off()
    third_led.off()

deactivate_all_leds()

def activate_led(led_number):
    deactivate_all_leds()  
    if led_number == 1:
        first_led.on()
    elif led_number == 2:
        second_led.on()
    elif led_number == 3:
        third_led.on()

def handle_led_selection():
    chosen_led = led_choice.get()
    activate_led(chosen_led)

def close_application():
    deactivate_all_leds()
    app_window.quit()

app_window = tk.Tk()
app_window.title("LED Controller")

led_choice = tk.IntVar()

title_label = tk.Label(app_window, text="LED Controller", font=("Arial", 20))
title_label.pack(pady=10)

led_radio_1 = tk.Radiobutton(app_window, text="Activate LED 1", variable=led_choice, value=1, command=handle_led_selection)
led_radio_2 = tk.Radiobutton(app_window, text="Activate LED 2", variable=led_choice, value=2, command=handle_led_selection)
led_radio_3 = tk.Radiobutton(app_window, text="Activate LED 3", variable=led_choice, value=3, command=handle_led_selection)

led_radio_1.pack(anchor=tk.W, padx=20)
led_radio_2.pack(anchor=tk.W, padx=20)
led_radio_3.pack(anchor=tk.W, padx=20)

reset_leds_button = tk.Button(app_window, text="Reset LEDs", command=deactivate_all_leds)
reset_leds_button.pack(pady=10)

exit_button = tk.Button(app_window, text="Exit", command=close_application)
exit_button.pack(pady=10)

app_window.mainloop()
