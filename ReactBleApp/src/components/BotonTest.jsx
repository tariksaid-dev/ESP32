import React, { useState, useContext, useEffect } from "react";
import { TouchableOpacity, Text, View, StyleSheet, FlatList } from "react-native";
import { useBle } from "../services/bluetooth.js";
import DeviceModal from "./ModalBluetooth.jsx";

const BotonTest = () => {
    const {  requestPermissions, scanForPeripherals, allDevices } = useBle();


    useEffect(() => {
        scanForPeripherals();
    }, []);

    useEffect(() => {
        console.log(allDevices);
    }, [allDevices]);
    // const handlePress = async () => {
    //     const granted = await ble.requestPermissions();
    //     console.log("Permission granted?", granted);
    // };

    const [devices, setDevices] = useState([]);
    // const handleScanForPeripherals = async () => {
    //     const allDevices = await ble.scanForPeripherals();
    //     setDevices(allDevices);
    //     console.log(devices);
    // };

    const scanForDevices = async () => {
        const isPermissionEnabled = await requestPermissions();
        console.log(isPermissionEnabled);
        if (isPermissionEnabled) {
            scanForPeripherals();
        } else {
            console.log("No hay permisos")
        }
    } 


    // const [isModalVisible, setIsModalVisible] = useState(false);
    // const hideModal = () => {
    //     setIsModalVisible(false);
    // }
    // const openModal = () => {
    //     scanForDevices();
    //     setIsModalVisible(true);
    // }

    // const scanForDevices = async() => {
    //     const isPermissionEnabled = await requestPermissions();
    //     if(isPermissionEnabled) {
    //         scanForPeripherals();
    //     }
    // };

    return (
        <View style={styles.contenedor}>
            <TouchableOpacity
                onPress={{}}
                style={styles.btn}>
                    <Text style={styles.btnModalText}>
                        Probar
                    </Text>
            </TouchableOpacity>
            <TouchableOpacity
                style={styles.btn}
                onPress={scanForDevices}>
                <Text style={styles.btnModalText}>
                    Scan
                </Text>
            </TouchableOpacity>
            <Text></Text>
        </View>
    )
}

export default BotonTest

const styles = StyleSheet.create ({
    contenedor: {
        justifyContent: 'center',
        alignItems: 'center',
        // marginTop: 60
        marginTop: 20
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
        fontSize: 30,
        color: 'white',
        fontWeight: 'bold'
    },

    ventanaModal: {
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'white',
        marginVertical: 180,
        borderRadius: 10,
        elevation: 10,
    },

    contenedorModalText: {
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20
    },

    txtModal: {
        fontSize: 24,
        textAlign: 'center',
        // margin: 20
    },

    contenedorModalBtn: {
        justifyContent: 'center',
        alignItems: 'center',
        borderWidth: 1,
        borderRadius: 10,
        padding: 6,
        backgroundColor: '#2196F3',
        marginTop: 20, 
        elevation: 6
    },

    btnModalText: {
        color: 'white',
        fontSize: 24,
    }
})