import { useMemo, useState, useEffect, useContext } from 'react'
import { PermissionsAndroid, Platform } from 'react-native'
import { BleError, BleManager, Characteristic, Device } from 'react-native-ble-plx'

import * as ExpoDevice from 'expo-device'
import base64 from 'react-native-base64'
import { AppContext } from '../context/AppContext'

export const useBle = () => {
    // se utiliza en ScanForPeripherals
    const bleManager = useMemo(() => new BleManager(), []);
    const [allDevices, setAllDevices] = useState([]);
    const [connectedDevice, setConnectedDevice] = useState(null);


    //test para sac
    const { conectando, setConectando } = useContext(AppContext);
    const { isError, setIsError } = useContext(AppContext);


    const ESP32_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
    const ESP32_CHARACTERISTIC = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
    

    const requestAndroid31Permissions = async () => {
        const bluetoothScanPermission = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.BLUETOOTH_SCAN,
            {
                title: "Location Permission",
                message: "Bluetooth Low Energy requires Location",
                buttonPositive: "OK",
            }
        );
        const bluetoothConnectPermission = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.BLUETOOTH_CONNECT,
            {
                title: "Location Permission",
                message: "Bluetooth Low Energy requires Location",
                buttonPositive: "OK",
            }
        );
        const fineLocationPermission = await PermissionsAndroid.request(
            PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
            {
                title: "Location Permission",
                message: "Bluetooth Low Energy requires Location",
                buttonPositive: "OK",
            }
        );
        return (
            bluetoothScanPermission === "granted" &&
            bluetoothConnectPermission === "granted" &&
            fineLocationPermission === "granted"
        );
    };
  
    const requestPermissions = async () => {
        if (Platform.OS === "android") {
            if ((ExpoDevice.platformApiLevel ?? -1) < 31) {
                const granted = await PermissionsAndroid.request(
                    PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
                    {
                        title: "Location Permission",
                        message: "Bluetooth Low Energy requires Location",
                        buttonPositive: "OK",
                    }
                );
                return granted === PermissionsAndroid.RESULTS.GRANTED;
            } else {
                const isAndroid31PermissionsGranted = await requestAndroid31Permissions();
                return isAndroid31PermissionsGranted;
            }
        } else {
            return true;
        }
    };

    // Test, usa useMemo, más info en https://www.oneclickitsolution.com/blog/ble-plx-in-react-native/
    // ok
    const scanForPeripherals = () => {
        bleManager.startDeviceScan(null, {allowDuplicates: false}, async (error, device) => {
            console.log("Scanning");
            if(error) {
                bleManager.stopDeviceScan();
                console.log("Error");
            }
            console.log("Traza 1: ", device.localName, device.name);
            if(device.localName == "ESP32" || device.name == "ESP32") {
                setAllDevices((prevDevices) => [...prevDevices, device]);
                bleManager.stopDeviceScan();
            }
        });
    };

    //test
    const connectToDevice = async (deviceId) => {
        try {
            const device = await bleManager.connectToDevice(deviceId);
            console.log(`Connected to device ${device.name}`);
            setConnectedDevice(device);
            await device.discoverAllServicesAndCharacteristics();
            console.log(connectedDevice, "CONNECTED DEVICEEEEEEEEED");
            return device;
        } catch (error) {
            console.error("Error connecting to device", error);
            throw error;
        }
    };

    // useEffect(() => {
    //     console.log(connectedDevice, "USE EFFECT -----------------------"); // El estado se ha actualizado, se puede usar aquí
    //   }, [connectedDevice]);

    const disconnect = async () => {
        if (connectedDevice) {
          try {
            await bleManager.cancelDeviceConnection(connectedDevice.id);
            setConnectedDevice(null);
            console.log("desconectado correctamente")
          } catch (error) {
            console.error("Error disconnecting from device", error);
            throw error;
          }
        }
    };

    const sendData = async (device, param1, param2) => {
        console.log(device)
        
        try {
          const service = await device.discoverService(ESP32_UUID);
          const characteristic = await device.discoverCharacteristic(ESP32_CHARACTERISTIC);
      
          const value = new TextEncoder().encode(`${param1},${param2}`);
          await characteristic.writeWithoutResponse(value);
      
          console.log(`Successfully sent params ${param1},${param2}`);
        } catch (error) {
          console.error("Error sending params", error);
          throw error;
        }
      };

      const handleSendData = async () => {
        if (connectedDevice) {
            await sendData(connectedDevice, "param1", "param2");
        } else {
            console.error("Device not connected")
        }
      }


    //   TEST
    const sac = async (ssid, password) => {
        setConectando(true);
        setIsError(false);
        if(await requestPermissions()) {
            console.log("Tengo permisos");
        } else {
            setConectando(false);
            setIsError(true); // podría crear otro estado para indicar que no hay permisos y ser más concreto
            console.log("Sin permisos");
        }
        bleManager.stopDeviceScan();
        bleManager.startDeviceScan(null, {allowDuplicates: false}, async (error, device) => {
            // console.log("Scanning...");
            // console.log(device);
            if(error) {
                console.log(error);
                setConectando(false);
                setIsError(true);
                return
            }

            if (device.name ==="ESP32") {
                console.log("Conectando al ESP32")
                bleManager.stopDeviceScan();

                device.connect()
                    .then((device) => {
                        setConectando(false);
                        console.log("Descubriendo servicios");
                        return device.discoverAllServicesAndCharacteristics()
                    })
                    .then((device) => {
                        console.log(device.id);

                        const ssidEncoded = base64.encode(ssid);
                        const passwdEncoded = base64.encode(password);

                        device.writeCharacteristicWithoutResponseForService(ESP32_UUID, ESP32_CHARACTERISTIC, ssidEncoded);
                        device.writeCharacteristicWithoutResponseForService(ESP32_UUID, ESP32_CHARACTERISTIC, passwdEncoded);
                    })
                    .catch((error) => {
                        setIsError(true);
                        console.log(error);
                    });
                device.cancelConnection() // test, puede fallar
                    .then(console.log("Desconexion realizada con éxito"));
            }
        })
    }

    return { 
        requestPermissions,
        scanForPeripherals,
        allDevices,
        connectToDevice,
        connectedDevice,
        disconnect,
        sendData,
        sac
    };
}