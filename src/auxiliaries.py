# Arquivo para funcoes auxiliares

import cv2
import numpy as np

def normaliza_angulo(h):
    """
    Garante que um angulo fique no intervalo [0, 360).
    """
    return np.mod(h, 360)

def bgr_para_hsv(imagem_bgr):
    """
    Converte uma imagem BGR para HSV.

    Trabalhamos com a imagem normalizada em float32 em vez do padrao do opencv
    porque, dessa maneira, o canal H e entregue diretamente em graus (0-360), 
    preservando a precisao necessaria para os calculos do intervalo [H-d, H+d].
    """
    img_float = imagem_bgr.astype(np.float32) / 255.0
    hsv = cv2.cvtColor(img_float, cv2.COLOR_BGR2HSV)
    return hsv

def hsv_para_bgr(imagem_hsv):
    """
    Converte uma imagem HSV (float32, H em [0,360), S e V em [0,1])
    de volta para BGR.
    """
    bgr_float = cv2.cvtColor(imagem_hsv.astype(np.float32), cv2.COLOR_HSV2BGR)
    bgr_uint8 = np.clip(bgr_float * 255.0, 0, 255).astype(np.uint8)
    return bgr_uint8

def carrega_imagem(caminho):
    """Le uma imagem colorida do disco no formato BGR."""
    imagem = cv2.imread(caminho, cv2.IMREAD_COLOR)
    if imagem is None:
        raise FileNotFoundError(f"Nao foi possivel abrir a imagem '{caminho}'.")
    return imagem

def salva_imagem(caminho, imagem_bgr):
    """Salva uma imagem BGR no disco."""
    cv2.imwrite(caminho, imagem_bgr)

def exibe_imagens(pares_titulo_imagem):
    """
    Exibe uma ou mais imagens em janelas separadas.

    pares_titulo_imagem: lista de tuplas (titulo, imagem_bgr)
    """
    for titulo, imagem in pares_titulo_imagem:
        cv2.imshow(titulo, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()