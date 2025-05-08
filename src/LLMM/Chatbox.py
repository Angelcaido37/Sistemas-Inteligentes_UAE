#pip install beautifulsoup4
from bs4 import BeautifulSoup


def obtener_carreras_por_nivel():
    """Devuelve las carreras organizadas por nivel educativo y área."""
    niveles = {
        "Medio Superior": {
            "Preparatorias": [
                "UA Preparatoria 1 (Tepic)",
                "UA Preparatoria 2 (Santiago Ixcuintla)",
                "UA Preparatoria 3 (Acaponeta)",
                "UA Preparatoria 4 (Tecuala)",
                "UA Preparatoria 5 (Tuxpan)",
                "UA Preparatoria 6 (Ixtlán del Río)",
                "UA Preparatoria 7 (Compostela)",
                "UA Preparatoria 8 (Ahuacatlán)",
                "UA Preparatoria 9 (Villa Hidalgo)",
                "UA Preparatoria 10 (Valle de Banderas)",
                "UA Preparatoria 11 (Ruiz)",
                "UA Preparatoria 12 (San Blas)",
                "UA Preparatoria 13 (Tepic)",
                "UA Preparatoria 14. Modalidad Abierta"
            ]
        },
        "Superior": {
            "Área de Artes": ["Licenciatura en Artes"],
            "Área de Ciencias Básicas e Ingenierías": ["Ingeniería en Computación", "Ingeniería Civil"],
            "Área de Ciencias Biológico Agropecuarias y Pesqueras": ["Ingeniería en Agronomía", "Licenciatura en Biología"],
            "Área de Ciencias de la Salud": ["Medicina", "Odontología", "Enfermería"],
            "Área de Ciencias Económicas y Administrativas": ["Contaduría", "Administración", "Economía"],
            "Área de Ciencias Sociales y Humanidades": ["Derecho", "Psicología", "Comunicación"]
        },
        "Profesional Asociado": {
            "Área de Artes": ["Profesional Asociado en Música"]
        },
        "Posgrados": {
            "Área de Ciencias Sociales y Humanidades": ["Maestría en Ciencias Sociales"],
            "Área de Ciencias Económico Administrativas": ["Maestría en Administración"],
            "Área de Ciencias de la Salud": ["Maestría en Salud Pública"],
            "Área de Ciencias Biológico Agropecuarias": ["Maestría en Producción Animal"],
            "Área de Ciencias Básicas e Ingeniería": ["Maestría en Ingeniería"]
        }
    }
    return niveles

def mostrar_niveles(niveles):
    """Muestra los niveles educativos disponibles."""
    print("\nNiveles educativos disponibles:")
    for idx, nivel in enumerate(niveles.keys(), 1):
        print(f"{idx}. {nivel}")

def mostrar_areas(nivel, niveles):
    """Muestra las áreas disponibles para un nivel."""
    print(f"\nÁreas disponibles en el nivel {nivel}:")
    for idx, area in enumerate(niveles[nivel].keys(), 1):
        print(f"{idx}. {area}")

def mostrar_carreras(nivel, area, niveles):
    """Muestra las carreras disponibles en un nivel y área específicos."""
    print(f"\nCarreras disponibles en el área {area} del nivel {nivel}:")
    carreras = niveles[nivel][area]
    for carrera in carreras:
        print(f"- {carrera}")

def interactuar_con_usuario():
    """Interacción principal con el usuario."""
    niveles = obtener_carreras_por_nivel()

    print("Bienvenido al asistente de admisión de la UAN 2025.")
    while True:
        mostrar_niveles(niveles)
        nivel_idx = int(input("\nElige un nivel (ingresa el número correspondiente o escribe '0' para salir): "))
        if nivel_idx == 0:
            print("Gracias por utilizar el asistente de admisión. ¡Éxito en tu proceso!")
            break

        nivel = list(niveles.keys())[nivel_idx - 1]
        mostrar_areas(nivel, niveles)
        area_idx = int(input("\nElige un área (ingresa el número correspondiente o escribe '0' para regresar): "))
        if area_idx == 0:
            continue

        area = list(niveles[nivel].keys())[area_idx - 1]
        mostrar_carreras(nivel, area, niveles)
        input("\nPresiona Enter para continuar o escribe 'salir' para terminar: ")
        if input().strip().lower() == 'salir':
            print("Gracias por utilizar el asistente de admisión. ¡Éxito en tu proceso!")
            break

def main():
    """Función principal del programa."""
    interactuar_con_usuario()

if __name__ == "__main__":
    main()
