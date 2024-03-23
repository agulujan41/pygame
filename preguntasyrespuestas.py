import pygame
import textArea
pygame.init()

#PANTALLA
ANCHO = 500
ALTO = 500
DIMENSION = (ANCHO,ALTO)


pantalla = pygame.display.set_mode(DIMENSION)
pygame.display.set_caption("Preguntas y Respuestas")
#COLORES
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
NEGRO = (0,0,0)
BLANCO = (255,255,255)

presentacion_juego = textArea.TextArea(0,0,500,100,pantalla,BLANCO)
presentacion_juego.cambiarTexto("Bienvenidos al juego",70,NEGRO)
continuar = textArea.TextArea(0,200,500,100,pantalla,BLANCO)
continuar.cambiarTexto("Presiona la letra ESPACIO para continuar",30,AZUL)
def juego():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pantalla.fill(ROJO)
        pygame.display.update()

while True:
    pantalla.fill(BLANCO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Espacio")
                juego()

    presentacion_juego.dibujar(0,0)
    continuar.dibujar(0,0)
    pygame.display.update()