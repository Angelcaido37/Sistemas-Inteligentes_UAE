import os

def generar_arbol(path, prefijo=""):
    estructura = ""
    archivos = sorted(os.listdir(path))
    for i, archivo in enumerate(archivos):
        ruta_completa = os.path.join(path, archivo)
        conector = "└── " if i == len(archivos) - 1 else "├── "
        estructura += f"{prefijo}{conector}{archivo}\n"
        if os.path.isdir(ruta_completa) and archivo != '.venv' and not archivo.startswith('.'):
            nuevo_prefijo = prefijo + ("    " if i == len(archivos) - 1 else "│   ")
            estructura += generar_arbol(ruta_completa, nuevo_prefijo)
    return estructura

estructura = generar_arbol(".")

contenido_md = "## 📁 Sistemas Inteligentes\n\n"
contenido_md += "```\n"
contenido_md += estructura
contenido_md += "```\n"

# Guardar en archivo .md
with open("/Proyectos Algoritmos/Sistemas Inteligentes/README.md", "w", encoding="utf-8") as f:
    f.write(contenido_md)

"README.md"
