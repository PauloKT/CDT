
import math

def converter_anos(segundos):
    return segundos / (60 * 60 * 24 * 365.25)

def main():
    print("\n=== Viagem Fictícia a Alpha Centauri ===\n")
    print("Imagine que você pode viajar MUITO RÁPIDO até Alpha Centauri,")
    print("a estrela mais próxima do nosso Sol, a 4,37 anos-luz de distância!\n")
    print("Você vai ver quanto tempo se passa para você (no foguete)")
    print("e quanto passa para quem ficou na Terra.\n")
    print("Vamos começar!\n")

    distancia_anosluz = 4.37
    distancia_metros = distancia_anosluz * 9.4607e15

    while True:
        try:
            perc = float(input("Com qual fração da velocidade da luz você quer viajar? (ex: 0.8 para 80 por cento da velocidade da luz): "))
            if not (0 < perc < 1):
                print("A fração deve ser maior que 0 e menor que 1!")
                continue
            break
        except ValueError:
            print("Digite um número válido, por exemplo 0.9")

    v = perc * 299792458  # velocidade em m/s
    # Tempo para quem está na Terra (t = d/v)
    t_terra_seg = distancia_metros / v
    t_terra_anos = converter_anos(t_terra_seg)

    # Agora, calcule o tempo no foguete (tempo próprio)
    beta = perc
    gamma = 1 / math.sqrt(1 - beta**2)
    t_foguete_seg = t_terra_seg / gamma
    t_foguete_anos = converter_anos(t_foguete_seg)

    print("\n--- RESULTADOS ---")
    print(f"Distância a Alpha Centauri:      {distancia_anosluz:.2f} anos-luz")
    print(f"Velocidade da viagem:            {perc*100:.0f}% da velocidade da luz")
    print(f"\nPara quem ficou na Terra, a viagem dura:   {t_terra_anos:.2f} anos")
    print(f"Para você, dentro do foguete:              {t_foguete_anos:.2f} anos")

    print("\n>> Veja só: para você, a viagem parece DURAR MENOS do que para quem ficou na Terra!")
    print("Esse é o famoso 'paradoxo dos gêmeos' da relatividade especial.")
    print("Quanto mais rápido você viaja, menor é o tempo PASSADO para você!\n")

    print("Experimente rodar de novo com diferentes velocidades. Divirta-se! 🚀\n")

if __name__ == "__main__":
 main()
