# Inversão de Valores de Matizes

Programa em Python que recebe uma imagem colorida e dois parâmetros numéricos
`H` e `d`, e devolve uma nova imagem com alguns valores de matiz (hue)
invertidos.

## Descrição do trabalho

O programa converte a imagem de entrada para o sistema de cor **HSV** e
processa somente a banda **H** (matiz). As bandas **S** (saturação) e **V**
(valor) são preservadas sem alteração.

Para todo matiz `h` pertencente ao intervalo `[H - d, H + d]`, o valor é
substituído por `h - 180`. Após essa substituição, a imagem é convertida de
volta para **RGB/BGR**.

**Parâmetros:**

| Parâmetro | Significado            | Intervalo válido |
|-----------|-------------------------|-------------------|
| `H`       | Matiz central            | `0` a `360`       |
| `d`       | Raio do intervalo         | `0` a `180`       |

**Observação sobre os ângulos:** como `H` e `d` definem um intervalo de
ângulos, é preciso cuidado especial com valores que caiam fora de
`[0, 360)` — tanto na definição do intervalo `[H-d, H+d]` (que pode cruzar
a fronteira 0°/360°, ex: `H=10, d=30` → intervalo `[340°, 360°) ∪ [0°, 40°]`)
quanto no resultado da subtração `h - 180` (que pode ficar negativo). Essa
normalização é feita pela função `normaliza_angulo`.

## Estrutura dos arquivos

O trabalho foi dividido em três módulos:

- **`hsv_utils.py`** — Funções auxiliares: normalização de ângulos e
  conversão entre os sistemas de cor RGB ↔ HSV (usando OpenCV), além de
  funções de leitura, gravação e exibição de imagens.
- **`hue_inversion.py`** — Lógica principal do trabalho: validação dos
  parâmetros, cálculo do intervalo `[H-d, H+d]` (com tratamento do
  cruzamento da fronteira 0°/360°) e a função `inverte_matizes`, que aplica
  a substituição `h → h - 180` nos pixels do intervalo.
- **`main.py`** — Ponto de entrada do programa, via linha de comando.

## Requisitos

- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/) (`opencv-python`)
- [NumPy](https://pypi.org/project/numpy/)

### Instalação das dependências

```bash
pip install opencv-python numpy
```

## Como executar

Os três arquivos (`hsv_utils.py`, `hue_inversion.py` e `main.py`) devem
estar na mesma pasta.

```bash
python main.py <entrada> <saida> <H> <d>
```

**Parâmetros da linha de comando:**

- `<entrada>` — caminho da imagem de entrada (ex: `foto.jpg`)
- `<saida>` — caminho onde a imagem resultante será salva (ex: `resultado.png`)
- `<H>` — matiz central, entre 0 e 360
- `<d>` — raio do intervalo, entre 0 e 180

**Exemplo:**

```bash
python main.py foto.png resultado.png 120 30
```

Esse comando inverte todos os matizes entre 90° e 150° (tons de verde) da
imagem `foto.png`, salva o resultado em `resultado.png` e exibe a imagem
original lado a lado com o resultado em janelas separadas.