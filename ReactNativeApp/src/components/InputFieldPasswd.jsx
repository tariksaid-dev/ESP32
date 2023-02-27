import React, {useState} from 'react'
import FontAwesome from 'react-native-vector-icons/Ionicons'
import { Text, TextInput, View, StyleSheet, Dimensions, TouchableOpacity, KeyboardAvoidingView } from 'react-native'


const InputFieldPasswd = () => {
    const [showPassword, setShowPassword] = useState(false);

    return (

        <View style={styles.container}>
            <Text style={styles.label}>Password</Text>
            <View style={styles.container2}>
            <TextInput 
                placeholder='Introduce la contraseña' 
                style={styles.input} 
                secureTextEntry={!showPassword}/>
            <TouchableOpacity 
                onPress={() => setShowPassword(!showPassword)}>
                <Text style={{paddingHorizontal: 5}}>
                    {showPassword ? <FontAwesome name='eye-outline' size={20}/> : 
                    <FontAwesome name='eye-off-outline' size={20}/>}
                </Text>
            </TouchableOpacity>
            </View>
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
        fontSize: 28,
    },

    container2: {
        flexDirection: 'row',
        alignItems: 'center',
        borderWidth: 1,
        marginBottom: 50
    },
    
    input: {
        height: 40,
        width: Dimensions.get('window').width * 0.8 -30,
        paddingHorizontal: 5,
        fontSize: 20,
    }, 
})

export default InputFieldPasswd;