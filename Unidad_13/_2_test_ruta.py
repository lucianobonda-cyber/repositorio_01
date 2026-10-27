# Cambia la ruta desde donde ejecutas el script
# Y verificar si encuentra o no la carpeta data

import os

# Ver el directorio de trabajo actual
print("Directorio actual (cwd):", os.getcwd())

# Construir rutas de forma segura con os.path.join
# Esto funciona en Windows, Mac y Linux sin cambios
ruta = os.path.join("data", "usuarios.json")
print("Ruta construida:", ruta)

# Verificar si un archivo o carpeta existe
print("¿Existe la carpeta 'data'?", os.path.exists("data"))