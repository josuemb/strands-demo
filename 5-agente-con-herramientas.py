from strands import Agent
from strands_tools import current_time, shell, use_aws


def main():
    # Crea un agente con la configuración estándar
    agent = Agent(tools=[current_time, shell, use_aws])

    # Hace preguntas al agente

    agent("""
          1)¿Qué hora es en la Ciudad de México?
          2)¿Cuántos archivos tengo en el directorio actual?
          3)¿Cuáles son los buckets de s3 que tengo en mi cuenta?
    """)


if __name__ == "__main__":
    main()
