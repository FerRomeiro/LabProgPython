#pygame nos ayuda a realizar videojuegos
#es un contenedor de python para la biblioteca SDL que significa simple directmedia layer q esta desarrollada en C. 
#SDL brinda acceso multiplataforma a los componentes de hardware
#multimedia subyacentes de su sistema,como sonido,video,mouse,teclado,y joystick
#


import pygame #SIEMPRE IMPORTAMOS MODULO O BIBLIOTECA PYGAME

pygame.init() #LO INICIALIZAMOS 

window=pygame.display.set_mode([500,500]) #screen es el objeto,y creamos una ventana  set_mode es el metodo

running = True

while running: #while eterno o infinito siempre Verdadero
	for event in pygame.event.get(): #UN EVENTO ES ALGO Q OCURRE Y Q TIENE SIGNIFICADO POR EJEMPL
		if event.type == pygame.QUIT: #quit es salir, q es la cruz q hago para salir de una ventada
			running = False

	window.fill((255,255,255)) #defino con la tupla el rgb osea el color de la ventana, en este caso es color blanco
	pygame.draw.circle(window,(0,0,255),(250,250),75)

	pygame.display.flip() #todos los cambios q hagamos se reconstruye en pantalla gracias a flip
						#constantemente lo pinta de blanco y lo muestra y asi sucesivamente porque esta dentro del for hasta q sea False


window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("vamos a hacer un juego!")
while(running):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

#Caracteristicas: imagenes en formato png,bmp , sistemas de sonidos, formato wav, ogc,MP3,operaciones relacionadas con el gestor de ventanas
#eventos de aplicacion,manejo de distpositivos de entrada , temporizadores,colisiones, sistemas de sprites

#VENTANAS: el modulo display permite controlar todo lo q tiene q ver con las ventanas y las pantallas de un programa 
#se crea una ventana:
#screen=pygame.display.set_mode([500,500]) #screen es el objeto o variable, seteo el modo 
#titulo de la ventana:
#pygame.display.set_caption("Hola mundo") #aca se setea el caption

#SUPERFICIE:un objeto Surface representa un buffer de memoria de pixeles, la pantalla se representa tambien como una superficie
#Se pinta el fondo de la ventana de blanco
#scree.fill((255,255,255))
#sobre una superficie se puede dibujar diferentes formas(rectangulos,elipses,lineas,etc)
#se dibuja circulo azul:
#pygame.draw.circle(screen,(0,0,255),(250,250),75)
#se dibuja cuadrado amarillo
#pygame.draw.rect(scree,(255,255,0),(30,30,60,60))
#
#CONTROLES: pygame provee control sobre los dispostivos de entrada mas comunes:
#Teclas pygame.key 
#Mouse pygame.mouse
#joystick pygame.joystick

#pygame maneja todos sus mensajes de eventos a traves de una cola de eventos
#pygame.event.get()
#tengo q controlar los distintos eventos y los eventos van a una cola de eventos, primer elemento en entrar es q el q se ejecuta y es el primero en salir
#el segundo evento entra para ejecutar y sale y asi sucesivamente
#el concepto de pila: el primero q llega es el ultimo en irse, el de arriba es el concepto de cola
#ej: cuando lavo los plato el primero q lavo va a ser el ultimo q seque porq los acumulo uno encima de otro
#
#EVENTOS: la cola de eventos contiene objetos de evento pygame.event.EventType
#se verifica si el usuario cerro la ventana:
#for event in pygame.event.get(): #obtengo el evento con get y lo guardo en event despues lo imprime para ver q evento es
#	print(type(event)) #class "Event"
#todas la instancias de Event contienen un identificador de tipo de evento y atributos especificos para ese tipo de evento.
#se verifica q el usuario cerro la ventana:
#for event in pygame.event.get():
	#if event.type==pygame.QUIT:
		#running=False
#EVENTOS mouse: se verifica si el evento es el del mouse presionado y luego se verifica cual es la posicion
#for event in pygame.event.get():
	#if event.type==pygame.QUIT:
		#running=False
	#if event.type==pygame.MOUSEBUTTONDOWN:
		#print(event.pos) #(322,153)  #ACA IMPRIME LA POSICION DEL MOUSE 
