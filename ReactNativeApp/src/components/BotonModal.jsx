import React, { useState } from "react";
import { TouchableOpacity, Text, View, StyleSheet, Dimensions } from "react-native";
import Modal from "react-native-modal";

function BotonModal() {
  const [isModalVisible, setModalVisible] = useState(false);

  const toggleModal = () => {
    setModalVisible(!isModalVisible);
  };

  return (
    <View style={styles.contenedor}>
        <TouchableOpacity
            style={styles.btn}
            onPress={toggleModal} >
                <Text style={styles.btnText}>
                    ENVIAR
                </Text>
        </TouchableOpacity>
        <Modal 
            isVisible={isModalVisible}
            onBackdropPress={toggleModal}
            style={styles.ventanaModal}>
            <View style={styles.contenedorModalText} >
                <Text style={styles.txtModal}>
                    Tus credenciales han sido enviadas correctamente. Espera mientras el ESP32 se intenta conectar...
                </Text>
            </View>

            <View style={styles.contenedorModalBtn}>
            <TouchableOpacity
                style={styles.btnModal} 
                onPress={toggleModal}>
                <Text 
                    style={styles.btnModalText}>
                    Cerrar
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
        justifyContent: 'center',
        backgroundColor: 'white',
        marginVertical: 180,
        borderRadius: 10,
        elevation: 10,
    },

    contenedorModalText: {
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20
    },

    txtModal: {
        fontSize: 24,
        textAlign: 'center',
        // margin: 20
    },

    contenedorModalBtn: {
        justifyContent: 'center',
        alignItems: 'center',
        borderWidth: 1,
        borderRadius: 10,
        padding: 6,
        backgroundColor: '#2196F3',
        marginTop: 20, 
        elevation: 6
    },

    btnModalText: {
        color: 'white',
        fontSize: 24,
    }
})
