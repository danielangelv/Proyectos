import pygame, sys

#Variables que parametrizan los color y dimencines de la pantalla
AZUL = [0,0,28]
ROJO = [245,15,15]
VERDE = [47, 163, 41]
BLANCO = [255,255,255]
NEGRO = [0,0,0]
AMARILLO = [255, 192, 5]
GRIS = [120,120,120]
color_fondo = (0,0,0)
ANCHO = 900
ALTO = 700
#----------------------------------------------------------------------------------------------------------------------------------
#Clase principal con cada uno de sus atributos
class Cliente:
    def __init__(self, Nombre, Celular, PQR):
        
        self.Nombre = Nombre
        self.Celular = Celular
        self.PQR = PQR
        
    def Ingresar_datos(self):

        self.Nombre = input("Ingresa tu nombre: ")
        self.Celular = input("Ingresa tu celular: ")

    #Funcion para poner las PQR
    def Poner_PQR(self):
        self.PQR = input("\nIngrese su PQR: ")
        print("\nPara nosotros es muy importante saber su opinion sobre nuestro servicio, hasta pronto.\n")
#----------------------------------------------------------------------------------------------------------------------------------

#Clase Auto la cual hereda los atributos de la clase padre cliente y ademas tiene sus propios atributos
class Auto(Cliente):
    def __init__(self, Nombre, Celular, PQR):
        super().__init__(Nombre, Celular, PQR)
    

    #Funcion Para mostrar los datos del vehiculo ingresador por el usuario
    def Mostras_datos(self, Placa, Color, Marca):

        self.Placa = Placa
        self.Color = Color
        self.Marca = Marca

    def ingresar_datos(self):

        self.Placa = input("Ingresa el numero de la placa de tu vehiculo: ")
        self.Color = input("Ingresa el color de tu vehiculo: ")
        self.Marca = input("Ingresa la marca de tu vehiculo: ")
#----------------------------------------------------------------------------------------------------------------------------------

#La ultima clase la cual hereda los atributos de la clase Auto y ademas cuenta con sus atributos propios.
class Parqueadero(Auto):
    def __init__(self, Nombre, Celular, PQR, Hora_Ingreso, Hora_Salida, Valor_horas, Cantidad_Horas, Valor_Turno1, Valor_Turno2, Valor_Turno3, Valor_Turno4):
        super().__init__(Nombre,Celular, PQR)

        self.Hora_Ingreso = Hora_Ingreso
        self.Hora_Salida = Hora_Salida
        self.Valor_horas = Valor_horas
        self.Cantidad_Horas = Cantidad_Horas
        self.Valor_Turno1 = Valor_Turno1
        self.Valor_Turno2 = Valor_Turno2
        self.Valor_Turno3 = Valor_Turno3
        self.Valor_Turno4 = Valor_Turno4

    
    def ingresar_datos(self):

        print("\nPor favor recuerde ingresar la hora en formato 24H")
        self.Hora_Ingreso = int(input("\nDigite la hora de ingreso de su vehiculo: "))
        self.Hora_Salida = int(input("\nDigite la hora aproximada de salida de su vehiculo: "))
        self.Valor_horas = int(input("\nDigite el valor de hora que desea usar de acuerdo a lo visto en la tabla de precios: "))

    #Esta funcion realiza el calculo de cuanto es el valor a pagar por el cliente al momento de retirar su vehiculo    
    def Facturacion(self):

        self.Cantidad_Horas = int(self.Hora_Salida - self.Hora_Ingreso)

        self.Valor_Turno1 = int(self.Cantidad_Horas * self.Valor_horas)

        #Condiconal para asegurar que si el cliente llega luego del turno elegido.
        if self.Valor_horas == 8000:
            self.Valor_Turno2 = int(self.Valor_horas) + ((self.Cantidad_Horas - 6) * 3000)

        elif self.Valor_horas == 15000:
            self.Valor_Turno3 = int(self.Valor_horas) + ((self.Cantidad_Horas - 12) * 3000)

        elif self.Valor_horas == 50000:
            self.Valor_Turno4 = int(self.Valor_horas)

#----------------------------------------------------------------------------------------------------------------------------------
#Creacion de la ventana de pygame y se le asigna un nombre.
pygame.init()
pantalla = pygame.display.set_mode([ANCHO, ALTO])
pygame.display.set_caption("Proyecto Final Parqueadero POO")