#
#LOS EVENTOS VAN A SER TODO LO Q PASE DENTRO DE LA VENTANA DE JUEGO CLICK, PRESIONAR UN BOTON, ETC TODO ESTO SON EVENTOS Y NOSOTROS GUARDAMOS LOS EVENTOS 
#PARA SABER CUAL ES EL Q NOSOTROS QUEREMOS
#

#Matias quiroz
import pygame
pygame.init()

ancho_ventana=500
alto_ventana=500
color_blanco=(255,255,255)
color_amarillo=(255,255,0)
color_celeste=(0,0,128)
#posicion circulo
posicion_circulo=(0,100)
#Timer 
timer_segundos=pygame.USEREVENT
#un evento q creo yo q es este evento se ejecute con un tiempo que yo determine
#esto se va a ejecutar cada 1 seg
pygame.time.set_timer(timer_segundos,100) #1000 es 1 seg
pantalla=pygame.display.set_mode((ancho_ventana,alto_ventana)) #esto es una tupla, como siempre voy a trabajar con la misma resolucion lo dejo asi
pygame.display.set_caption("Juego") #el titulo del juego es juego
flag_correr=True
while flag_correr:
		lista_eventos=pygame.event.get() #CON ESTO TOMAMOS TODOS LOS ELEMENTOS Q PASE EN NUETRA VENTANA 
		for event in lista_eventos:
			if event == pygame.QUIT: #CON ESTO DETECTO SI EL USUARIO CERRO LA VENTANA 
				flag_correr=False
			if event.type == pygame.MOUSEMOTION: #CON EL MOUSEMOTION MUEVO EL CIRCULO CON EL MOUSE 
				posicion_circulo = evento.pos 
		
		pantalla.fill(color_celeste) # FONDO COLOR
		pygame.draw.circle(pantalla,color_amarillo,posicion_circulo,80)
		#mostrar
		pygame.display.flip() #MUESTRA O ACTUALIZA LOS CAMBIOS AL USUARIO. UNA VEZ Q TERMINO DE CARGAR TODO HAGO UN FLIP SINO SERIA UNA VENTANA NEGRA AUNQ
							#TODO CARGADO. LO Q HACE EL FLIP ES Q TODO LO Q TENGA CARGADO EL USUARIO PUEDA VERLO 

pygame.quit() #ESTA ES LA FORMA CORRECTA DE CERRAR EL PROGRAMA MAS ALLA Q FUNCIONE TODO SIN ESTA LINEA. 

#Evento  tiempo: para poder fijar un evento q ocurran por tiempo. Necesitamos un timer porque esto es electreconico y lo hace en una velocidad inperceptible 
#
#tick = pygame.USEREVENT + 0 
#pygame.time.set_timer(tick,1000) #1000 milesimas q es 1 seg
#while running:
	#for event in pygame.event.get():
		#if event.type == tick:
			#print("Ya paso un segundo")

#Evento Teclado: se verifica si el evento es el de una tecla presionada y luego se verifica cual es la tecla
#for event in pygame.event.get():
	#if event.type==pygame.QUIT:
		#running=False
	#if event.type==pygame.KEYDOWN: #si se presiono una tecla
		#if event.key == pygame.K_x: #aca prgunto q tecla y la capturo, en este caso es la X
			#print("Se presiono la tecla X")
	
#renato
#manejo de eventos

import pygame
import colores

pygame.init()

ancho=800
alto=600
ventana=pygame.display.set_mode(ancho,alto)
pygame.display.set_caption("Dibujar en negro al hacer click")
ventana.fill(colores.BLANCO)
#variables de color
dibujando=False
punto_anteorior=None 
#bucle principal del juego
jugando=True
while jugando:
	for evento in pygame.event.get():
		if evento.type==pygame.quit:
			jugando=False
		elif evento.type==pygame.MOUSEBUTTONDOWN:
			#iniciar el rastreo del mouse y obtener las coordenadas del click
			dibujando=True
			punto_anteorior=pygame.mouse.get_pos()
		elif evento.type == pygame.MOUSEBUTTONUP:
			#detener el rastreo del mouse al soltar el boton
			dibujando=False
		elif evento.type==pygame.MOUSEMOTION:
			if dibujando:
				#detener las coordenadas actuales del mouse 
				x,y = pygame.mouse.get_pos()

				#dibujar una linea desde el punto anterior al actual 
				pygame.draw.line(ventana,colores,ROJO,punto_anterior,(x,y),10)
				pygame.draw.circle(ventana,colores.NEGRO,(x,y),1)
				#actualizar el punto anterior 
				punto_anteorior=(x,y)
