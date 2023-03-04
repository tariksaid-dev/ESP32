import React from 'react'
import Header from './Header'
import InputFieldSSID from './InputFieldSsid'
import InputFieldPasswd from './InputFieldPasswd'
import { AppProvider } from '../context/AppContext'
import BotonModal from './BotonModal'
import { KeyboardAvoidingView } from 'react-native'
import BotonTest from './BotonTest'
import DisplayConexion from './DisplayConexion'

const Main = () => {
    return (
        <AppProvider>
            <KeyboardAvoidingView behavior='padding' style={{flex:1}}>
                <Header/>
                <DisplayConexion />
                <InputFieldSSID />
                <InputFieldPasswd />
                <BotonModal /> 
                {/* <BotonTest /> */}
            </KeyboardAvoidingView>
        </AppProvider>
    )
}


export default Main
