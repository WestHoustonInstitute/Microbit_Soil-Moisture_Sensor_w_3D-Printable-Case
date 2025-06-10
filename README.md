# Microbit Soil Moisture Sensor with 3D Printable Case

This repository will:
1. Help you **get started** with beginner electronics, microcontroller programming, and 3D printing integration.
2. Provide a simple example of how to use a **soil moisture sensor** with a micro:bit and visualize data on the device.
3. Demonstrate how to build a practical IoT sensor project with an interactive display and a 3D-printed protective case.

# What do you need for this project?

* 1x micro:bit
* 1x micro:bit Sensor Shield V2
* 1x Soil Humidity Sensor
* 3x Jumper Wires
* 1x Battery
* 1x USB to USB-C Cable

We used components from Keyestudio's "37 in 1 Starter Kit for BBC micro:bit". Check your kit and collect the required parts.

<img src="https://github.com/user-attachments/assets/47acbabb-18b4-49d5-adba-f83b402e7392" alt="hardware_list" width="400" height="400">

# Step 1: Software Setup

Follow the steps in the [`1-)Software_Setup`](./1-%29Software_Setup/) folder:

1. Review the detailed **Code_Blocks.pdf** guide.
2. Follow each step with visual references:
    - ![Step 1](./1-%29Software_Setup/Step-1.PNG)
    - ![Step 2](./1-%29Software_Setup/Step-2.PNG)
    - ![Step 3](./1-%29Software_Setup/Step-3.PNG)
    - ![Step 4](./1-%29Software_Setup/Step-4.PNG)
    - ![Step 5](./1-%29Software_Setup/Step-5.PNG)
    - ![Step 6](./1-%29Software_Setup/Step-6.PNG)
    - ![Step 7](./1-%29Software_Setup/Step-7.PNG)
    - ![Step 8 Complete](./1-%29Software_Setup/Step-8_Complete.PNG)
3. Optionally review the example [`code(optional).py`](./1-%29Software_Setup/code(optional).py).
4. If you prefer, you can flash the ready-to-use [`microbit-moisture_soil.hex`](./1-%29Software_Setup/microbit-moisture_soil.hex) directly onto your micro:bit using the USB cable.

# Step 2: Hardware Setup

Follow the steps in the [`2-)Hardware_Setup`](./2-%29Hardware_Setup/) folder:

1. Connect your Soil Humidity Sensor as shown in the images:
    - ![Step 1](./2-%29Hardware_Setup/Step-1.jpeg)
    - ![Step 2](./2-%29Hardware_Setup/Step-2.jpeg)
    - ![Step 3](./2-%29Hardware_Setup/Step-3.jpeg)
    - ![Step 4 Complete](./2-%29Hardware_Setup/Step-4_Complete.jpeg)
2. Use the provided [`Instructions.txt`](./2-%29Hardware_Setup/Instructions.txt) to guide the wiring and assembly.
3. Optionally 3D print the case for better protection and usability of your project.

# Step 3: How to Use the Sensor

1. Insert the sensor into the soil.
2. Press button **A** on your micro:bit.
3. The micro:bit will display the current **soil moisture level** on the LED grid (range 0–100):
    * 0 = no moisture detected (dry soil)
    * 100 = fully saturated soil.

Example of a completed setup:

<img src="https://github.com/user-attachments/assets/4ffb5ce8-ea9f-44f7-84ba-c70a9ef8a3c0" alt="Completed" width="500" height="500">

# Summary

Once you follow the Software Setup and Hardware Setup, you will have a working **soil moisture sensor** that displays real-time readings on your micro:bit. You can extend this project with:
- Radio communication to log data remotely
- Alerts when moisture is too low/high
- Integration into a larger smart garden system
- Data visualization in Python using micro:bit serial output

---

Happy building!