#actualizar ventana
pygame.display.flip()

#salir del programa
pygame.quit()



import pygame
import personaje

ancho_ventana=800
alto_ventana=800

pygame.init()
ventana_ppal=pygame.display.set_mode((ancho_ventana,alto_ventana))
pygame.display.set_caption("pygame homero come donas")

#TIMER
timer=pygame.USEREVENT + 0 
pygame.time.set_timer(timer,100) #100 es 0,1 seg y esto seria de cuanto en cuanto va aumentar, las donas caen cada 0,1 seg

player=personaje.crear(ancho_ventana/2,alto_ventana-200,200,200) #ACA TRABAJAMOS CON IMAGENES Y RECTANGULOS, esta vendria a ser la proporcion o tamaño del persaonej
lista_donas=dona.crear_lista_donas(50)

flag_run=True
while flag_run:
	lista_eventos=pygame.event.get()

	for event in lista_eventos:
		if evento.type==pygame.QUIT:
			flag_run=False
		if evento.type==pygame.USEREVENT: #constatemente va haber un valor del tipo userevent
			if evento.type==timer:
				dona.update(lista_donas)

	lista_teclas=pygame.key.get_pressed()

	if lista_teclas[pygame.K_LEFT]: #pregunto si apreta la tecla izq
		personaje.update(player,-3) # -3 se mueve -3 pixeles hacia la izq si fuera un -30 se iria a la mierda el personaje
	if lista_teclas[pygame.K_RIGHT]:
		personaje.update(player,3)
	
	ventana_ppal.fill(colores,BLANCO)
	personaje.actualizar_pantalla(player,ventana_ppal) #actualiza la posicion del personaje 
	dona.actualizar_pantalla(lista_donas,player,ventana_ppal)

	pygame.display.flip()

pygame.quit()

#NOSOTRO PARA INICIAR EL CONTADOR TENEMSO Q HACER set_timer 
#

#EJEMPLO TECLADO
import pygame
pygame.init()

ancho_ventana=500
alto_ventana=500
color_blanco=(255,255,255)
color_amarillo=(255,255,0)
color_celeste=(0,0,128)
#posicion circulo
posicion_circulo=(0,100)
#Timer 
timer_segundos=pygame.USEREVENT
#un evento q creo yo q es este evento se ejecute con un tiempo que yo determine
#esto se va a ejecutar cada 1 seg
pygame.time.set_timer(timer_segundos,100) #1000 es 1 seg
pantalla=pygame.display.set_mode((ancho_ventana,alto_ventana)) #esto es una tupla, como siempre voy a trabajar con la misma resolucion lo dejo asi
pygame.display.set_caption("Juego") #el titulo del juego es juego
flag_correr=True
while flag_correr:
		lista_eventos=pygame.event.get() #CON ESTO TOMAMOS TODOS LOS ELEMENTOS Q PASE EN NUETRA VENTANA 
		for event in lista_eventos:
			if event == pygame.QUIT:
				flag_correr=False
			if evento.type == pygame.KEYDOWN: #si presiono la tecla una vez
				if evento.key==pygame.K_RIGHT:
					posicion_circulo[0]=posicion_circulo[0]+10
				if evento.key==pygame.K_LEFT:
					posicion_circulo[0]=posicion_circulo[0]-10
				if evento.key==pygame.K_UP:
					posicion_circulo[0]=posicion_circulo[1]-10
				if evento.key==pygame.K_DOWN:
					posicion_circulo[0]=posicion_circulo[1]+10
	
	pantalla.fill(color_celeste)
	pygame.draw.circle(pantalla,(color_amarillo),posicion_circulo,80) #pantalla ES EL NOMBRE DE LA VENTANA, DONDE SE VA A DIBUJAR EL CIRCULO
																#A TRAVES DE posicion_circulo JUEGO CON LOS TAMAÑOS EN EL IF Y 80 ES EL TAMAÑO DEL CIRCULO
	#mostrar
	pygame.display.flip()
pygame.quit()




#segunda parte de la clase

import pygame 
pygame.init() #LO INICIALIZAMOS 

