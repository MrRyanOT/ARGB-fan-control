# Rainbow Fade LED Control for Raspberry Pi Pico

This project controls a **single fan's 12 RGB LEDs** connected to **Pin 18** of the Raspberry Pi Pico. The LEDs cycle through a **smooth rainbow fade effect** using the **WS2812** LED protocol, creating a beautiful and dynamic lighting effect for your setup.

## Features
- Control **12 LEDs** per fan.
- **Smooth rainbow fade effect**.
- Each LED gradually transitions through **different colors** for a wave-like effect.
- Uses **PWM (Pulse Width Modulation)** for brightness control.
- Created using **MicroPython** and the **RP2040's PIO (Programmable I/O)** to communicate with WS2812 LEDs.

## Hardware Requirements
- **Raspberry Pi Pico** or any compatible board with the **RP2040** chip.
- **12 WS2812 RGB LEDs**.
- **Jumper wires** to connect the LEDs to **GPIO Pin 18**.

## Software Requirements
- **MicroPython** installed on the Raspberry Pi Pico.
- **`rp2` module** (comes pre-installed with MicroPython for RP2040).

## Setup Instructions

### 1. Install MicroPython on Raspberry Pi Pico
If you haven't already, install **MicroPython** on your Raspberry Pi Pico:
- Download the latest **MicroPython firmware** from the official [MicroPython site](https://micropython.org/download/rp2-pico/).
- Hold the **BOOTSEL** button on the Raspberry Pi Pico and plug it into your computer.
- Copy the **MicroPython firmware** file to the Pico.

### 2. Connect the LEDs
- Connect the **Data Input Pin (DI)** of your WS2812 LED strip to **GPIO Pin 18** on the Raspberry Pi Pico.
- Connect the **GND** and **VCC** of the LED strip to **GND** and **5V** on the Raspberry Pi Pico, respectively.

### 3. Upload the Code
- Download and open the `main.py` script.
- Use any editor (e.g., **Thonny** or **uPyCraft**) to upload the script to your Raspberry Pi Pico.

### 4. Run the Code
Once the code is uploaded, the LEDs should start running a smooth **rainbow fade effect** on your fan.

## How It Works
This project uses **Programmable I/O (PIO)** on the Raspberry Pi Pico to control the **WS2812** LEDs. The LEDs are updated periodically in a loop, and the colors cycle through the **hue spectrum** (from red, orange, yellow, green, blue, indigo, violet).

The script uses the **HSV (Hue, Saturation, Value)** color model to create a smooth transition of colors. The **brightness** is set to a value of `0.5` to ensure the LEDs are not too bright.

## Code Explanation
1. **WS2812 Protocol**: The `ws2812` function is a **PIO program** that generates the necessary signals for controlling the LEDs.
2. **HSV to RGB Conversion**: The `hsv_to_rgb` function converts hue values into RGB values.
3. **LED Update**: The `update_leds` function updates the LEDs by changing their colors based on the current hue value, creating the **rainbow fade** effect.

## Customization
- **Number of LEDs**: Change `NUM_LEDS` to match your setup (default is 12).
- **Speed of Color Transition**: Modify `HUE_SHIFT_SPEED` to change how fast the colors change.
- **Brightness**: Adjust `MAX_BRIGHTNESS` to make the LEDs dimmer or brighter.

## Contributing
Feel free to open issues, contribute improvements, or suggest new features. Pull requests are welcome!

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## Credits
- **MicroPython**: [https://micropython.org/](https://micropython.org/)
- **RP2040**: Raspberry Pi's custom chip for low-level hardware access.
- **WS2812 LED protocol**: A popular protocol for controlling RGB LEDs.
"""

# Save the content to a .md file
file_path = '/mnt/data/README.md'
with open(file_path, 'w') as file:
    file.write(readme_content)

file_path  # Return the path to the generated file
