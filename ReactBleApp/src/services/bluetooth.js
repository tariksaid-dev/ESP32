import { useMemo, useState } from 'react'
import { PermissionsAndroid, Platform } from 'react-native'
import { BleError, BleManager, Characteristic, Device } from 'react-native-ble-plx'

import * as ExpoDevice from 'expo-device'
import base64 from 'react-native-base64'

export const useBle = () => {
    // se utiliza en ScanForPeripherals
    const bleManager = useMemo(() => new BleManager(), []);
    const [allDevices, setAllDevices] = useState([]);
    const [connectedDevice, setConnectedDevice] = useState(null);

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
            return device
        } catch (error) {
            console.error("Error connecting to device", error);
            throw error;
        }
    };

    return { 
        requestPermissions,
        scanForPeripherals,
        allDevices,
        connectToDevice,
        connectedDevice
    };
}