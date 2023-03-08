import React, { createContext, useState } from 'react'

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
    const [ssid, setSsid] = useState('');
    const [password, setPassword] = useState('');
    const [devices, setDevices ] = useState([]);
    const [allDevices, setAllDevices] = useState([]);
    
    const [conectando, setConectando] = useState(false);
    const [isError, setIsError] = useState(false);

    return (
        <AppContext.Provider 
            value= {{ ssid, setSsid, password, setPassword, devices, setDevices, allDevices, setAllDevices, conectando, setConectando, isError, setIsError }}>
                {children}
        </AppContext.Provider>
    );
};