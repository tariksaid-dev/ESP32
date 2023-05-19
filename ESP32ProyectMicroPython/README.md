# ESP32 MicroPython controller

:::info
La versión de MicroPython instalada en esta placa ESP32 es la v1.19.1, la cuál se puede encontrar [aqui](https://micropython.org/download/esp32/).
:::

El objetivo del proyecto es, mediante una placa ESP32, ser capaz de recibir información sobre el PVPC (precio voluntario para el pequeño consumidor) de la luz de manera diaria, y en base a dichos datos establecer un uso de la energía eficiente, limitando las horas en las que ciertos aparatos están conectados mediante una interfaz web, dónde se nos permite elegir distintas horas para dicho fin. 

Cabe recalcar qué, en la actualidad, tanto la web, como la lógica y los servicios, están implementados directamente en la placa, por lo que se nos presentan ciertos problemas de almacenamiento, así que la web presenta diversas limitaciones. En un futuro, se podría implementar tanto los servicios como la web en un servidor remoto (por ejemplo, en Vercel) de modo que la placa simplemente hiciera llamadas a los mismos, y solo tendríamos que preocuparnos de las funcionalidades relacionadas con el control del voltaje.

## Estableciendo conexión

En la memoria de la placa hay almacenado un archivo de texto llamado 'credentials.txt'. El código establecido en el archivo de arranque de la placa contiene la lógica para conectarse, utilizando **la primera línea como SSID** y **la segunda línea como password**. 

De modo que primero intentará conectarse con dichos datos, y en caso de no lograrlo, **vaciará el archivo completamente**, eliminando su contenido y entrando en modo BLE.

BLE son las siglas de Bluetooth Low Energy, un bluetooth el cuál consume extremadamente poca energía. Paralelamente a este proyecto, se ha creado una app móvil la cuál establece conexión a la placa **con este software instalado** (esto es importante, ya que la conexión se realiza mediante una UUID arbitraria que se ha asignado en la ESP32), de modo que sea posible pasarle la SSID y la contraseña sin necesidad de editar el archivo 'credentials.txt' de forma manual. 

:::note
Actualmente, las funcionalidades de la placa no inician si no es capaz de establecer al menos una conexión Wifi. Es posible cambiar esto fácilmente, por ejemplo escribiendo un código en el archivo de credenciales que nos permitiera hacer bypass de esta protección.
:::

## Abriendo interfaz web

La web es accesible mediante la IP a la cuál la placa está conectada. Es decir, si conectamos la placa a una red cuya dirección es 192.168.1.1, escribir dicho valor en nuestro navegador, nos llevaría a la interfaz, dónde podemos ver las distintas horas y modos disponibles.

## Modos de uso

La placa dispone de tres modos de uso:

- Automático: Selecciona las 

- Semi-automático: 

- Manual: 