import React, { createContext, useState } from 'react'

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
    const [ssid, setSsid] = useState('');
    const [password, setPassword] = useState('');

    return (
        <AppContext.Provider 
            value= {{ ssid, setSsid, password, setPassword }}>
                {children}
        </AppContext.Provider>
    );
};