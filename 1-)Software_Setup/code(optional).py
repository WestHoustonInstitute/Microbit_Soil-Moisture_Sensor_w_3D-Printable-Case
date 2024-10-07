from microbit import *

moisturereading = 0

def on_button_pressed_a():
    global moisturereading
    moisturereading = Math.map(pins.analog_read_pin(AnalogPin.P0), 0, 750, 0, 100)
    basic.show_number(Math.round(moisturereading))
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
