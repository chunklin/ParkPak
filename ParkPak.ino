#include <math.h>
#include "DHT.h"
#define DHTTYPE DHT11
#define DHTPIN 2
#define UVPIN 4

#define lightS A2
#define soundS A1
#define tempS A0
#define soilS 1

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(115200);
  pinMode(tempS, INPUT);
  pinMode(lightS, INPUT);
  pinMode(soundS, INPUT);
  pinMode(UVPIN, INPUT);
  pinMode(soilS, INPUT);
  dht.begin();
}

void loop()
{
  while (true)
  {
start:
    // DHT11 Environment Sensor Code
    float h = dht.readHumidity();
    // Read temperature as Celsius (the default)
    float t = dht.readTemperature();
    
    // Check if any reads failed and exit early (to try again).
    if (isnan(h) || isnan(t)) {
      Serial.println(F("Failed to read from DHT sensor!"));
      goto start;
    }
    // Compute heat index in Celsius (isFahreheit = false)
    float hic = dht.computeHeatIndex(t, h, false);
    
    //...................................NEXT SEGMENT........................................//
    int uvVal = analogRead(UVPIN);
    int lightVal = analogRead(lightS);
    int soundVal = analogRead(soundS);
    int t2 = analogRead(tempS);
    int soil = analogRead(soilS);
    float t1 = 1023.0 / t2 - 1.0;
    t1 = t1 * 100000;
    float temper = 1.0 / (log(t1 / 100000) / 4275 + 1 / 298.15) - 273.15;
    float UVindex= uvVal * (5.0 / 1023.0);

    /*
    Output Variables:
    h: humidity value
    hic: Heat Index in celsius from dht11
    temper: heat value from temp sensor

    */
    //...................................NEXT SEGMENT........................................//
    
    Serial.print(temper); //4
    Serial.print("|" );
    Serial.print(h);
    Serial.print("|" );
    Serial.print(hic);
    Serial.print("|" );
    Serial.print(lightVal); //3
    Serial.print("|" );
    Serial.print(soundVal); //3
    Serial.print("|" );
    Serial.print(UVindex);
    Serial.print("|");
    Serial.print(soil);
    Serial.println(""); //5
    
    delay(500);
  }
}