window=pygame.display.set_mode([500,500]) #screen es el objeto,y creamos una ventana  set_mode es el metodo
running = True
while running: 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			running = False

	window.fill((255,255,255)) #defino con la tupla el rgb osea el color de la ventana, en este caso es color blanco

	pygame.draw.circle(window,(0,0,255),(250,250),75)#WINDOW ES EL NOMBRE DE LA VENTANA DONDE SE VA A DIBUJAR EL CIRCULO,PRIMER(ES EL COLOR) Y SEG (POSICION)
														#Y 75 ES EL TAMAÑO DEL CIRCULO OSEA LA RADIO

	pygame.display.flip() #todos los cambios q hagamos se reconstruye en pantalla gracias a flip
						#constantemente lo pinta de blanco y lo muestra y asi sucesivamente porque esta dentro del for hasta q sea False


window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("vamos a hacer un juego!")
while(running):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


#IMAGENES:png y jpg la diferencia es q la imagen png no tiene fondo, cortonea y la jpg es una imagen completa con fondo y todo
#con el metodo load de la clase image se puede generar una superficie desde una imagen EN PNG TMB TIENE BORDES PERO SON INVISIBLES ES DECIR ES CUADRADO TMB
#hay q crear una carpeta con las imagenes para usar el nombre y la extension q tiene y para usarla hay q hacer lo del ejemplo:
#imagen=pygame.image.load("00.png")
#print(type(image)) #class "pygame.Surface"
#esto es lo q primero se debe hacer con las imagenes
#Para copiar la superficie de la imagen en la superficie de la pantalla o en otra superficie se debe utilizar blit() indicando la ubicacion
#imagen=pygame.image.load("00.png")  
#print(type(image)) #class "pygame.Surface"
#sceen.blit(imagen,(50,50)) #

#ejemplo imagen:
import pygame 
pygame.init()

#colores
ANCHO_VENTADA=500
ALTO_VENTANA=500
COLOR_CELESTE=(0,0,128)

#posiciones
posicion_messi=[30,100] #COMO LA POSICION DE MESSI SI LA VOY A MODIFICAR ES UNA LISTA SI FUERA TUPLA COMO EN SCALE NO PODRIA LUEGO MODIFICAR SU TAMAÑO
posicion_pasto=(0,0)
#imagenes
imagen_messi=pygame.image.load("messi.png") #el load me permite con el nombre de la imagen agarrar la superficie de la imagen y guardarla
imagen_messi=pygame.transform.scale(imagen_messi,(200,200)) #esto me permite cambiar el escalado, el tamaño de la imagen Y COMO ES TUPLA NO PUEDO CAMBIARL LUEGO
imagen_pasto=pygame.image.load("pasto.jpg")
imagen_pasto=pygame.transform.scale(imagen_pasto,(500,500))
#crear pantalla
pantalla=pygame.display.set_mode((ANCHO_VENTADA,ALTO_VENTANA))
#seteo un titulo de pantalla
pygame.display.set_caption("Juego")
flag_correr=True
while flag_correr:
	lista_eventos=pygame.event.get()
	for evento in lista_eventos:
		if evento.type==pygame.QUIT:
			flag_correr=False
		if evento.type==pygame.MOUSEBUTTONDOWN: #si presiono el boton del mouse y mantengo dependendiendo de donde cambio la posicion de messi
			#print(evento.pos)
			posicion_messi=evento.pos

	#fondo color
	pantalla.fill(COLOR_CELESTE)
	pantalla.blit(imagen_pasto,(posicion_pasto)) #RECORDAR Q ESTA PARTE SON POR CAPAS, ES DECIR PRIMERO SIEMPRE VA EL FONDO 
												#EN ESTE CASO SI FUERA AL REVES MESSI ESTARIA DEBAJO DEL FONDO
	pantalla.blit(imagen_messi,(posicion_messi)) #fundir la imagen, pegamos la foto de messi a nuestra pantalla ya q agregamos algo externo q no pertenece a pygame
												#por eso usamos el metodo blit

	#mostrar
	pygame.display.flip()
pygame.quit()


#TEXTOS:el metodo render me permite obtener una superficie a partir de un texto
#ESTO NOS VA A PERMITIR EMPEZAR A JUGAR CON LOS TEXTOS Q VOY A PONER

