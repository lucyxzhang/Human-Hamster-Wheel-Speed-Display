#include <Encoder.h>

// Change these pin numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability
Encoder knob(5, 6);
//   avoid using pins with LEDs attached

unsigned long previousMillis = 0;
unsigned long interval = 250;  // 250 milliseconds (1/4 second)

int ledPin = 9;  // LED connected to digital pin 9

void setup() {
  pinMode(ledPin, OUTPUT);  // sets the pin as output
  Serial.begin(9600);
  //Serial.println("One Knob Encoder Test:");
}

long positionKnob = -999;
long prevKnob = -999;
signed long sp = 0;

void loop() {
  unsigned long currentMillis = millis();

  long newKnob;
  newKnob = knob.read();
  if (newKnob != positionKnob) {
    //Serial.print("Knob = ");
    //Serial.print(newKnob);
    //Serial.println();
    positionKnob = newKnob;
  }
  // if a character is sent from the serial monitor,
  // reset both back to zero.
  if (Serial.available()) {
    Serial.read();
    Serial.println("Reset knob to zero");
    knob.write(0);
  }

  // Calculate speed at a certain time interval
  if (currentMillis - previousMillis > interval) {
    sp = abs(newKnob - prevKnob) / (interval / 20);

    // Serial.println("speed");
    signed long output = sp * 4500 / (10 * 40);
    
    if (output > 8000){
      Serial.println("MAX Hamster Power!");
    }
    else{
    Serial.print(output);
    Serial.println(" Hamster Power");
    }

    if (sp <= 255) {
      analogWrite(ledPin, sp/2);  // analogRead values go from 0 to 1023, analogWrite values from 0 to 255
    } else if (sp > 255) {
      analogWrite(ledPin, 255/2);
    } else {
      analogWrite(ledPin, 0);
    }
    prevKnob = newKnob;

    previousMillis = currentMillis;
    //Serial.println("interval");
    //Serial.println(previousMillis);
  }
}
