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


#SUPERFICIES 
#EVENTOS
#pygame maneja todos sus mensajes de eventos a traves de una cola de eventos
#pygame.event.get()


