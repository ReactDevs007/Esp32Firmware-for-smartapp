#include "WiFi.h"
#include <HTTPClient.h>
const char* ssid ="TheCottages";
const char* password="Excel3rate";
void setup()
{
    delay(1000);
    WiFi.mode(WIFI_OFF);    
    Serial.begin(115200);
    delay(1000);
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid,password);
    while (WiFi.status() != WL_CONNECTED) {
      delay(1000);
      Serial.println("Connecting to Wifi....");
    }
    // Set WiFi to station mode and disconnect from an AP if it was previously connected
    //WiFi.mode(WIFI_STA);
    //WiFi.disconnect();
    //delay(100);
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
    Serial.println("Setup done");
}

void loop()
{
    Serial.println("scan start");

    if ((WiFi.status() == WL_CONNECTED)) {
      HTTPClient http;
      http.begin("http://18.219.209.163:3000/schedule/getdata");
      //http.begin("http://18.219.209.163:3000/light");
     
      int httpCode = http.GET();
      if (httpCode > 0) {
        String payload = http.getString();
        Serial.println(httpCode);
        Serial.println(payload);
      }
      else {
        Serial.println("Error  on HTTP request");
      }
      http.end();
    }
    Serial.println("");
    // Wait a bit before scanning again
    delay(5000);
}