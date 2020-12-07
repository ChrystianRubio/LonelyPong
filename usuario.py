import pygame


class Usuario:
    def __init__(self):
        self.corpo = ''
        self.coordenada_x = 200
        self.coordenada_y = 595
        self.movendo_esquerda = self.movendo_direita = False
        self.rect = 0
        self.pontos = 3
        self.velocidade = 1.3
        self.tocando_bola = pygame.mixer.Sound('Sons/ping.wav')
