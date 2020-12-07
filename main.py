#!/usr/bin/env python3.7
import pygame
import sys

from definicoes_de_tela import Tela
from bola import Bola
from usuario import Usuario


tela = Tela()
bola = Bola()
usuario = Usuario()

while True:
    tela.janela.fill((0, 0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                usuario.movendo_direita = True
                usuario.movendo_esquerda = False
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                usuario.movendo_esquerda = True
                usuario.movendo_direita = False
            if evento.key == pygame.K_SPACE:
                usuario.velocidade = 2

        if evento.type == pygame.KEYUP:
            usuario.velocidade = 1.3

    # Movendo usuario
    if usuario.movendo_direita and usuario.coordenada_x < tela.delimitador_x_direita:
        usuario.coordenada_x += usuario.velocidade
    if usuario.movendo_esquerda and usuario.coordenada_x > tela.delimitador_x_esquerda:
        usuario.coordenada_x -= usuario.velocidade

    # Desenhando o usuario
    usuario.corpo = pygame.draw.rect(tela.janela, (0, 0, 255), (usuario.coordenada_x, usuario.coordenada_y, 100, 50))

    # Desenhando a bola
    bola.corpo = pygame.draw.circle(tela.janela, (255, 0, 0), (bola.coordenada_x, bola.coordenada_y), 15, 14)
    # Movimentando a bola
    bola.movimentando_bola_horizontal(tela)
    bola.movimentando_bola_vertical(tela)

    tela.colisao(usuario, bola)

    tela.desenhando_bordas()
    tela.mostrando_velocidade_da_bola(bola)
    tela.atualizando_tela()
