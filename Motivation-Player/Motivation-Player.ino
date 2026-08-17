#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

//SSD1306 pins
const u_int scl = 13;
const u_int sda = 12;

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3D ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

//Rotary encoder pins 
const u_int encoder_A = 9;
const u_int encoder_B = 8;

//Play button
const u_int play_btn = 6;

//Random button
const u_int rand_btn = 7;

void setup() {
  // put your setup code here, to run once:

  //Setup the pins 
  pinMode(encoder_A, INPUT_PULLUP);
  pinMode(encoder_B, INPUT_PULLUP);
  pinMode(play_btn, INPUT_PULLUP);
  pinMode(rand_btn, INPUT_PULLUP);

  //Setup SSD1306
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

}

void loop() {
  // put your main code here, to run repeatedly:

}

//Returns a random index in the playlist
u_int random_index(){
  return 0;
}

//Plays the mp3 file based on the index passed in
void play_file(u_int index){

}
