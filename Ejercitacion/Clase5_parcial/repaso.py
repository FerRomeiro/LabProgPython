#Rectangulos
#pygame usa objetos Rect para almacenar y manuipular areas rectangulaes. Son contenedores de los objetos que vamos a trabajar, se acrean a partir de dmiensaiones
#de ancho, alto y la posicion respecto al lado izquierdo y superior de un objeto.
#pygame.Rect(left,top,width,height)
#en cada juego, cada objeto requiere un conjunto de limites fijos que definen el espacio q ocupa.
#estos limites fijos son esenciales cuando el objeto interactua o choca con otros objetos.
#en pygame se crean rectangulos alrededor de los objetos para definir los limites
#La forma mas basica de crear un objeto Rect en pygame es simplemente pasar 2 tuplas
#la primera tupla izquierda, arriba representa la posicion del Rect en la ventana mientras que la segunda tupla ancho y alto
#represente la dimensiones del REct
#
#rectangulo=pygame.rect((30,30),(60,60))
#
#tambien es posible objetenr un objeto un objeto Rect de una superficie y manipularlo
#imagen_dona=pygame.image.load("00.png")
#rect_dona=image_dona.get_rect()
#rect_dona.centerx=200
#rect_dona.centery=100
#print(rect_dona.width)


#Colisiones: es chocar que se toquen, la forma mas sencilla de comprobar colisiones es ver si se solapan los rectangulos de las distintas superficies
#En pygame se crean rectangulos que nos sirven para fijar los limites de los objetos
#Para cada rectangulo es posible comprobar si colisiona con otro
#if rect_player.colliderect(rect_piedra): #elobjetodelpersonaje.metododecolision(rectangulo)
#   print("Eljugador colisiona con la piedra")
#if rect_player.colliderect(rect_fuego):
#   print("El jugador colisiona con el fuego")

##es posible comprobar si un rectangulo colisiona con algun otro rectangulo de una lista de rectangulo
#if rect_player.collidelist()
#tambien es posible comprobar si colisiona una superficie con una coordenada
#if event.type==pygane_MOUSEBUTTONDOWN:
    #if rect_player.collide
#SONIDOS:
#los formatos de archivos de sonidos que pygame soporta son mid,wav,y mp3
#si al play se le pasa -1 como argumento, se va a reproducir el sonido de manera indefinida
#pygame.mixer.init()
#pygame.mixer.music.set_volume
#
#SPRITES:
#en terminos de progrmacion una sprite es una representacion 2D de algo de la pantalla.
#esencialmente, es una imgen. pygame proporciona una clase Sprite que esta diseñada para contener una o varias representaciones graficas 
#



