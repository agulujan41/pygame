import pygame
class TextArea():
    def __init__(self,x,y,ancho,alto,pantalla,color):
        self.x = x
        self.y = y
        self.ancho = ancho 
        self.alto = alto
        self.crearRectangulo(x,y,ancho,alto)
        self.pantalla = pantalla 
        self.colorFondo = color
    def crearRectangulo(self,x,y,ancho,alto):
        self.rect= pygame.Rect(x,y,ancho,alto)

    def cambiarTexto(self,texto,tamanio,colorLetra):
        self.texto = texto
        self.imagen = pygame.font.Font(None,tamanio).render(texto,True,colorLetra)
    def dibujar(self,cambiarx,cambiary):
        pygame.draw.rect(self.pantalla,self.colorFondo,self.rect)
        self.pantalla.blit(self.imagen,(self.rect.x+ cambiarx,self.rect.y+cambiary))