import React, { useContext, useState, useEffect} from 'react'
import FontAwesome from 'react-native-vector-icons/MaterialCommunityIcons'
import { Text, TextInput, View, StyleSheet, Dimensions, TouchableOpacity } from 'react-native'
import { AppContext } from '../context/AppContext'
import { useBle } from "../services/bluetooth.js";

const DisplayConexion = () => {
    const { 
        requestPermissions, 
        scanForPeripherals, 
        allDevices,
        connectToDevice } = useBle();

    const [devices, setDevices] = useState([]);
    const [isScanning, setIsScanning] = useState(false);
    const [connectedDevice, setConnectedDevice] = useState(null); 

    const scanForDevices = async () => {
        const isPermissionEnabled = await requestPermissions();
        console.log(isPermissionEnabled);
        if (isPermissionEnabled) {
            scanForPeripherals();
            setIsScanning(true);
        } else {
            console.log("No hay permisos")
        }
    } 

    //test
    useEffect(() => {
        console.log(allDevices);
        setDevices(allDevices);
        if(allDevices.some(device => device.name === "ESP32")) {
            setIsScanning(false);
            scanForPeripherals(false);

            // test
            const device = allDevices.find((device) => device.name === "ESP32");
            connectToDevice(device.id).then((connectedDevice) => {
                setConnectedDevice(connectedDevice);
            });
        }
    }, [allDevices]);

    return (
        <View style={styles.container}>
            <Text>
                <FontAwesome
                    name={isScanning ? "bluetooth-connect" : "bluetooth-off"}
                    size={40}/>
            </Text>
            <TouchableOpacity 
                style={styles.btn}
                onPress={scanForDevices }>
                <Text style={styles.btnText}>
                    Buscar dispositivo
                </Text>
            </TouchableOpacity>
        </View>
    )
}

const styles = StyleSheet.create({

    container: {
        marginTop: 5,
        marginHorizontal: 25,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexDirection: 'row',
        // gap: 10,
        
    },

    btn: {
        backgroundColor: '#2196F3',
        padding: 10,
        shadowColor: '#000',
        shadowOffset: {
            width: 3,
            height: 2,
        },
        borderRadius: 10,
        shadowOpacity: 0.5,
        shadowRadius: 1,
        elevation: 10,
    },

    btnText: {
        fontSize: 12,
        color: 'white',
        fontWeight: 'bold'
    },
})

export default DisplayConexion;