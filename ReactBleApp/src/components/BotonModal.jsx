import { useState, useContext, useEffect } from "react";
import { TouchableOpacity, Text, View, StyleSheet, ActivityIndicator } from "react-native";
import Modal from "react-native-modal";
import { AppContext } from "../context/AppContext.js";
import { useBle } from "../services/bluetooth.js";
import { Pulse } from "react-native-animated-spinkit";


const BotonModal = () => {
    const { sendData, sac } = useBle();

    const { devices, setDevices, allDevices, setAllDevices } = useContext(AppContext);

    
    // DataContext
    const { ssid } = useContext(AppContext);
    const { password } = useContext(AppContext);

    // Manejo del modal
    const [isModalVisible, setModalVisible] = useState(false);

    const { conectando } = useContext(AppContext);
    const { isError } = useContext(AppContext);

    // Manejo de la data
    const [isSendingData, setSendingData] = useState(false);

    const toggleModal = () => {
        setModalVisible(!isModalVisible);
    };

    const handleSendData = async () => {
        console.log(allDevices)
        // setDevices(allDevices);
        try {
          await sendData(devices ,"aa", "bb");
        } catch (error) {
          console.error("Error sending data", error);
        }
    };

    useEffect(() => {
        console.log(conectando);
    }, [conectando]);

    const handleOnPress = async () => {
        sac(ssid, password);
        toggleModal();
    }

    useEffect(() => {
        console.log(isError);
    }, [isError])

  return (
    <View style={styles.contenedor}>
        <TouchableOpacity
            style={styles.btn}
            onPress={handleOnPress}>
                <Text style={styles.btnText}>
                    ENVIAR
                </Text>
        </TouchableOpacity>
        <Modal 
            isVisible={isModalVisible}
            onBackdropPress={toggleModal}
            style={styles.ventanaModal}>
            <View style={styles.contenedorModalText}>
                {conectando ? (
                    <View style={styles.contenedorAnimacion} >
                        <Pulse
                            size={110}
                            color="blue" />
                        <Text
                            style={styles.txtModal}>
                            Enviando...
                        </Text>
                    </View>
                ) : isError ? (
                        <Text style={styles.txtConfirm}>
                            Hubo un error
                        </Text>
                ) : (
                    <Text style={styles.txtConfirm}>
                        Tus credenciales han sido enviadas correctamente.
                    </Text>
                )}

                </View>
            <View style={styles.contenedorModalBtn}>
            <TouchableOpacity
                style={styles.btnModal} 
                onPress={toggleModal}>
                <Text 
                    style={styles.btnModalText}>
                    CERRAR
                </Text>
            </TouchableOpacity>
            </View>
      </Modal>
    </View>
  );
}

export default BotonModal;

const styles = StyleSheet.create ({
    contenedor: {
        justifyContent: 'center',
        alignItems: 'center',
        marginTop: 60
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
        justifyContent: 'space-around',
        flexDirection: 'column',
        backgroundColor: 'white',
        marginVertical: '55%',
        borderRadius: 10,
        elevation: 10,
        // backgroundColor: 'yellow'
    },

    contenedorModalText: {
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20,
        // backgroundColor: 'green',
        height: '40%'
    },

    txtModal: {
        fontSize: 24,
        textAlign: 'center',
        marginTop: 40,
    },

    contenedorModalBtn: {
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 10,
        padding: 6,
        backgroundColor: '#2196F3',
        marginTop: 30,
        
    },

    btnModalText: {
        color: 'white',
        fontSize: 24,
        fontWeight: 'bold'
    },

    btnModal: {
        backgroundColor: '#2196F3',
        padding: 3,
    },

    txtConfirm: {
        fontSize: 25,
        textAlign: 'center',
    },

    contenedorAnimacion: {
        marginTop: 32
    }

})