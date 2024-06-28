import os
import cv2

def binary_thresholding(img, threshold, inv=False):
    if inv:
        ret, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)
    else:
        ret, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return img

def resize_image(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim)
    return resized

def load_file():
    """
    Carga una imagen desde el directorio actual y la muestra después de aplicar umbralización y redimensionamiento.
    """
    try:
        file_name = "diome.jpg"
        path = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(path, file_name)
        
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise FileNotFoundError("No se pudo cargar la imagen.")
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        return None
    
    img_thresh = binary_thresholding(img, 127, inv=True)
    result = resize_image(img_thresh, 50)
    matrix = result / 255

    return result, matrix

image, matrix = load_file()
print(matrix)  # Imprimir la matriz resultante

cv2.imshow('Imagen', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