#Se carga la imagen de fondo, las lineas y los autos.
Fondo = pygame.image.load('imagenes/fondo.jpg')
Fondo_principal = pygame.image.load('imagenes/fondo_principal.png')
Lineas = pygame.image.load('imagenes/lineas.png')
Auto_amarillo = pygame.image.load('imagenes/auto_amarillo.png')
Auto_azul = pygame.image.load('imagenes/auto_azul.png')
Auto_blanco = pygame.image.load('imagenes/auto_blanco.png')
Auto_rojo = pygame.image.load('imagenes/auto_rojo.png')
Auto_verde = pygame.image.load('imagenes/auto_verde.png')

#Se establecen las variables de fondos que se van a usar.
fuente_titulo = pygame.font.SysFont("Times New Roman", 40, bold = True)
fuente = pygame.font.SysFont("Times New Roman", 20, bold = True)
base_PQR = pygame.font.SysFont("Times New Roman", 30, bold = True)

#----------------------------------------------------------------------------------------------------------------------------------
Cliente_1 = Cliente("", "", "")
Auto_1 = Auto("", "", "")
Parqueadero_1 = Parqueadero("", "", "", 0, 0, 0, 0, 0, 0, 0, 0)

mensaje_PQR = ""
mensaje_datos = ""
#----------------------------------------------------------------------------------------------------------------------------------
#Creacion del ciclo inicial donde se muestra el primer menu.
menu = False
while menu == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Inicio del evento de los numeros correspondientes al menu.
        if event.type == pygame.KEYDOWN:
            #Datos del ciclo 1
            if event.key == pygame.K_1:
                Cliente_1.Ingresar_datos()
                Auto_1.ingresar_datos()
                Parqueadero_1.ingresar_datos()
                Parqueadero_1.Facturacion()
                #Empieza el ciclo para la creacion de la pantalla de la opcion 1
