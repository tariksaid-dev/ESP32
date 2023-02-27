import React from 'react'
import Constants from 'expo-constants'
import { Text, View, StyleSheet, Dimensions } from 'react-native'


const Header = () => {
    return (
        <View style={styles.header}>
            <Text 
                style={styles.header_text} 
                numberOfLines={1} 
                adjustsFontSizeToFit>Credenciales WiFi para ESP32</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    header: {
        marginTop: Constants.statusBarHeight,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'blue',
        height: Dimensions.get('window').height * 0.1
    },

    header_text: {
        fontWeight: 'bold',
        color: 'white',
        textAlign: 'center',
        fontSize: 28
    }
})

export default Header