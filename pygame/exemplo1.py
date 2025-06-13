import pygame # importando a biblioteca
pygame.init() # inicia o pygame
largura = 800
altura = 600 # define o tamanho da tela
tela = pygame.display.set_mode((largura, altura)) # cria a tela com as dimensoes especificadas
pygame.display.set_caption("Exemplo de jogo") # define o titulo da janela
radando = True # variavel para controlar o loop principal
while radando: # loop principal do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((255, 255, 255)) #preenche a tela com preto
    pygame.display.update() # atualiza a tela

pygame.quit() #Encerra a tela