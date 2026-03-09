from tasks import tasks
from agent import generate_plan


def main():
    # Iniciamos el agente
    print("Iniciando el Agente de planificación semanal")

    try:
        # El agente procesa las tareas
        plan = generate_plan(tasks)

        # Imprimimos el resultado por consola
        print("\nPlan Generado: ")
        print(plan)

        # Guardamos el resultado en el archivo 'plan_semanal.txt'
        with open("plan_semanal.txt", "w", encoding="utf-8") as f:
            f.write(plan)

        print("\nPlan guardado en 'plan_semanal.txt'")

    except Exception as e:
        print(f"Error al generar el plan: {str(e)}")

if __name__ == "__main__":
    main()
   