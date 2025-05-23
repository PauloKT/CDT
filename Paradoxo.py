# Fabio Massucatto, Paulo Henrique, Felipe Shinkae, Heitor Cortes, Erick da Costa
import pygame
import math
import sys

# Função para converter segundos em anos
def converter_anos(segundos):
    return segundos / (60 * 60 * 24 * 365.25)

# Inicializa o pygame
pygame.init()

# Configurações da janela
largura, altura = 900, 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Viagem a Alpha Centauri 🚀")

# Cores
BRANCO = (255, 255, 255)
AZUL = (100, 149, 237)
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VERDE = (50, 205, 50)

# Fonte
fonte = pygame.font.SysFont("arial", 20)

# Objetos
terra_pos = (100, altura//2)
alpha_pos = (800, altura//2)
foguete_img = pygame.Surface((40, 20))
foguete_img.fill(VERDE)

# Variáveis físicas
distancia_anosluz = 4.37
distancia_metros = distancia_anosluz * 9.4607e15

# Input de velocidade
while True:
    try:
        perc = float(input("Com qual fração da velocidade da luz você quer viajar? (ex: 0.8 para 80%): "))
        if not (0 < perc < 1):
            print("Digite um valor entre 0 e 1 (não incluso)")
            continue
        break
    except ValueError:
        print("Valor inválido. Use ponto, exemplo: 0.9")

v = perc * 299792458  # velocidade da viagem

    v = perc * 299792458  # velocidade em m/s
    # Tempo para quem está na Terra (t = d/v)
    t_terra_seg = distancia_metros / v
    t_terra_anos = converter_anos(t_terra_seg)

    # Agora, calcule o tempo no foguete (tempo próprio)
    beta = perc
    gamma = 1 / math.sqrt(1 - beta**2)
    t_foguete_seg = t_terra_seg / gamma
    t_foguete_anos = converter_anos(t_foguete_seg)

# Simulação
pos_x = terra_pos[0]
vel_simulada = (alpha_pos[0] - terra_pos[0]) / (t_terra_anos * 60)  # pixels por frame (1 ano = 60 frames)

clock = pygame.time.Clock()
tempo_terra = 0
tempo_foguete = 0

rodando = True
while rodando:
    clock.tick(60)  # 60 FPS

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            pygame.quit()
            sys.exit()

    # Atualiza posição
    if pos_x < alpha_pos[0]:
        pos_x += vel_simulada
        tempo_terra += t_terra_anos / (t_terra_anos * 60)
        tempo_foguete = tempo_terra / gamma

    # Desenhar
    tela.fill(PRETO)

    # Desenha Terra e Alpha Centauri
    pygame.draw.circle(tela, AZUL, terra_pos, 30)
    pygame.draw.circle(tela, AMARELO, alpha_pos, 30)

    # Desenha foguete
    tela.blit(foguete_img, (pos_x, altura//2 - 10))

    # Textos
    texto1 = fonte.render(f"Tempo na Terra: {tempo_terra:.2f} anos", True, BRANCO)
    texto2 = fonte.render(f"Tempo no Foguete: {tempo_foguete:.2f} anos", True, BRANCO)
    texto3 = fonte.render(f"Velocidade: {perc*100:.0f}% da velocidade da luz", True, BRANCO)
    texto4 = fonte.render("Terra", True, BRANCO)
    texto5 = fonte.render("Alpha Centauri", True, BRANCO)

    tela.blit(texto1, (20, 20))
    tela.blit(texto2, (20, 50))
    tela.blit(texto3, (20, 80))
    tela.blit(texto4, (terra_pos[0]-20, terra_pos[1]+40))
    tela.blit(texto5, (alpha_pos[0]-50, alpha_pos[1]+40))

    pygame.display.update()

pygame.quit()
