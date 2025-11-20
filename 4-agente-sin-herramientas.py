from strands import Agent


def main():
    # Crea un agente con la configuración estándar
    agent = Agent()

    # Hace preguntas al agente

    agent("""
          1)¿Qué hora es en la Ciudad de México?
          2)¿Cuántos archivos tengo en el directorio actual?
          3)¿Cuáles son los buckets de s3 que tengo en mi cuenta?
    """)


if __name__ == "__main__":
    main()
