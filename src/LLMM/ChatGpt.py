import os
import faiss
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer
from sentence_transformers import SentenceTransformer
import gradio as gr

# Cargar el modelo de lenguaje y el tokenizador
#Se puede utilizar distilgpt2, gpt2
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")

# Cargar el modelo de embeddings
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Leer y preparar tus datos
try:
    with open("tus_datos.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
except FileNotFoundError:
    raise FileNotFoundError("El archivo 'tus_datos.txt' no se encontró en el directorio actual.")

documents = [doc.strip() for doc in data if doc.strip() != ""]

# Verificar que la lista de documentos no esté vacía
if not documents:
    raise ValueError("La lista de documentos está vacía. Por favor, agrega contenido a 'tus_datos.txt'.")

print(f"Documents loaded: {documents}")
print(f"Number of documents: {len(documents)}")

# Generar embeddings para los documentos
try:
    document_embeddings = embedding_model.encode(documents)
    print(f"Document embeddings shape: {document_embeddings.shape}")
except Exception as e:
    raise RuntimeError(f"Error al generar embeddings: {str(e)}")

# Crear el índice FAISS
try:
    embedding_dim = document_embeddings.shape[1]
    index = faiss.IndexFlatL2(embedding_dim)
    index.add(document_embeddings)
    print(f"Índice FAISS creado con {index.ntotal} documentos.")
except Exception as e:
    raise RuntimeError(f"Error al crear el índice FAISS: {str(e)}")

# Función del chatbot
def chatbot(user_input):
    try:
        if not user_input:
            return "Por favor, ingresa una pregunta o comentario."

        # Recuperar los 3 documentos más similares
        k = 3
        query_embedding = embedding_model.encode([user_input])
        distances, indices = index.search(query_embedding, k)
        relevant_docs = [documents[i] for i in indices[0]]

        # Construir contexto con documentos relevantes
        context = " ".join(relevant_docs[:2])  # Usar los dos primeros documentos relevantes
        print(f"Contexto generado: {context}")

        # Generar respuesta basada en el contexto y la entrada del usuario
        input_text = f"{context}\nUsuario: {user_input}\nChatbot:"
        input_ids = tokenizer.encode(input_text, return_tensors="pt")
        output = model.generate(
            input_ids,
            max_length=200,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            early_stopping=True,
            temperature=0.7,
            top_k=50,
            top_p=0.9
        )
        response = tokenizer.decode(output[0], skip_special_tokens=True)

        # Limpiar la respuesta generada
        clean_response = response.replace(f"Usuario: {user_input}", "").replace("Chatbot:", "").strip()
        clean_response = " ".join(clean_response.split())  # Eliminar espacios extra
        print(f"Respuesta generada: {clean_response}")

        return clean_response

    except Exception as e:
        return f"Error en el chatbot: {str(e)}"

# Crear la interfaz de usuario con botones personalizados
with gr.Blocks() as iface:
    gr.Markdown("# Chatbot Inteligente Personalizado")
    gr.Markdown("Este chatbot está diseñado para responder preguntas basadas en tu propio conjunto de datos.")
    
    with gr.Row():
        user_input = gr.Textbox(lines=2, placeholder="Escribe tu pregunta aquí...", label="Pregunta")
        response_output = gr.Textbox(label="Respuesta del Chatbot")

    with gr.Row():
        submit_button = gr.Button("Enviar")
        clear_button = gr.Button("Limpiar")

    # Conectar botones con acciones
    submit_button.click(chatbot, inputs=user_input, outputs=response_output)
    clear_button.click(lambda: "", None, user_input)  # Limpiar la entrada
    clear_button.click(lambda: "", None, response_output)  # Limpiar la salida

# Ejecutar la aplicación
iface.launch()

