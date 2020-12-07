import pygame


class Tela:
    def __init__(self):
        pygame.init()
        self.janela = pygame.display.set_mode((1365, 700))
        pygame.display.set_caption('Pong Solitario')
        self.delimitador_x_direita = 1215
        self.delimitador_x_esquerda = 50
        self.delimitador_y_baixo = 595
        self.delimitador_y_cima = 50
        self.font = pygame.font.Font('freesansbold.ttf', 30)

        self.borda_vertical_esquerda = pygame.draw.rect(self.janela, (255, 0, 0), (0, 0, 50, 700))
        self.borda_vertical_direita = pygame.draw.rect(self.janela, (255, 0, 0), (1315, 0, 50, 700))
        self.borda_horizontal_cima = pygame.draw.rect(self.janela, (255, 0, 0), (0, 0, 1315, 50))
        self.borda_horizontal_baixo = pygame.draw.rect(self.janela, (255, 0, 0), (0, 650, 1315, 50))

        self.lista_de_paredes = [
            self.borda_vertical_esquerda, self.borda_vertical_direita,
            self.borda_horizontal_cima, self.borda_horizontal_baixo,
            ]

    def desenhando_bordas(self):
        self.borda_vertical_esquerda = pygame.draw.rect(self.janela, (255, 0, 0), (0, 0, 50, 700))
        self.borda_vertical_direita = pygame.draw.rect(self.janela, (255, 0, 0), (1315, 0, 50, 700))
        self.borda_horizontal_cima = pygame.draw.rect(self.janela, (255, 0, 0), (0, 0, 1315, 50))
        self.borda_horizontal_baixo = pygame.draw.rect(self.janela, (255, 0, 0), (0, 650, 1315, 50))

    def colisao(self, usuario, bola):
        if pygame.Rect.colliderect(usuario.corpo, bola.corpo):
            bola.movendo_bola_baixo = False
            bola.velocidade += 0.02
            usuario.tocando_bola.play()

        if pygame.Rect.colliderect(bola.corpo, self.borda_horizontal_baixo):
            bola.coordenada_y = 300
            bola.movendo_bola_baixo = False
            usuario.pontos -= 1
            bola.velocidade = 1
            bola.tocando_o_solo.play()
            pygame.time.delay(1700)

        if pygame.Rect.colliderect(bola.corpo, self.borda_horizontal_cima):
            bola.tocando_as_paredes.play()

        if pygame.Rect.colliderect(bola.corpo, self.borda_vertical_direita):
            bola.tocando_as_paredes.play()

        if pygame.Rect.colliderect(bola.corpo, self.borda_vertical_esquerda):
            bola.tocando_as_paredes.play()

    def mostrando_velocidade_da_bola(self, bola):
        texto = self.font.render(f'Velocidade: {str(bola.velocidade)[0:3]}', True, (255, 0, 0))
        self.janela.blit(texto, (60, 60))

    @staticmethod
    def atualizando_tela():
        pygame.display.update()