#----------------------------------------------------------------------------------------------------------------------------------
                Fin = False
                while not Fin:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                Fin = True
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_f:

                                    menu = False
                                    while menu == False:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()
                                            
                                            pantalla.fill(BLANCO)

                                            #Lineas de la parte superior
                                            pantalla.blit(Lineas, [0,-310])
                                            pantalla.blit(Lineas, [490,-310])
                                            #Lineas de la parte inferior
                                            pantalla.blit(Lineas, [0,590])
                                            pantalla.blit(Lineas, [490,590])

                                            #Se muestran todos los datos de la factura digital.
                                            text_surfae = fuente_titulo.render("FACTURA PARQUEADERO POO",True, NEGRO)
                                            pantalla.blit(text_surfae,(150,110))
                                            text_surfae = fuente.render(f"Cliente: {Cliente_1.Nombre}",True, NEGRO)
                                            pantalla.blit(text_surfae,(80,180))
                                            text_surfae = fuente.render(f"Celular: {Cliente_1.Celular}",True, NEGRO)
                                            pantalla.blit(text_surfae,(80,210))
                                            text_surfae = fuente.render(f"La placa de su vehiculo: {Auto_1.Placa}",True, NEGRO)
                                            pantalla.blit(text_surfae,(80,240))
                                            text_surfae = fuente.render(f"Marca del vehiculo: {Auto_1.Marca}",True, NEGRO)
                                            pantalla.blit(text_surfae,(80,270))
                                            text_surfae = fuente.render(f"Color del vehiculo: {Auto_1.Color}",True, NEGRO)
                                            pantalla.blit(text_surfae,(80,300))
                                            text_surfae = fuente.render(f"Su vehiculo ingreso a las {Parqueadero_1.Hora_Ingreso}",True, NEGRO)
                                            pantalla.blit(text_surfae,(80,330))
                                            text_surfae = fuente.render(f"Su vehiculo salio a las {Parqueadero_1.Hora_Salida}",True, NEGRO)
                                            pantalla.blit(text_surfae,(80,360))
                                            text_surfae = fuente.render(f"Su vehiculo estuvo un total de {Parqueadero_1.Cantidad_Horas} horas",True, NEGRO)
                                            pantalla.blit(text_surfae,(450,180))
                                            text_surfae = fuente.render(f"Por un valor de {Parqueadero_1.Valor_horas} pesos el turno.",True, NEGRO)
                                            pantalla.blit(text_surfae,(450,210))

                                            #Condicional para asegurar que use la variable correcta a la hora de mostrar el valor total de pago
                                            if Parqueadero_1.Valor_horas == 3000:
                                                text_surfae = fuente.render(f"El valor total a pagar es de {Parqueadero_1.Valor_Turno1} de pesos",True, NEGRO)
                                                pantalla.blit(text_surfae,(450,240))
                                            
                                            elif Parqueadero_1.Valor_horas == 8000:
                                                text_surfae = fuente.render(f"El valor total a pagar es de {Parqueadero_1.Valor_Turno2} de pesos",True, NEGRO)
                                                pantalla.blit(text_surfae,(450,240))
                                            
                                            elif Parqueadero_1.Valor_horas == 15000:
                                                text_surfae = fuente.render(f"El valor total a pagar es de {Parqueadero_1.Valor_Turno3} de pesos",True, NEGRO)
                                                pantalla.blit(text_surfae,(450,240))
                                            
                                            elif Parqueadero_1.Valor_horas == 50000:
                                                text_surfae = fuente.render(f"El valor total a pagar es de {Parqueadero_1.Valor_Turno4} de pesos",True, NEGRO)
                                                pantalla.blit(text_surfae,(450,240))
                                            

                                            text_surfae = fuente.render("Muchas gracias por confiarnos su vehiculo, que en las mejores manos, hasta pronto.",True, NEGRO)
                                            pantalla.blit(text_surfae,(0,570))

                                            pygame.display.flip()

                                #Se crea la pantalla de regreso para que el usuario al precionar espacio vuelva al menu principal.
                                if event.key == pygame.K_SPACE:
                                    menu = False
                                    while menu == False:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_1:
                                                    Cliente_1.Ingresar_datos()
                                                    Auto_1.ingresar_datos()
                                                    Parqueadero_1.ingresar_datos()
                                                    Parqueadero_1.Facturacion()

                                                if event.key == pygame.K_2:
                                                    print("Actualmente tenemos 3 cupos disponibles.")
                                                if event.key == pygame.K_3:
                                                    Cliente_1.Poner_PQR()

                                            
                                            pantalla.fill(color_fondo)

                                            #Lineas de la parte superior
                                            pantalla.blit(Lineas, [0,-310])
                                            pantalla.blit(Lineas, [490,-310])
                                            #Lineas de la parte inferior
                                            pantalla.blit(Lineas, [0,590])
                                            pantalla.blit(Lineas, [490,590])

                                            pantalla.blit(Fondo_principal,[380,300])

                                            mensaje="BIENVENIDO AL PARQUEADERO POO"
                                            text_surfae = fuente_titulo.render(mensaje,True, NEGRO, AMARILLO)
                                            pantalla.blit(text_surfae,(100,30))
                                            
                                            mensaje_menu_1 = "1. Ingresar datos."
                                            text_surfae = fuente.render(mensaje_menu_1,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,120))

                                            mensaje_menu_2 = "2.Verificar si hay cupos."
                                            text_surfae = fuente.render(mensaje_menu_2,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,160))

                                            mensaje_menu_3 = "3.Ingresar una PQR."
                                            text_surfae = fuente.render(mensaje_menu_3,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,200))

                                            mensaje_menu_4 = "TABLA DE PRECIOS"
                                            text_surfae = fuente.render(mensaje_menu_4,True, NEGRO, AMARILLO)
                                            pantalla.blit(text_surfae,(350,240))

                                            mensaje_menu_4_1 = "Turno 1 valor hora: 3.000 pesos"
                                            text_surfae = fuente.render(mensaje_menu_4_1,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,270))

                                            mensaje_menu_4_2 = "Turno 2 valor 6 horas: 8.000"
                                            text_surfae = fuente.render(mensaje_menu_4_2,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,300))

                                            mensaje_menu_4_3 = "Turno 3 valor 12 horas: 15.000"
                                            text_surfae = fuente.render(mensaje_menu_4_3,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,330))

                                            mensaje_menu_4_4 = "Turno 4 valor mensualidad: 50.000"
                                            text_surfae = fuente.render(mensaje_menu_4_4,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,370))

                                            text_surfae = base_PQR.render(mensaje_datos,True, BLANCO)
                                            pantalla.blit(text_surfae,(100,400))

                                            pygame.display.flip()
                                        
                                    
                        pantalla.fill(color_fondo)

                        #Posicion de la de la imagen de fondo.
                        pantalla.blit(Fondo, [150, 158])

                        #Creacion de los condicionales para asegurar el ingreso del vehiculo con el color elegido.
                        if Auto_1.Color == 'Verde':
                            pantalla.blit(Auto_verde, [270,250])

                        elif Auto_1.Color == 'Amarillo':
                            pantalla.blit(Auto_amarillo, [480,250])

                        elif Auto_1.Color == 'Azul':
                            pantalla.blit(Auto_azul, [270,250])

                        elif Auto_1.Color == 'Blanco':
                            pantalla.blit(Auto_blanco, [270,250])

                        elif Auto_1.Color == 'Rojo':
                            pantalla.blit(Auto_rojo, [480,250])
                        else:
                            print("Por favor ingrese de manera correcta el color de su vehiculo.")
                            break

                        #Lineas de la parte superior
                        pantalla.blit(Lineas, [0,-310])
                        pantalla.blit(Lineas, [490,-310])

                        mensaje_registro = "Ahora su vehiculo se encuentra parqueado, muchas gracias por confiar en nosotros."
                        text_surfae = fuente.render(mensaje_registro,True, AZUL, AMARILLO)
                        pantalla.blit(text_surfae,(100,130))

                        mensaje_factura = "Presiona F para que ver tu factura digital."
                        text_surfae = fuente.render(mensaje_factura,True, AZUL, GRIS)
                        pantalla.blit(text_surfae,(250,670))

                        mensaje_regreso = "Si desea regresa por favor precione la BARRA ESPACIADORA"
                        text_surfae = fuente.render(mensaje_regreso,True, NEGRO, AMARILLO)
                        pantalla.blit(text_surfae,(350,10))
                        
                        #Actualizacion de la pantalla.
                        pygame.display.flip()
