import array
import rp2
import time
import math
from machine import Pin, Timer

# Configuration
NUM_LEDS = 12  # LEDs in the fan
LED_PIN = 18  # GPIO Pin
MAX_BRIGHTNESS = 0.5  # Adjust brightness (0.0 - 1.0)
HUE_SHIFT_SPEED = 3  # Speed of color shifting

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)                .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")    .side(1)    [T1 - 1]
    jmp("bitloop")           .side(1)    [T2 - 1]
    label("do_zero")
    nop()                    .side(0)    [T2 - 1]
    wrap()

# Initialize state machine
sm = rp2.StateMachine(0, ws2812, freq=8000000, sideset_base=Pin(LED_PIN))
sm.active(1)

# LED array
led_array = array.array("I", [0 for _ in range(NUM_LEDS)])

def hsv_to_rgb(h, s, v):
    """Convert HSV to RGB. h: 0-360, s: 0-1, v: 0-1"""
    h = h % 360  # Ensure hue wraps around
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if h < 60:
        r, g, b = c, x, 0
    elif h < 120:
        r, g, b = x, c, 0
    elif h < 180:
        r, g, b = 0, c, x
    elif h < 240:
        r, g, b = 0, x, c
    elif h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    return int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)

def rgb_to_color(r, g, b):
    """Convert RGB to 24-bit color."""
    return (g << 16) | (r << 8) | b

def set_pixel(led_index, color):
    """Set a specific LED to a color."""
    if 0 <= led_index < NUM_LEDS:
        led_array[led_index] = color

def show():
    """Update the LEDs."""
    sm.put(led_array, 8)

# Animation state
hue_base = 0  # Starting hue

def update_leds(timer):
    """Smoothly transition through the rainbow."""
    global hue_base
    hue_base = (hue_base + HUE_SHIFT_SPEED) % 360  # Increment hue

    for i in range(NUM_LEDS):
        hue = (hue_base + (i * 30)) % 360  # Offset each LED for a wave effect
        r, g, b = hsv_to_rgb(hue, 1, MAX_BRIGHTNESS)  # Full saturation, limited brightness
        set_pixel(i, rgb_to_color(r, g, b))

    show()

# Timer to update LEDs
timer = Timer()
timer.init(freq=20, mode=Timer.PERIODIC, callback=update_leds)  # Update 20 times per second
