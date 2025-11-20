from strands import Agent


def main():
    # Crea un agente con un modelo distinto al estándar
    agent = Agent(model="amazon.nova-micro-v1:0")

    # Imprime la configuracion del modelo
    print(agent.model.config)

    # Hace una pregunta al agente
    agent("¿Cuál es la capital de Francia?")


if __name__ == "__main__":
    main()
