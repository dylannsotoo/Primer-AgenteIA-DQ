import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carga de seguridad de las variables de entorno
load_dotenv()

# Configuración de la API forzando transporte estable 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"), transport='rest')

# Usamos el modelo que confirmamos que tienes disponible en tu lista
model = genai.GenerativeModel('models/gemini-2.0-flash')

def generate_plan(tasks):
    # Formateamos las tareas para que la IA las entienda mejor que un simple string
    tasks_text = ""
    for t in tasks:
        tasks_text += f"- Tarea: {t['task']}, Plazo: {t['deadline_days']} días, Duración: {t['duration']}h\n"
    
    prompt = f"""
    Eres un experto en productividad y gestión del tiempo. 
    Analiza la siguiente lista de tareas y organiza una semana eficiente:
    
    {tasks_text}
    
    Genera la respuesta con este formato exacto:
    Prioridad: (Lista de tareas de más a menos importante con una breve justificación)
    Plan semanal: (Distribución sugerida de las tareas de lunes a domingo)
    Razón: (Explicación de por qué has priorizado de esta manera)
    """

    try:
        # Llamada al modelo 2.0-flash
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # En caso de error de cuota o conexión, devolvemos el error detallado
        return f"Error en la comunicación con la API: {str(e)}"