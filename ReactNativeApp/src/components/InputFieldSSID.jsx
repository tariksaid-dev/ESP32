import React, { useContext } from 'react'
import { Text, TextInput, View, StyleSheet, Dimensions } from 'react-native'
import { AppContext } from '../context/AppContext.js';

const InputFieldSSID = () => {
    const { ssid, setSsid } = useContext(AppContext);

    const handleSsidChange = (text) => {
        setSsid(text);
    }

    return (
        <View style={styles.container}>
            
            <Text style={styles.label}>SSID</Text>
            <TextInput 
                placeholder='Introduce el nombre de la red' 
                style={styles.input}
                value={ssid}
                onChangeText={handleSsidChange} /> 
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        marginTop: Dimensions.get('window').height * 0.1,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 10,
    },

    label: {
        fontWeight: 'bold',
        fontSize: 28
    },
    
    input: {
        height: 40,
        width: Dimensions.get('window').width * 0.8,
        borderColor: 'black',
        borderWidth: 1,
        paddingHorizontal: 5,
        fontSize: 20,
    }, 
})

export default InputFieldSSID;