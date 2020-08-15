#!/usr/bin/env python
# coding: utf-8

# In[1]:


from socket import *
import os

def getSaldo():
    file = open("saldo.txt", "r")
    saldo = file.readline()
    file.close()

    return saldo

servidorPuerto = 12006
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
file = open("saldo.txt", "w")
file.write("2000")
print("El servidor está listo para recibir mensajes")
file.close()
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Conexión establecida con ", clienteDireccion)
    mensaje = str( conexionSocket.recv(1024), "utf-8" )
    print("Mensaje recibido de ", clienteDireccion)
    print(mensaje)
    mensaje = mensaje.upper()
    if (mensaje == "SALDO"):
        mensaje_respuesta = "Su saldo es: "+getSaldo()
    elif(mensaje[0:7] == "DEBITAR"):
        debito = mensaje[8:]
        nuevo_saldo = int(getSaldo()) - int(debito)
        if(nuevo_saldo < 0):
            mensaje_respuesta = "Saldo insuficiente"

        else:
            
            file = open("saldo.txt","w+")
            file.write(str(nuevo_saldo))
            mensaje_respuesta = "Ok"
            
    elif(mensaje[0:9] == "ACREDITAR"):
        nuevo = mensaje[9:]
        nuevo_saldo = int(getSaldo())+int(nuevo)
        file = open("saldo.txt","w+")
        file.write(str(nuevo_saldo))
        mensaje_respuesta = "nuevo saldo:" +str(nuevo_saldo)
    else:
        mensaje_respuesta = "ERROR"
       
    conexionSocket.send(bytes(mensaje_respuesta, "utf-8"))
    mensajeRespuesta = mensaje.upper()
    conexionSocket.close()
    file.close()





