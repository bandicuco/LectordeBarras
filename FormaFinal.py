from barcode import EAN13
from barcode.writer import ImageWriter
from random import randint
from tkinter import *
from PIL import Image, ImageTk
import cv2
import os
import imutils
from pyzbar import pyzbar

def InicioSesión():
    global ventIni
    ventIni = Tk()
    ventIni.title("Inicio_Sesion")
    ventIni.geometry("540x960")

    imagen5=PhotoImage(file='Images/P1_mainingresar.png')
    fondo4=Label(image=imagen5, text="inicio_sesion")
    fondo4.place(x=0,y=0,relheight=1,relwidth=1)
    
    bVolver3 = PhotoImage(file='Images/P1_volverbttn.png')
    btVolver3 = Button(ventIni, text='Volver', image=bVolver3, height="51", width="51", command=volver3)
    btVolver3.place(x=42.3, y=43.8)

    bScan = PhotoImage(file='Images/P1_escanerbttn.png')
    btScan = Button(ventIni, text='Escanear', image=bScan, height="221", width="204", command=transicion2)
    btScan.place(x=170, y=180)

    ventIni.mainloop()

def registro():
    global ventReg, EntryNombre, EntryApellido, EntryContraseña
    ventReg = Tk()
    ventReg.title("Nuevo_Registro")
    ventReg.geometry("540x960")

    imagen2=PhotoImage(file='Images/REGISTRO_pag.png')
    fondo1=Label(image=imagen2, text="Inicio")
    fondo1.place(x=0,y=0,relheight=1,relwidth=1)

    icono = PhotoImage(file='Images/LOGO_PEQUEÑO.png')
    ventReg.iconphoto(True, icono)

    EntryNombre = Entry(ventReg, font = "Arial 20")
    EntryNombre.place(x=45.2, y=239.7,relheight=0.04,relwidth=0.8)
    EntryApellido = Entry(ventReg, font = "Arial 20")
    EntryApellido.place(x=45.2, y=355.3,relheight=0.04,relwidth=0.8)
    EntryContraseña = Entry(ventReg, font = "Arial 20")
    EntryContraseña.place(x=45.2, y=470.9,relheight=0.04,relwidth=0.8)

    bVolver1 = PhotoImage(file='Images/VOLVER_bttn.png')
    btVolver1 = Button(ventReg, text='Volver', image=bVolver1, height="51", width="51", command=volver1)
    btVolver1.place(x=42.3, y=43.8)

    bCrear = PhotoImage(file='Images/CREARCUENTA_bttn.png')
    btCrear = Button(ventReg, text='Crear_Cuenta', image=bCrear, height="50", width="216", command=RegistroCompletado)
    btCrear.place(x=36.4, y=564.9)

    bCancelar = PhotoImage(file='Images/CANCELAR_bttn.png')
    btCancelar = Button(ventReg, text='Cancelar', image=bCancelar, height="50", width="216", command=volver1)
    btCancelar.place(x=287.6, y=564.9)

    ventReg.mainloop()

def RegistroCompletado():
    global nombre,apellido,a
    nombre=EntryNombre.get()
    apellido=EntryApellido.get()
    contraseña=EntryContraseña.get()
    if len(nombre)==0 or len(apellido)==0 or len(contraseña)==0:
        texto1 = Label(ventReg, text="Complete todos los aspectos", font = "Arial 16")
        texto1.place(x=45.2, y=520,relheight=0.03)
    else:
        data.append(nombre)
        data.append(apellido)
        data.append(contraseña)

        a=randint(100000000000,999999999999)
        a=str(a)

        f = open(f"{OutFolderUser}/{a}.txt ", "w")
        f.write(nombre + ',')
        f.write(a + ',')
        f.write(apellido + ',')
        f.write(contraseña)
        f.close()

        print(a)
        with open(f"{OutFolderBarcode}/{a}.png ", "wb") as f:
            EAN13(a, writer=ImageWriter()).write(f)
        transicion()

def Generado():
    global nombre, ventGen, imagen4
    ventGen = Tk()
    ventGen.title("Registro_Generado")
    ventGen.geometry("540x960")

    imagen3=PhotoImage(file='Images/P2_principal.png')
    fondo2=Label(image=imagen3, text="Verificado")
    fondo2.place(x=0,y=0,relheight=1,relwidth=1)

    labelI = Label(ventGen)
    labelI.place(x=5.5, y=200)
    imagen4 = cv2.imread(f"{OutFolderBarcode}/{a}.png")
    imagen4 = Image.fromarray(imagen4)
    imagenT = ImageTk.PhotoImage(image=imagen4)
    labelI.configure(image=imagenT)

    bGuardar = PhotoImage(file='Images/P2_guardarbttn.png')
    btGuardar = Button(ventGen, text='Guardar', image=bGuardar, height="51", width="453", command=descarga)
    btGuardar.place(x=38, y=520)

    bSalirN = PhotoImage(file='Images/P2_salirbttn.png')
    btSalirN = Button(ventGen, text='Salir', image=bSalirN, height="51", width="453", command=volver2)
    btSalirN.place(x=38, y=600)
    
    ventGen.mainloop()

