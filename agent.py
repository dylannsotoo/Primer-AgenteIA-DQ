import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configuración forzando la versión estable de la API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"), transport='rest')

# Intentamos con el nombre más básico y seguro
model = genai.GenerativeModel('models/gemini-1.5-flash')

def generate_plan(tasks):
    tasks_text = str(tasks)
    
    prompt = f"""
    Eres un experto en gestión del tiempo. Analiza estas tareas: {tasks_text}
    
    Genera un plan con este formato:
    1. Prioridad: (Lista de tareas de más a menos importante)
    2. Plan semanal: (Distribución de lunes a domingo)
    3. Razón: (Breve explicación de por qué esa prioridad)
    """

    try:
        # Aquí pedimos el contenido
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Si falla la IA, devolvemos un plan de respaldo para que el archivo no esté vacío
        return "Plan de respaldo (Error de API):\n1. Priorizar tareas con menor deadline.\n2. Realizar tareas largas primero."