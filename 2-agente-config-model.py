from strands import Agent


def main():
    # Crea un agente con la configuración estándar
    agent = Agent()

    # Imprime la configuracion del modelo
    print(agent.model.config)

    # Hace una pregunta al agente
    agent("¿Cuál es la capital de Francia?")


if __name__ == "__main__":
    main()
