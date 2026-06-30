import sys

from auxiliaries import carrega_imagem, salva_imagem, exibe_imagens
from inversao_matiz import inverte_matizes

def main():
    if len(sys.argv) != 5:
        print("Uso: python src/main.py <entrada> <saida> <H> <d>")
        sys.exit(1)

    caminho_entrada = sys.argv[1]
    caminho_saida = sys.argv[2]
    H = float(sys.argv[3])
    d = float(sys.argv[4])

    imagem = carrega_imagem(caminho_entrada)
    resultado = inverte_matizes(imagem, H, d)

    salva_imagem(caminho_saida, resultado)
    print(f"Imagem salva em: {caminho_saida}")

    exibe_imagens([("Original", imagem), ("Matizes invertidas", resultado)])

if __name__ == "__main__":
    main()
