import pygame
import textArea
import random
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

listaPreguntas = ["¿De que pais es Messi?","¿Cuantos habitantes tiene Bolivia?","¿Que es PyGame?"]
listaRespuestas = ["Argentina","12 millones","Una libreria de Python","Narnia"]

#agregarALaLista
listaRespuestas.append("Fornite")
listaPreguntas.append("¿Cuantos años tiene Cristiano Ronaldo?")


preguntas = textArea.TextArea(0,0,500,30,pantalla,BLANCO)
preguntas.cambiarTexto("Pregunta:",25,NEGRO)

respuestas = textArea.TextArea(0,30,500,30,pantalla,BLANCO)
respuestas.cambiarTexto("Respuesta:",25,NEGRO)


def juego():
    
    
    while True:
        pantalla.fill(ROJO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    numero_random = random.randint(1,len(listaPreguntas))
                    preguntas.cambiarTexto("Pregunta:"+listaPreguntas[numero_random-1],25,NEGRO)
                    
                if event.key == pygame.K_a:
                   numero_random = random.randint(1,len(listaRespuestas))
                   respuestas.cambiarTexto("Respuesta:"+listaRespuestas[numero_random-1],25,NEGRO)
        
        preguntas.dibujar(0,0)
        respuestas.dibujar(0,0)
        pygame.display.update()

while True:
    pantalla.fill(BLANCO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                juego()

    presentacion_juego.dibujar(0,0)
    continuar.dibujar(0,0)
    pygame.display.update()