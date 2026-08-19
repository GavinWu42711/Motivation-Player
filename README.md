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
The enclosure for the PCB is comprised of a bottom and a lid. The two screw together with M2 screws in each of the corner (4 total). All the parts were designed using Fusion.

**Lid**
<img width="1235" height="688" alt="image" src="https://github.com/user-attachments/assets/1619e5f0-63c2-47e4-b9b9-c8af7acd143e" />

**Bottom**
<img width="1117" height="646" alt="image" src="https://github.com/user-attachments/assets/74cb35e4-7267-4ea0-a749-18674b72be84" />

<img width="1132" height="602" alt="image" src="https://github.com/user-attachments/assets/a363e96f-6474-44a3-a970-0f764e46f399" />

**Fully Assembled**
<img width="982" height="686" alt="image" src="https://github.com/user-attachments/assets/22b6de31-671b-4b74-b46c-ea86d6ed83f6" />

*Some parts such as the switch, speaker, and potentiometer are slightly off due to not having models for the ones to be used in the project. The placeholders are a way to show proof of concept*

# PCB
The PCB was designed using KiCAD. All the parts were chosen to be through hole instead of surface mount for easier soldering.

**Schematic**
<img width="1089" height="576" alt="image" src="https://github.com/user-attachments/assets/d42606b7-10cd-4344-b66e-1fedce215d7b" />

**PCB**
<img width="1075" height="660" alt="image" src="https://github.com/user-attachments/assets/264b83c2-f9cf-4196-993b-98ba599b7f30" />

*C5 is supposed to be a non-polarized capacitor*

# Firmware
Circuit Python was used to program the project as it works best with the Raspberry Pi Pico. Libraries from Adafruit were also used to interface with the OLED. The program can only read .WAV files from the SD card, with the SD card being formatted in FAT32 and the .WAV files being mono-channel, 16-bit, 22kHz.

The "lib" folder in the "Firmware" folder contains the library files that need to be uploaded to the Pi Pico in addition to the code and Circuit Python.

# BOM
- 
