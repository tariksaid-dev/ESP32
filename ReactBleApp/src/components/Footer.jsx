import React from 'react'
import { Text, View, StyleSheet, Dimensions, Image } from 'react-native'


const Footer = () => {
    return(
        <View style={styles.container}>
            <Text 
                style={styles.footer_text}
                numberOfLines={1}
                adjustsFontSizeToFit>
                    by @tariksaid.dev
            </Text>
            <Image
                style={styles.img}
                source={require("../../assets/logotipoHlanzTrimmed.png")}
            />
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        display: 'flex',
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between',
        // alignContent: 'space-between',
        backgroundColor: 'blue',
        height: Dimensions.get('window').height * 0.06,
        position: 'absolute',
        bottom: 0,
        left: 0,
        right: 0,
    },

    footer_text: {
        color: 'white',
        textAlign: 'center',
        fontSize: 16,
        padding: 5
    },

    imgContainer: {
        backgroundColor: 'green'
    },

    img: {
        width: '100%',
        height: '85%',
        resizeMode: 'contain',
    }
})

export default Footer