#font=pygame.font.SysFont("Arial Narrow",50)
#text=font.render("HOLA MUNDO",True,(255,0,0))
#print(type(text)) #class "pygame.Surface"

#ejeplo texto

import pygame 
pygame.init()

#colores
ANCHO_VENTADA=500
ALTO_VENTANA=500
COLOR_CELESTE=(0,0,128)

#posiciones
posicion_messi=[30,100] #
posicion_pasto=(0,0)

#TEXTO
font = pygame.font.SysFont("Arial Narrow",50) #la fuente q quiero ponerle y 50 es el tamaño

#imagenes
imagen_messi=pygame.image.load("messi.png") 
imagen_messi=pygame.transform.scale(imagen_messi,(200,200)) 
imagen_pasto=pygame.image.load("pasto.jpg")
imagen_pasto=pygame.transform.scale(imagen_pasto,(500,500))
#crear pantalla
pantalla=pygame.display.set_mode((ANCHO_VENTADA,ALTO_VENTANA))
#seteo un titulo de pantalla
pygame.display.set_caption("Juego")
flag_correr=True
while flag_correr:
	lista_eventos=pygame.event.get()
	for evento in lista_eventos:
		if evento.type==pygame.QUIT:
			flag_correr=False
		if evento.type==pygame.MOUSEBUTTONDOWN: 
			#print(evento.pos)
			posicion_messi=evento.pos

	#fondo color

	pantalla.fill(COLOR_CELESTE)
	pantalla.blit(imagen_pasto,(posicion_pasto)) 
	pantalla.blit(imagen_messi,(posicion_messi)) 

	text=font.render("HOLA MUNDO",True,(255,0,0)) #DENTRO SE PONE EL TEXTO Q QUIERO el antialias lo vamos a tener en TRUE q hace q no se vean pixeleadas 
												#por eso esta en TRUE, lo q va (es el color)

	pantalla.blit(text(50,50)) #ACA FUNDIMOS EL TEXTO pantalla seria el nombre de la pantalla q es lo q le puse yo en este ejemplo 
							#ACA PUESO USARLO COMO EL TIEMPO DE ALGO O EL PUNTAJE Y ASI 
							#el blit es importante para fundirlo a la pantalla y para el texto
	#mostrar
	pygame.display.flip()

pygame.quit()


#ejemplo si de si mantengo la tecla presionado mueve el circulo
import pygame
#iniciar la pantalla
pygame.init()
#COLORES
ANCHO_VENTANA = 500
ALTO_VENTANA = 500
COLOR_AMARILLO = (255, 255, 0)
COLOR_CELESTE = ( 0, 0,128)
#POSICIONES
posicion_circulo = [100, 100]
#crear la pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
#Seteo un título en la pantalla
pygame.display.set_caption("Juego")
flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
    #salgo del for para ver que teclas están presionadas, se lee todo el tiempo
    #funciona mientras las teclas están presionadas
    lista_teclas = pygame.key.get_pressed() #ESTE METODO ME GUARDA TODAS LAS TECLAS Q PRESIONO POR ESO NO ESTA EN EVENTOS, ME GUARDO TODAS LAS TECLAS Q TOCO
    #print(lista_teclas)
    if True in lista_teclas: #PREGUNTO SI EN LA LISTA Q TENGO HAY ALGUNA Q ES VERDADERA 
        if lista_teclas[pygame.K_RIGHT]:
            posicion_circulo[0] = posicion_circulo[0] + 0.05 #se mueve 0.05 pixel #mientras #la tecla está presionada
        if lista_teclas[pygame.K_LEFT]:
            posicion_circulo[0] = posicion_circulo[0] - 0.05
        if lista_teclas[pygame.K_UP]:
            posicion_circulo[1] = posicion_circulo[1] - 0.05
        if lista_teclas[pygame.K_DOWN]:
            posicion_circulo[1] = posicion_circulo[1] + 0.05
    #fondo color
    pantalla.fill(COLOR_CELESTE)
    pygame.draw.circle(pantalla, COLOR_AMARILLO,posicion_circulo,80)
    #mostrar
    pygame.display.flip()
pygame.quit()


















































#SUPERFICIES 
#EVENTOS
#pygame maneja todos sus mensajes de eventos a traves de una cola de eventos
#pygame.event.get()


