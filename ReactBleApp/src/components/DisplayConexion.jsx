import React, { useContext, useState, useEffect} from 'react'
import FontAwesome from 'react-native-vector-icons/MaterialCommunityIcons'
import { Text, TextInput, View, StyleSheet, Dimensions, TouchableOpacity, ActivityIndicator } from 'react-native'
import { AppContext } from '../context/AppContext'
import { useBle } from "../services/bluetooth.js";

const DisplayConexion = () => {
    const { 
        requestPermissions, 
        scanForPeripherals, 
        allDevices,
        connectToDevice,
        connectedDevice,
        disconnect } = useBle();

    const { devices, setDevices } = useContext(AppContext);
    const [isScanning, setIsScanning] = useState(false);
    const [isDeviceFound, setIsDeviceFound] = useState(false);

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

    useEffect(() => {
        console.log(allDevices, "traza uno");
        setDevices(allDevices);
        if(allDevices.some(device => device.name === "ESP32")) {
            setIsScanning(false);
            setIsDeviceFound(true);
            connectToDevice(allDevices.find(device => device.name === "ESP32").id);
        }
    }, [allDevices]);


    const handleDisconnect = async () => {
        await disconnect();
        setIsDeviceFound(false);
    }

    return (
        <View style={styles.container}>
            <Text>
                {isDeviceFound ? (
                    <FontAwesome 
                        name="bluetooth-connect" 
                        size={40} />
                    ) : (
                    isScanning ? (
                        <ActivityIndicator
                            size='small'
                            color={"#0000ff"} />
                    ) : (
                        <FontAwesome 
                            name='bluetooth-off'
                            size={40} />
                    )
                )}
            </Text>
            <Text>
                Sin conexión
            </Text>
            {/* {isDeviceFound ? (
                <TouchableOpacity 
                    style={styles.btn}
                    onPress={handleDisconnect }>
                    <Text style={styles.btnText}>
                        Desconectar
                    </Text>
                </TouchableOpacity>
            ) : (
                <TouchableOpacity 
                    style={styles.btn}
                    onPress={scanForDevices }>
                    <Text style={styles.btnText}>
                        Buscar dispositivo
                    </Text>
                </TouchableOpacity>
            )} */}
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