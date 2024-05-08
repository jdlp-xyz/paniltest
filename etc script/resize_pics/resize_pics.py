from PIL import Image
import os

def resize_and_convert_to_jpg(input_folder, output_folder, max_size=1500):
    # Comprueba si la carpeta de salida existe, si no, la crea
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lista todos los archivos en la carpeta de entrada
    files = os.listdir(input_folder)

    # Itera sobre cada archivo en la carpeta de entrada
    for file_name in files:
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.jpg')

        # Abre la imagen
        image = Image.open(input_path)

        # Obtiene las dimensiones de la imagen
        width, height = image.size

        # Calcula la escala para redimensionar la imagen
        if width >= height:
            ratio = max_size / width
        else:
            ratio = max_size / height

        # Redimensiona la imagen
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        resized_image = image.resize((new_width, new_height))

        # Guarda la imagen redimensionada como JPEG
        resized_image.save(output_path, 'JPEG')

        print(f"Imagen {file_name} redimensionada y convertida a JPEG")

# Ruta de la carpeta de entrada y salida
input_folder = r'D:\loreto\panil-web\mat\entrega-1\fotos\fotos\seleccion'
output_folder = r'D:\loreto\panil-web\mat\entrega-1\fotos\fotos\seleccion\comp'

# Llama a la función para redimensionar y convertir las imágenes
resize_and_convert_to_jpg(input_folder, output_folder)
