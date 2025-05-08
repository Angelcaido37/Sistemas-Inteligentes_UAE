import json

# Cargar la base de conocimientos desde un archivo JSON
def cargar_base_conocimientos():
    with open("src/Sistemas Inteligentes/Otros/base_conocimientos_uan.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Responder preguntas relacionadas con el proceso de admisión
def responder_pregunta_admision(base, pregunta):
    if "examen" in pregunta.lower():
        return base["proceso_admision"]["examen"]
    elif "promedio" in pregunta.lower():
        return base["proceso_admision"]["promedio"]
    elif "requisitos" in pregunta.lower():
        return "\n".join(base["proceso_admision"]["requisitos"])
    elif "registro" in pregunta.lower():
        registro = base["proceso_admision"]["registro"]
        return f"Plazo: {registro['plazo']}\nPágina: {registro['pagina']}\nDocumentos necesarios:\n- " + "\n- ".join(registro["documentos_necesarios"])
    elif "pago" in pregunta.lower():
        pago = base["proceso_admision"]["pago"]
        return f"Monto: {pago['monto']}\nPlazo: {pago['plazo']}\nOpciones:\n- " + "\n- ".join(pago["opciones"])
    elif "contacto" in pregunta.lower():
        contacto = base["contacto"]
        return f"Teléfono: {contacto['telefono']}\nCorreo: {contacto['correo']}\nDirección: {contacto['direccion']}"
    else:
        return "Lo siento, no tengo información sobre eso. Por favor, consulta el sitio web oficial: https://www.uan.edu.mx/."

def interactuar_con_usuario(base):
    """Interacción principal con el usuario."""
    print("Bienvenido al asistente de admisión de la UAN 2025.")
    while True:
        pregunta = input("\n¿Qué información necesitas? (Escribe 'salir' para terminar): ")
        if pregunta.strip().lower() == 'salir':
            print("Gracias por utilizar el asistente de admisión. ¡Éxito en tu proceso!")
            break
        respuesta = responder_pregunta_admision(base, pregunta)
        print(f"\n{respuesta}")

def main():
    """Función principal del programa."""
    base_conocimientos = cargar_base_conocimientos()
    interactuar_con_usuario(base_conocimientos)
exa
if __name__ == "__main__":
    main()
