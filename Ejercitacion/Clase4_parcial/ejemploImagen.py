import pygame
#iniciar la pantalla
pygame.init()
#COLORES
ANCHO_VENTANA = 500
ALTO_VENTANA = 500
COLOR_CELESTE = ( 0, 0,128)
#POSICIONES
posicion_messi = [30, 100]
posicion_pasto = (0, 0)

#TEXTO
font = pygame.font.SysFont("Arial Narrow", 50)


#IMAGENES
imagen_messi = pygame.image.load("messi.png")
imagen_messi = pygame.transform.scale(imagen_messi,(200,200)) #puedo cambiar el tamaño de la imagen
imagen_pasto = pygame.image.load("pasto.jpg")
imagen_pasto = pygame.transform.scale(imagen_pasto,(500,500))
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
        if evento.type == pygame.MOUSEBUTTONDOWN:
            #print(evento.pos)
            posicion_messi = evento.pos

    #fondo color
    
    
    #print(type(text))

    pantalla.fill(COLOR_CELESTE)
    pantalla.blit(imagen_pasto,(posicion_pasto))
    pantalla.blit(imagen_messi,(posicion_messi))  #fundir la imagen en una superficie
    text = font.render("3 estrellas", True, (255, 0, 0))
    pantalla.blit(text,(50,50))
    #mostrar
    pygame.display.flip()
pygame.quit()