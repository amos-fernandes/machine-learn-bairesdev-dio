import cv2
import numpy as np

def converter_para_tons_de_cinza(img):
    """Converte uma imagem colorida para tons de cinza.

    Args:
        img: A imagem colorida como um array NumPy.

    Returns:
        A imagem em tons de cinza como um array NumPy.
    """

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img

def binarizar_imagem(img, threshold=127):
    """Binariza uma imagem em tons de cinza.

    Args:
        img: A imagem em tons de cinza como um array NumPy.
        threshold: O valor do limiar para binarização.

    Returns:
        A imagem binarizada como um array NumPy.
    """

    _, binary_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return binary_img

# Carregando a imagem
img = cv2.imread('./01.jpeg')

# Convertendo para tons de cinza
gray_img = converter_para_tons_de_cinza(img)

# Binarizando a imagem
binary_img = binarizar_imagem(gray_img, threshold=127)  # Ajuste o limiar conforme necessário

# Mostrando as imagens
cv2.imshow('Original', img)
cv2.imshow('Tons de Cinza', gray_img)
cv2.imshow('Binarizada', binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
