import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configuramos la API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("--- LISTANDO MODELOS DISPONIBLES ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Modelo encontrado: {m.name}")
            
    # Intentamos con el nombre técnico completo
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    response = model.generate_content("Hola, ¿estás activa?")
    print("\n✅ ¡ÉXITO! RESPUESTA:")
    print(response.text)

except Exception as e:
    print(f"\n❌ ERROR DETALLADO: {e}")