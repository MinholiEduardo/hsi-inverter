# Arquivo para a inversao da Matiz

import numpy as np
from auxiliaries import normaliza_angulo, bgr_para_hsv, hsv_para_bgr

def valida_parametros(H, d):
    """Valida os parametros H e d."""
    if not (0 <= H <= 360):
        raise ValueError("H deve estar entre 0 e 360.")
    if not (0 <= d <= 180):
        raise ValueError("d deve estar entre 0 e 180.")

def calcula_mascara_intervalo(H_band, H, d):
    """
    Calcula a mascara dos pixels cujo matiz h esta em [H-d, H+d],
    tratando o caso em que o intervalo cruza a fronteira 0/360.
    """
    if d >= 180:
        return np.ones_like(H_band, dtype=bool)


    h_min = normaliza_angulo(H - d)
    h_max = normaliza_angulo(H + d)

    if h_min <= h_max:
        mascara = (H_band >= h_min) & (H_band <= h_max)
    else:
        mascara = (H_band >= h_min) | (H_band <= h_max)

    return mascara

def inverte_banda_h(H_band, H, d):
    """
    Recebe a banda H em graus, [0,360)) e devolve uma nova banda H
    com os matizes do intervalo [H-d, H+d] substituidos por h - 180.
    """
    mascara = calcula_mascara_intervalo(H_band, H, d)

    H_novo = H_band.copy()
    H_novo[mascara] = normaliza_angulo(H_band[mascara] - 180)

    return H_novo

def inverte_matizes(imagem_bgr, H, d):
    """
    Recebe uma imagem BGR e os parametros
    H e d, e devolve uma nova imagem BGR com os matizes invertidos no
    intervalo [H-d, H+d]. As bandas S e V sao preservadas.
    """
    valida_parametros(H, d)

    # Converte para HSV
    hsv = bgr_para_hsv(imagem_bgr)
    H_band = hsv[:, :, 0]
    S_band = hsv[:, :, 1]
    V_band = hsv[:, :, 2]

    # Processa somente a banda H
    H_novo = inverte_banda_h(H_band, H, d)

    # Reconstroi o HSV (S e V preservados) e converte de volta para BGR
    hsv_novo = np.stack([H_novo, S_band, V_band], axis=-1)
    return hsv_para_bgr(hsv_novo)
