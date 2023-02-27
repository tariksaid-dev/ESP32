import { Bluetooth } from 'expo';

export const sendBluetoothData = async (ssid, password) => {
  try {
    // Escanea y encuentra dispositivos Bluetooth cercanos
    const device = await Bluetooth.requestDeviceAsync({
      name: 'ESP32', // nombre del dispositivo
      services: ['SERVICE_UUID'], // UUID del servicio Bluetooth del ESP32
    });

    // Conecta al dispositivo
    await device.connectAsync();

    // Encuentra la característica Bluetooth correspondiente
    const characteristic = await device.getServiceAsync('SERVICE_UUID')
      .then(service => service.getCharacteristicAsync('CHARACTERISTIC_UUID'));

    // Envía datos al dispositivo
    const data = ssid + '\n' + password; // datos a enviar
    const bytes = new TextEncoder().encode(data); // convierte los datos en un arreglo de bytes
    await characteristic.writeAsync(bytes);

    // Desconecta del dispositivo
    await device.disconnectAsync();
  } catch (error) {
    console.log(error);
  }
}
