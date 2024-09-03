import os
import shutil
import logging
from datetime import datetime

# Configuración del log
logging.basicConfig(filename='file_organizer.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Directorio a organizar
directory = 'C:/Users/Equipo/Downloads'

# Tipos de archivos y carpetas correspondientes
file_types = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Audio': ['.mp3', '.wav'],
    'Others': []
}

# Función para organizar archivos
def organize_files():
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Ignorar directorios
        if os.path.isdir(file_path):
            continue
        
        # Clasificar archivos por extensión
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False
        
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                move_file(file_path, folder)
                moved = True
                break
        
        # Archivos sin categoría
        if not moved:
            move_file(file_path, 'Others')

# Función para mover archivos
def move_file(file_path, folder_name):
    folder_path = os.path.join(directory, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Crea la carpeta si no existe
    
    shutil.move(file_path, os.path.join(folder_path, os.path.basename(file_path)))
    logging.info(f'Movido: {file_path} -> {folder_name}')

# Ejecutar la función
if __name__ == "__main__":
    organize_files()
    print(f"Archivos organizados en {directory}. Revisa el archivo log para más detalles.")
