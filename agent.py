import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carga de seguridad
load_dotenv()

# Configuración de la API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Usamos el nombre más estándar y compatible: 'gemini-1.5-flash'
# Este nombre funciona en casi todas las versiones de la API
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_plan(tasks):
    tasks_text = str(tasks)
    
    prompt = f"""
    Eres un experto en productividad. Analiza estas tareas: {tasks_text}
    
    Genera:
    1. Prioridad (basada en deadline y duración).
    2. Plan semanal.
    3. Razonamiento breve.
    
    Formato:
    Prioridad: ...
    Plan semanal: ...
    Razón: ...
    """

    try:
        # Llamada directa
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error en la comunicación: {str(e)}"