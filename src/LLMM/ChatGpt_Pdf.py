import os
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer
from sentence_transformers import SentenceTransformer
import gradio as gr
from PyPDF2 import PdfReader
from docx import Document
from tqdm import tqdm
from sklearn.neighbors import NearestNeighbors

# Configuración inicial
MAX_CHARACTERS = 5000
BATCH_SIZE = 5

# Cargar el modelo de lenguaje y el tokenizador
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")

# Cargar el modelo de embeddings
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Función para leer PDF
def process_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text.strip()[:MAX_CHARACTERS]

# Función para leer DOCX
def process_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text.strip()[:MAX_CHARACTERS]

# Dividir en párrafos
def split_into_paragraphs(text):
    return [p.strip() for p in text.split("\n") if p.strip()]

# Procesar documentos
directory = "./documentos"
documents = []
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if file_name.endswith(".pdf"):
        documents.extend(split_into_paragraphs(process_pdf(file_path)))
    elif file_name.endswith(".docx"):
        documents.extend(split_into_paragraphs(process_docx(file_path)))

if not documents:
    raise ValueError("No se encontraron documentos en el directorio especificado.")

# Generar embeddings
def generate_embeddings_in_batches(docs, batch_size=5):
    embeddings = []
    for i in tqdm(range(0, len(docs), batch_size)):
        batch = docs[i:i + batch_size]
        embeddings.extend(embedding_model.encode(batch))
    return np.array(embeddings)

document_embeddings = generate_embeddings_in_batches(documents, batch_size=BATCH_SIZE)

# Indexar con sklearn
index = NearestNeighbors(n_neighbors=1, metric="euclidean")
index.fit(document_embeddings)

# Obtener contexto relevante
def get_relevant_context(paragraph_index, documents, context_size=2):
    start_index = max(0, paragraph_index - context_size)
    end_index = min(len(documents), paragraph_index + context_size + 1)
    return "\n".join(documents[start_index:end_index])

# Chatbot
def chatbot(user_input):
    try:
        if not user_input:
            return "Por favor, ingresa una pregunta o comentario.", "robot_thinking.gif"
        query_embedding = embedding_model.encode([user_input])
        distances, indices = index.kneighbors(query_embedding)
        if len(indices[0]) == 0 or indices[0][0] == -1:
            return "No se encontró información relevante.", "robot_thinking.gif"
        paragraph_index = indices[0][0]
        relevant_context = get_relevant_context(paragraph_index, documents)
        return f"Contenido relevante:\n{relevant_context}", "robot_searching.gif"
    except Exception as e:
        return f"Error en el chatbot: {str(e)}", "robot_error.gif"

# Interfaz Gradio
css = """
#robot-image img {
    width: 200px;
    height: auto;
    margin: 0 auto;
    display: block;
    animation: pulse 2s infinite;
    border-radius: 50%;
    object-fit: cover;
    background: none;
}
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}
"""

with gr.Blocks(css=css) as iface:
    gr.Markdown("# Chatbot Inteligente Personalizado")
    user_input = gr.Textbox(lines=2, placeholder="Escribe tu pregunta aquí...", label="Pregunta")
    response_output = gr.Textbox(label="Respuesta del Chatbot")
    robot_image = gr.Image(value="robot_thinking.gif", label="Estado del chatbot", elem_id="robot-image")
    submit_button = gr.Button("Enviar")
    clear_button = gr.Button("Limpiar")
    submit_button.click(chatbot, inputs=user_input, outputs=[response_output, robot_image])
    clear_button.click(lambda: "", None, user_input)
    clear_button.click(lambda: "", None, response_output)
    clear_button.click(lambda: "robot_thinking.gif", None, robot_image)

iface.launch()