#----------------------------------------------------------------------------------------------------------------------------------
            if event.key == pygame.K_2:
                Fin = False
                while not Fin:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                Fin = True
                            if event.type == pygame.KEYDOWN:
#----------------------------------------------------------------------------------------------------------------------------------
                                #Se crea la pantalla de regreso para que el usuario al precionar espacio vuelva al menu principal.
                                if event.key == pygame.K_SPACE:
                                    menu = False
                                    while menu == False:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_1:
                                                    Cliente_1.Ingresar_datos()
                                                    Auto_1.ingresar_datos()
                                                    Parqueadero_1.ingresar_datos()
                                                    Parqueadero_1.Facturacion()

                                                    Fin = False
                                                    while not Fin:
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.QUIT:
                                                                    Fin = True
                                                                if event.type == pygame.KEYDOWN:
                                                                    if event.key == pygame.K_f:

                                                                        menu = False
                                                                        while menu == False:
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    pygame.quit()
                                                                                    sys.exit()
                                                                                
                                                                                pantalla.fill(BLANCO)

                                                                                #Lineas de la parte superior
                                                                                pantalla.blit(Lineas, [0,-310])
                                                                                pantalla.blit(Lineas, [490,-310])
                                                                                #Lineas de la parte inferior
                                                                                pantalla.blit(Lineas, [0,590])
                                                                                pantalla.blit(Lineas, [490,590])
                                    
                                                                                text_surfae = fuente_titulo.render("FACTURA PARQUEADERO POO",True, NEGRO)
                                                                                pantalla.blit(text_surfae,(150,110))
                                                                                text_surfae = fuente.render(f"Cliente: {Cliente_1.Nombre}",True, NEGRO)
                                                                                pantalla.blit(text_surfae,(80,180))
                                                                                text_surfae = fuente.render(f"Celular: {Cliente_1.Celular}",True, NEGRO)
                                                                                pantalla.blit(text_surfae,(80,210))
                                                                                text_surfae = fuente.render(f"La placa de su vehiculo: {Auto_1.Placa}",True, NEGRO)
                                                                                pantalla.blit(text_surfae,(80,240))
                                                                                text_surfae = fuente.render(f"Marca del vehiculo: {Auto_1.Marca}",True, NEGRO)
                                                                                pantalla.blit(text_surfae,(80,270))
                                                                                text_surfae = fuente.render(f"Color del vehiculo: {Auto_1.Color}",True, NEGRO)
                                                                                pantalla.blit(text_surfae,(80,300))
                                                                                text_surfae = fuente.render(f"Su vehiculo ingreso a las {Parqueadero_1.Hora_Ingreso}",True, NEGRO)
                                                                                pantalla.blit(text_surfae,(80,330))
                                                                                text_surfae = fuente.render(f"Su vehiculo salido a las {Parqueadero_1.Hora_Salida}",True, NEGRO)
                                                                                pantalla.blit(text_surfae,(80,360))
                                                                                text_surfae = fuente.render(f"Su vehiculo estuvo un total de {Parqueadero_1.Cantidad_Horas} horas",True, NEGRO)
                                                                                pantalla.blit(text_surfae,(450,180))
                                                                                text_surfae = fuente.render(f"Por un valor de {Parqueadero_1.Valor_horas} pesos el turno.",True, NEGRO)
                                                                                pantalla.blit(text_surfae,(450,210))
                                                                                
                                                                                if Parqueadero_1.Valor_horas == 3000:
                                                                                    text_surfae = fuente.render(f"El valor total a pagar es de {Parqueadero_1.Valor_Turno1} de pesos",True, NEGRO)
                                                                                    pantalla.blit(text_surfae,(450,240))
                                                                                
                                                                                elif Parqueadero_1.Valor_horas == 8000:
                                                                                    text_surfae = fuente.render(f"El valor total a pagar es de {Parqueadero_1.Valor_Turno2} de pesos",True, NEGRO)
                                                                                    pantalla.blit(text_surfae,(450,240))
                                                                                
                                                                                elif Parqueadero_1.Valor_horas == 15000:
                                                                                    text_surfae = fuente.render(f"El valor total a pagar es de {Parqueadero_1.Valor_Turno3} de pesos",True, NEGRO)
                                                                                    pantalla.blit(text_surfae,(450,240))
                                                                                
                                                                                elif Parqueadero_1.Valor_horas == 50000:
                                                                                    text_surfae = fuente.render(f"El valor total a pagar es de {Parqueadero_1.Valor_Turno4} de pesos",True, NEGRO)
                                                                                    pantalla.blit(text_surfae,(450,240))

                                                                                pygame.display.flip()

                                                                    #Se crea la pantalla de regreso para que el usuario al precionar espacio vuelva al menu principal.
                                                                    if event.key == pygame.K_SPACE:
                                                                        menu = False
                                                                        while menu == False:
                                                                            for event in pygame.event.get():
                                                                                if event.type == pygame.QUIT:
                                                                                    pygame.quit()
                                                                                    sys.exit()

                                                                                if event.type == pygame.KEYDOWN:
                                                                                    if event.key == pygame.K_1:
                                                                                        Cliente_1.Ingresar_datos()
                                                                                        Auto_1.ingresar_datos()
                                                                                        Parqueadero_1.ingresar_datos()
                                                                                        Parqueadero_1.Facturacion()

                                                                                    if event.key == pygame.K_2:
                                                                                        print("Actualmente tenemos 3 cupos disponibles.")
                                                                                    if event.key == pygame.K_3:
                                                                                        Cliente_1.Poner_PQR()

                                                                                
                                                                                pantalla.fill(color_fondo)

                                                                                #Lineas de la parte superior
                                                                                pantalla.blit(Lineas, [0,-310])
                                                                                pantalla.blit(Lineas, [490,-310])
                                                                                #Lineas de la parte inferior
                                                                                pantalla.blit(Lineas, [0,590])
                                                                                pantalla.blit(Lineas, [490,590])

                                                                                pantalla.blit(Fondo_principal,[380,300])

                                                                                mensaje="BIENVENIDO AL PARQUEADERO POO"
                                                                                text_surfae = fuente_titulo.render(mensaje,True, NEGRO, AMARILLO)
                                                                                pantalla.blit(text_surfae,(100,30))
                                                                                
                                                                                mensaje_menu_1 = "1. Ingresar datos."
                                                                                text_surfae = fuente.render(mensaje_menu_1,True, BLANCO)
                                                                                pantalla.blit(text_surfae,(0,120))

                                                                                mensaje_menu_2 = "2.Verificar si hay cupos."
                                                                                text_surfae = fuente.render(mensaje_menu_2,True, BLANCO)
                                                                                pantalla.blit(text_surfae,(0,160))

                                                                                mensaje_menu_3 = "3.Ingresar una PQR."
                                                                                text_surfae = fuente.render(mensaje_menu_3,True, BLANCO)
                                                                                pantalla.blit(text_surfae,(0,200))

                                                                                mensaje_menu_4 = "TABLA DE PRECIOS"
                                                                                text_surfae = fuente.render(mensaje_menu_4,True, NEGRO, AMARILLO)
                                                                                pantalla.blit(text_surfae,(350,240))

                                                                                mensaje_menu_4_1 = "Turno 1 valor hora: 3000 pesos"
                                                                                text_surfae = fuente.render(mensaje_menu_4_1,True, BLANCO)
                                                                                pantalla.blit(text_surfae,(0,270))

                                                                                mensaje_menu_4_2 = "Turno 2 valor 6 horas: 8.000"
                                                                                text_surfae = fuente.render(mensaje_menu_4_2,True, BLANCO)
                                                                                pantalla.blit(text_surfae,(0,300))

                                                                                mensaje_menu_4_3 = "Turno 3 valor 12 horas: 15.000"
                                                                                text_surfae = fuente.render(mensaje_menu_4_3,True, BLANCO)
                                                                                pantalla.blit(text_surfae,(0,330))

                                                                                mensaje_menu_4_4 = "Turno 4 valor mensualidad: 50.000"
                                                                                text_surfae = fuente.render(mensaje_menu_4_4,True, BLANCO)
                                                                                pantalla.blit(text_surfae,(0,370))

                                                                                text_surfae = base_PQR.render(mensaje_datos,True, BLANCO)
                                                                                pantalla.blit(text_surfae,(100,400))

                                                                                pygame.display.flip()
                                                                            
                                                                        
                                                            pantalla.fill(color_fondo)

                                                            #Posicion de la de la imagen de fondo.
                                                            pantalla.blit(Fondo, [150, 158])

                                                            if Auto_1.Color == 'Verde':
                                                                pantalla.blit(Auto_verde, [270,250])

                                                            elif Auto_1.Color == 'Amarillo':
                                                                pantalla.blit(Auto_amarillo, [480,250])

                                                            elif Auto_1.Color == 'Azul':
                                                                pantalla.blit(Auto_azul, [270,250])

                                                            elif Auto_1.Color == 'Blanco':
                                                                pantalla.blit(Auto_blanco, [270,250])

                                                            elif Auto_1.Color == 'Rojo':
                                                                pantalla.blit(Auto_rojo, [480,250])
                                                            else:
                                                                print("Por favor ingrese de manera correcta el color de su vehiculo.")

                                                            #Lineas de la parte superior
                                                            pantalla.blit(Lineas, [0,-310])
                                                            pantalla.blit(Lineas, [490,-310])

                                                            mensaje_registro = "Ahora su vehiculo se encuentra parqueado, muchas gracias por confiar en nosotros."
                                                            text_surfae = fuente.render(mensaje_registro,True, AZUL, AMARILLO)
                                                            pantalla.blit(text_surfae,(100,130))

                                                            mensaje_factura = "Presiona F para que ver tu factura digital."
                                                            text_surfae = fuente.render(mensaje_factura,True, AZUL, GRIS)
                                                            pantalla.blit(text_surfae,(250,670))

                                                            mensaje_regreso = "Si desea regresa por favor precione la BARRA ESPACIADORA"
                                                            text_surfae = fuente.render(mensaje_regreso,True, NEGRO, AMARILLO)
                                                            pantalla.blit(text_surfae,(350,10))
                                                            
                                                            #Actualizacion de la pantalla.
                                                            pygame.display.flip()

                                                if event.key == pygame.K_2:
                                                    print("Actualmente tenemos 3 cupos disponibles.")
                                                if event.key == pygame.K_3:
                                                    Cliente_1.Poner_PQR()

                                            
                                            pantalla.fill(color_fondo)

                                            #Lineas de la parte superior
                                            pantalla.blit(Lineas, [0,-310])
                                            pantalla.blit(Lineas, [490,-310])
                                            #Lineas de la parte inferior
                                            pantalla.blit(Lineas, [0,590])
                                            pantalla.blit(Lineas, [490,590])

                                            pantalla.blit(Fondo_principal,[380,300])

                                            mensaje="BIENVENIDO AL PARQUEADERO POO"
                                            text_surfae = fuente_titulo.render(mensaje,True, NEGRO, AMARILLO)
                                            pantalla.blit(text_surfae,(100,30))
                                            
                                            mensaje_menu_1 = "1. Ingresar datos."
                                            text_surfae = fuente.render(mensaje_menu_1,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,120))

                                            mensaje_menu_2 = "2.Verificar si hay cupos."
                                            text_surfae = fuente.render(mensaje_menu_2,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,160))

                                            mensaje_menu_3 = "3.Ingresar una PQR."
                                            text_surfae = fuente.render(mensaje_menu_3,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,200))

                                            mensaje_menu_4 = "TABLA DE PRECIOS"
                                            text_surfae = fuente.render(mensaje_menu_4,True, NEGRO, AMARILLO)
                                            pantalla.blit(text_surfae,(350,240))

                                            mensaje_menu_4_1 = "Turno 1 valor hora: 3000 pesos"
                                            text_surfae = fuente.render(mensaje_menu_4_1,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,270))

                                            mensaje_menu_4_2 = "Turno 2 valor 6 horas: 8.000"
                                            text_surfae = fuente.render(mensaje_menu_4_2,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,300))

                                            mensaje_menu_4_3 = "Turno 3 valor 12 horas: 15.000"
                                            text_surfae = fuente.render(mensaje_menu_4_3,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,330))

                                            mensaje_menu_4_4 = "Turno 4 valor mensualidad: 50.000"
                                            text_surfae = fuente.render(mensaje_menu_4_4,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,370))

                                            text_surfae = base_PQR.render(mensaje_datos,True, BLANCO)
                                            pantalla.blit(text_surfae,(100,400))

                                            pygame.display.flip()
