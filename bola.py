import pygame


class Bola:
    def __init__(self):
        self.coordenada_x = 200
        self.coordenada_y = 410
        self.velocidade = 1
        self.movendo_bola_esquerda = False
        self.movendo_bola_direita = False
        self.movendo_bola_cima = False
        self.movendo_bola_baixo = False
        self.tocando_o_solo = pygame.mixer.Sound('Sons/fail.wav')
        self.tocando_as_paredes = pygame.mixer.Sound('Sons/ball.wav')

    def movimentando_bola_horizontal(self, tela):
        if self.coordenada_x <= tela.delimitador_x_direita + 86 and not self.movendo_bola_esquerda:

            self.movendo_bola_direita = True
        else:
            self.movendo_bola_direita = False

        if self.coordenada_x >= tela.delimitador_x_esquerda + 15 and not self.movendo_bola_direita:

            self.movendo_bola_esquerda = True
        else:
            self.movendo_bola_esquerda = False

        if self.movendo_bola_direita:
            self.coordenada_x += self.velocidade
        if self.movendo_bola_esquerda:
            self.coordenada_x -= self.velocidade

    def movimentando_bola_vertical(self, tela):
        if self.coordenada_y >= tela.delimitador_y_cima + 15 and not self.movendo_bola_baixo:

            self.movendo_bola_cima = True
        else:
            self.movendo_bola_cima = False

        if self.coordenada_y <= tela.delimitador_y_baixo + 60 and not self.movendo_bola_cima:

            self.movendo_bola_baixo = True
        else:
            self.movendo_bola_baixo = False

        if self.movendo_bola_cima:
            self.coordenada_y -= self.velocidade
        if self.movendo_bola_baixo:
            self.coordenada_y += self.velocidade
