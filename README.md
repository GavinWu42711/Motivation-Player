# Motivation Player
An MP3-like player where I can play "motivational" quotes from my friends from when I'm feeling down

# Motivation
I wanted to create this project as a way to learn how to make PCB's and design in CAD with minimal help from tutorials. I also often struggle with motivation and fall into the cyclical loop of "negative thoughts" so this project is meant to help break that if I'm having a bad day

# Features
- 128 x 64 OLED display to show information about what's being played
- A 30mm speaker with an LM386 audio amplifier to play sound at good quality
- Rotary encoder to scroll between quotes
- Potentiometer to adjust volume
- 2 Buttons to play quotes and randomize quotes
- Power switch to turn on and off the project (to save battery)
- SD card module to hold many recordings (Assuming ~2 mb per .WAV file, roughly 64 recordings on an 128 mb SD card)

# CAD Model
The enclosure for the PCB is comprised of a bottom and a lid. The two screw together with M2 screws in each of the corner (4 total).

# PCB

# Firmware
Circuit Python was used to program the project as it works best with the Raspberry Pi Pico. Libraries from Adafruit were also used to interface with the OLED. The program can only read .WAV files from the SD card, with the SD card being formatted in FAT32 and the .WAV files being mono-channel, 16-bit, 22kHz.

# Specifications

BOM
- 

Other
- Circuit Python
- Adafruit libraries