#----------------------------------------------------------------------------------------------------------------------------------
                                    
                        pantalla.fill(color_fondo)

                        #Posicion de la de la imagen de fondo.
                        pantalla.blit(Fondo, [150, 158])

                        #Lineas de la parte superior
                        pantalla.blit(Lineas, [0,-310])
                        pantalla.blit(Lineas, [490,-310])

                        mensaje_cupo = "Actualmente tenemos 3 cupos disponibles"
                        text_surfae = fuente.render(mensaje_cupo,True, BLANCO, NEGRO)
                        pantalla.blit(text_surfae,(250,180))

                        mensaje_regreso = "Si desea regresa por favor precione la BARRA ESPACIADORA"
                        text_surfae = fuente.render(mensaje_regreso,True, NEGRO, AMARILLO)
                        pantalla.blit(text_surfae,(350,10))
                        
                        #Actualizacion de la pantalla.
                        pygame.display.flip()

            if event.key == pygame.K_3:
                Cliente_1.Poner_PQR()
                mensaje_PQR = "Para nosotros es muy importante saber su opinion sobre nuestro servicio, hasta pronto."
                Fin = False
                while not Fin:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                Fin = True
                            if event.type == pygame.KEYDOWN:
#----------------------------------------------------------------------------------------------------------------------------------
                                #Se crea la pantalla de regreso para que el usuario al precionar espacio vuelva al menu principal.
                                if event.key == pygame.K_SPACE:
                                    menu = False
                                    while menu == False:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_1:
                                                    Cliente_1.Ingresar_datos()
                                                    Auto_1.ingresar_datos()
                                                    Parqueadero_1.ingresar_datos()
                                                    Parqueadero_1.Facturacion()

                                                if event.key == pygame.K_2:
                                                    print("Actualmente tenemos 3 cupos disponibles.")
                                                if event.key == pygame.K_3:
                                                    Cliente_1.Poner_PQR()
                                            
                                            pantalla.fill(color_fondo)

                                            #Lineas de la parte superior
                                            pantalla.blit(Lineas, [0,-310])
                                            pantalla.blit(Lineas, [490,-310])
                                            #Lineas de la parte inferior
                                            pantalla.blit(Lineas, [0,590])
                                            pantalla.blit(Lineas, [490,590])

                                            pantalla.blit(Fondo_principal,[380,300])

                                            mensaje="BIENVENIDO AL PARQUEADERO POO"
                                            text_surfae = fuente_titulo.render(mensaje,True, NEGRO, AMARILLO)
                                            pantalla.blit(text_surfae,(100,30))
                                            
                                            mensaje_menu_1 = "1. Ingresar datos."
                                            text_surfae = fuente.render(mensaje_menu_1,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,120))

                                            mensaje_menu_2 = "2.Verificar si hay cupos."
                                            text_surfae = fuente.render(mensaje_menu_2,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,160))

                                            mensaje_menu_3 = "3.Ingresar una PQR."
                                            text_surfae = fuente.render(mensaje_menu_3,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,200))

                                            mensaje_menu_4 = "TABLA DE PRECIOS"
                                            text_surfae = fuente.render(mensaje_menu_4,True, NEGRO, AMARILLO)
                                            pantalla.blit(text_surfae,(350,240))

                                            mensaje_menu_4_1 = "Turno 1 valor hora: 3000 pesos"
                                            text_surfae = fuente.render(mensaje_menu_4_1,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,270))

                                            mensaje_menu_4_2 = "Turno 2 valor 6 horas: 8.000"
                                            text_surfae = fuente.render(mensaje_menu_4_2,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,300))

                                            mensaje_menu_4_3 = "Turno 3 valor 12 horas: 15.000"
                                            text_surfae = fuente.render(mensaje_menu_4_3,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,330))

                                            mensaje_menu_4_4 = "Turno 4 valor mensualidad: 50.000"
                                            text_surfae = fuente.render(mensaje_menu_4_4,True, BLANCO)
                                            pantalla.blit(text_surfae,(0,370))

                                            text_surfae = base_PQR.render(mensaje_datos,True, BLANCO)
                                            pantalla.blit(text_surfae,(100,400))

                                            pygame.display.flip()

                        pantalla.fill(color_fondo)

                        #Lineas de la parte superior
                        pantalla.blit(Lineas, [0,-310])
                        pantalla.blit(Lineas, [490,-310])
                        #Lineas de la parte inferior
                        pantalla.blit(Lineas, [0,590])
                        pantalla.blit(Lineas, [490,590])

                        mensaje_regreso = "Si desea regresa por favor precione la BARRA ESPACIADORA"
                        text_surfae = fuente.render(mensaje_regreso,True, NEGRO, AMARILLO)
                        pantalla.blit(text_surfae,(350,10))

                        text_surfae = fuente.render(mensaje_PQR,True, BLANCO)
                        pantalla.blit(text_surfae,(50,350))
                        
                        #Actualizacion de la pantalla.
                        pygame.display.flip()
    
        pantalla.fill(color_fondo)

        #Lineas de la parte superior
        pantalla.blit(Lineas, [0,-310])
        pantalla.blit(Lineas, [490,-310])
        #Lineas de la parte inferior
        pantalla.blit(Lineas, [0,590])
        pantalla.blit(Lineas, [490,590])

        pantalla.blit(Fondo_principal,[380,300])

        mensaje="BIENVENIDO AL PARQUEADERO POO"
        text_surfae = fuente_titulo.render(mensaje,True, NEGRO, AMARILLO)
        pantalla.blit(text_surfae,(100,30))
        
        mensaje_menu_1 = "1. Ingresar datos."
        text_surfae = fuente.render(mensaje_menu_1,True, BLANCO)
        pantalla.blit(text_surfae,(0,120))

        mensaje_menu_2 = "2.Verificar si hay cupos."
        text_surfae = fuente.render(mensaje_menu_2,True, BLANCO)
        pantalla.blit(text_surfae,(0,160))

        mensaje_menu_3 = "3.Ingresar una PQR."
        text_surfae = fuente.render(mensaje_menu_3,True, BLANCO)
        pantalla.blit(text_surfae,(0,200))

        mensaje_menu_4 = "TABLA DE PRECIOS"
        text_surfae = fuente.render(mensaje_menu_4,True, NEGRO, AMARILLO)
        pantalla.blit(text_surfae,(350,240))

        mensaje_menu_4_1 = "Turno 1 valor hora: 3000 pesos"
        text_surfae = fuente.render(mensaje_menu_4_1,True, BLANCO)
        pantalla.blit(text_surfae,(0,270))

        mensaje_menu_4_2 = "Turno 2 valor 6 horas: 8.000"
        text_surfae = fuente.render(mensaje_menu_4_2,True, BLANCO)
        pantalla.blit(text_surfae,(0,300))

        mensaje_menu_4_3 = "Turno 3 valor 12 horas: 15.000"
        text_surfae = fuente.render(mensaje_menu_4_3,True, BLANCO)
        pantalla.blit(text_surfae,(0,330))

        mensaje_menu_4_4 = "Turno 4 valor mensualidad: 50.000"
        text_surfae = fuente.render(mensaje_menu_4_4,True, BLANCO)
        pantalla.blit(text_surfae,(0,370))

        text_surfae = base_PQR.render(mensaje_datos,True, BLANCO)
        pantalla.blit(text_surfae,(100,400))

        pygame.display.flip()
#----------------------------------------------------------------------------------------------------------------------------------

pygame.quit()