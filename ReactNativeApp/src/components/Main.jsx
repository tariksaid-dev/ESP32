import React from 'react'
import { KeyboardAvoidingView } from 'react-native'
import Header from './Header'
import InputFieldSSID from './InputFieldSSID'
import InputFieldPasswd from './InputFieldPasswd'
import BotonModal from './BotonModal'

const Main = () => {
    return (
        <KeyboardAvoidingView // Sirve para un ligero movimiento al salir el teclado. Puedo retocar algun margen tmb. Pensar en ello
            behavior='padding'
            style={{flex:1}}>
            <Header />
            <InputFieldSSID />
            <InputFieldPasswd />
            <BotonModal />
        </KeyboardAvoidingView>
    )
}

export default Main