def IniScan():
    global ventScan, barcodeData
    while(True):
        ret, frame = captura.read()
        frameCapt = frame.copy()
        frame = imutils.resize(frame, width=645, height=480)

        if ret==True:
            cv2.line(frame,(30,80),(130,80),(0,0,150),5)
            cv2.line(frame,(30,80),(30,120),(0,0,150),5)
            cv2.line(frame,(585,80),(485,80),(0,0,150),5)
            cv2.line(frame,(585,80),(585,120),(0,0,150),5)
            cv2.line(frame,(30,400),(130,400),(0,0,150),5)
            cv2.line(frame,(30,400),(30,360),(0,0,150),5)
            cv2.line(frame,(585,400),(485,400),(0,0,150),5)
            cv2.line(frame,(585,400),(585,360),(0,0,150),5)
            barcodes = pyzbar.decode(frame)
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                barcodeData = barcode.data.decode("utf-8")
                barcodeData=int(barcodeData)
                barcodeData=barcodeData//10 
                barcodeData=str(barcodeData)
                barcodeType = barcode.type
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

                usuarios = os.listdir(UserCheck)
                UBarcode = []
                for lis in usuarios:
                    Usuario = lis
                    Usuario = Usuario.split('.')
                    UBarcode.append(Usuario[0])
                    if barcodeData in UBarcode:
                        print("Barcode encontrado en la Data")
                        UserEncontrado = open(f"{OutFolderUser}/{barcodeData}.txt","r")
                        infoUser = UserEncontrado.read().split(',')
                        nombreUser = infoUser[0]
                        apellidoUser = infoUser[2]
                        print("Nombre: ",nombreUser)
                        print("Apellido: ",apellidoUser)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break   
        else:
            break

        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)

        lblVideo.configure(image=img)
        lblVideo.image = img
    else:
        captura.release()

def destruirPrin(): 
    ventPrin.destroy()

def transicion():
    ventReg.destroy()
    Generado()

def transicion2():
    global captura, lblVideo, ventScan
    ventIni.destroy()
    ventScan = Tk()
    ventScan.title("Escanear_Codigo_de_Barras")
    ventScan.geometry("648x480")

    lblVideo = Label(ventScan)
    lblVideo.place(x=0, y=0)

    captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    captura.set(3, 645)
    captura.set(4, 480)

    IniScan()


def botonReg():
    ventPrin.destroy()
    registro()

def botonIni():
    ventPrin.destroy()
    InicioSesión()

def volver1(): 
    ventReg.destroy()
    INICIO()

def volver2(): 
    ventGen.destroy()
    INICIO()

def descarga(): 
    ventGen.destroy()
    INICIO()

def volver3(): 
    ventIni.destroy()
    INICIO()

def volver4(): 
    ventPerf.destroy()
    INICIO()

def INICIO():
    global ventPrin, OutFolderBarcode, OutFolderUser, UserCheck, data, OutFolderScan
    ventPrin = Tk()
    ventPrin.title("Proyecto_Codigo_De_Barras")
    ventPrin.geometry("540x960")

    imagen1=PhotoImage(file='Images/FONDO_GENERADOR.png')
    fondo=Label(image=imagen1, text="Inicio")
    fondo.place(x=0,y=0,relheight=1,relwidth=1)

    icono = PhotoImage(file='Images/LOGO_PEQUEÑO.png')
    ventPrin.iconphoto(True, icono)

    OutFolderBarcode='Data/Barcode'
    OutFolderUser = 'Data/User'
    UserCheck = 'Data/User/'
    data=[]

    bReg = PhotoImage(file='Images/REGISTRO_bttn.png')
    btReg = Button(ventPrin, text='Registro', image=bReg, height="102", width="453", command=botonReg)
    btReg.place(x=43.5, y=564.5)

    bIni = PhotoImage(file='Images/INGRESAR_BTTN.png')
    btIni = Button(ventPrin, text='Inicio Sesión', image=bIni, height="102", width="453", command=botonIni)
    btIni.place(x=43.5, y=429)

    bSalir = PhotoImage(file='Images/SALIR_bttn.png')
    btSalir = Button(ventPrin, text='Salir', image=bSalir, height="102", width="453", command=destruirPrin)
    btSalir.place(x=43.5, y=700)

    ventPrin.mainloop()

INICIO()
