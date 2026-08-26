import board
import digitalio
import time
import random
import busio
import storage
import rotaryio
import sdcardio
from audiocore import WaveFile
from audiopwmio import PWMAudioOut as AudioOut
import displayio
from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus
import adafruit_displayio_ssd1306
import terminalio

#Setup SSD1306
displayio.release_displays()
SCL = board.GP13
SDA = board.GP12
i2c = busio.I2C(SCL, SDA)
display_bus = I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
splash = displayio.Group()
display.root_group = splash

#Setup speaker
SPEAKER_PIN = board.GP17
speaker = AudioOut(SPEAKER_PIN)

#Setup the play button
play_btn = digitalio.DigitalInOut(board.GP6)
play_btn.switch_to_input(pull = digitalio.Pull.UP)
play_btn_pressed = False

#Setup for the random button
rand_btn = digitalio.DigitalInOut(board.GP7)
rand_btn.switch_to_input(pull = digitalio.Pull.UP)
rand_btn_pressed = False

#Setup rotary encoder scroller
A_PIN = board.GP9
B_PIN = board.GP8
scroll_encoder = rotaryio.IncrementalEncoder(A_PIN, B_PIN)
last_position = scroll_encoder.posiion

#Index of the current audio to play
audio_index:int = 0
MAX_INDEX = 62

#SD card pins
SCK = board.GP2
MOSI = board.GP3
MISO = board.GP4
CS = board.GP5

#Set up SDcard
spi = busio.SPI(SCK, MOSI, MISO)
sdcard = sdcardio.SDCard(spi,CS)

#Mount SDcard file
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

#Play an audio file based on the index passed in
def play_audio(index:int):

    #Stop any audio from play if there is audio playing
    if speaker.playing:
        speaker.pause()

    try:
        wave_file = open("/sd/" + index + ".wav", "rb")
        wave = WaveFile(wave_file)
        speaker.play(wave) 
    except Exception:
        print("Error playing audio")
        print("Error: " + Exception)

#Setup texts on the display
index_text = ""
index_text_area = label.Label(terminalio.FONT, text=index_text, color=0xFFFFFF, x=28, y=15)
splash.append(index_text_area)

name_text = ""
name_text_area = label.Label(terminalio.FONT, text=name_text, color=0xFFFFFF, x=28, y=30)
splash.append(name_text)

#Update the display to show the current audio file playing/to be played
def update_display(index:int):  
    index_text_area.text = "Audio #" + index

    #Get name of person who gave quote in from a txt file
    try:
        with open("/sd/" + index + ".txt".r) as file:
            name = file.readline().strip()
            name_text_area.text = "- " + name
    except:
        name_text_area.text = "- Anonymous"


#Main loop
while True:

    #Check if the current encoder's position has changed. If it has, change the audio index
    #chosen accordingly
    position = scroll_encoder.position

    if position != last_position:
        #Get how many ticks have happened
        delta_index = position - last_position
        audio_index += delta_index

        #Make sure the index doesn't exceed the max and min index
        if audio_index < 0:
            audio_index += MAX_INDEX
        elif audio_index > MAX_INDEX:
            audio_index -= MAX_INDEX

        #Update display
        update_display(audio_index)

        #Update last position
        last_position = position

    #Check if the randomization button is pressed
    if not rand_btn.value and not rand_btn_pressed:
        rand_btn_pressed = True

        #Set the index to a random number
        audio_index = random.randint(0,MAX_INDEX)

        #Update display
        update_display(audio_index)

        #Button debounce
        time.sleep(0.2)

    elif rand_btn.value:
        rand_btn_pressed = False

    

    #Check if the play button is pressed -- inversed due to being pulled up by default
    if not play_btn.value and not play_btn_pressed:
        play_btn_pressed = True

        #Play the audio corresponding to the current index
        play_audio(audio_index)

        #Button debounce
        time.sleep(0.2)

    elif play_btn.value:
        play_btn_pressed = False

    time.sleep(0.1)

