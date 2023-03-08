import React from 'react'
import Header from './Header'
import InputFieldSSID from './InputFieldSsid'
import InputFieldPasswd from './InputFieldPasswd'
import { AppProvider } from '../context/AppContext'
import BotonModal from './BotonModal'
import { KeyboardAvoidingView } from 'react-native'
import DisplayConexion from './DisplayConexion'
import Footer from './Footer'

const Main = () => {
    return (
        <AppProvider>
            <KeyboardAvoidingView behavior='padding' style={{flex:1}}>
                <Header/>
                {/* <DisplayConexion /> */}
                <InputFieldSSID />
                <InputFieldPasswd />
                <BotonModal /> 
                <Footer />
            </KeyboardAvoidingView>
        </AppProvider>
    )
}


export default Main
