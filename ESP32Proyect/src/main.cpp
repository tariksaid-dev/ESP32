#include <Arduino.h>
#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>
#include <ESPmDNS.h>
#include <ArduinoJson.h>

const char *ssid = "DIGIFIBRA-sZu6";
const char *password = "UybNPKTy5Z";

WebServer server(80);

const int led = 13; //??

// devuelve main page, por defecto dirección ip local
String mainPage =
  "<!DOCTYPE html> <html>\n"
  "<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n"
  "<title>ESP32</title>\n"
  "<style>html {font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n"
  "body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;} h3 {color: #444444;margin-bottom: 50px;}\n"
  ".button {display: inline-block;width: 80px;background-color: #3498db;border: none;color: white;padding: 13px 30px;text-decoration: none;font-size: 25px;margin: 0px auto35px;cursor: pointer;border-radius: 4px;}\n"
  ".button-on {background-color: #3498db;}\n"
  ".button-on:active {background-color: #2980b9;}\n"
  ".button-off {background-color: #34495e;}\n"
  ".button-off:active {background-color: #2c3e50;}\n"
  "p {font-size: 14px;color: #888;margin-bottom: 10px;}\n"
  "</style>\n"
  "</head>\n"
  "<body>\n"
  "<h1>ESP32 Proyecto Hlanz</h1>\n"
  "<h3>Modo Servidor Local</h3>\n"
  "<p>Recibir horario de Luz</p><a class=\"button button-on\" href=\"#\">LEER</a>\n";

void handleRoot()
{
  digitalWrite(led, 1);
  server.send(200, "text/html", mainPage);
  digitalWrite(led, 0);
}

// al intentar entrar en una ruta no válida, muestra el error
void handleNotFound()
{
  digitalWrite(led, 1);
  String message = "El archivo no se encuentra!\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMétodo: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArgumentos: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++)
  {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
  digitalWrite(led, 0);
}



// setup del wifi?
void setup(void)
{
  pinMode(led, OUTPUT);
  digitalWrite(led, 0);
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");

  // espera al wifi
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Conectado a ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

// mensaje en el log + ruta /inline + ????
  if (MDNS.begin("esp32"))
  {
    Serial.println("MDNS responder started");
  }

  server.on("/", handleRoot);
// ejemplo de ruta en el servidor, habría que sustiuir los parámeetros con el return de la api de precioluz.org
// y añadirlo a la ruta deseada, la cual nos redireccionara al pulsar el botón
  server.on("/inline", []()
            { server.send(200, "text/plain", "Estamos bien"); });

  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("HTTP server iniciado");
}

//runea el programa en bucle (CREO) 
void loop(void)
{
  server.handleClient();
}