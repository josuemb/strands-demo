from mcp import StdioServerParameters, stdio_client
from strands import Agent
from strands.tools.mcp import MCPClient


def main():
    # Configurar el cliente MCP para core-mcp-server con roles específicos
    core_mcp_client = MCPClient(
        lambda: stdio_client(
            StdioServerParameters(
                command="uvx",
                args=[
                    "awslabs.core-mcp-server@latest",
                    "--roles",
                    "aws-foundation,dev-tools,frontend-dev,solutions-architect",
                ],
            )
        ),
        prefix="core",
    )

    # Configurar el cliente MCP para strands-agents-mcp-server
    strands_mcp_client = MCPClient(
        lambda: stdio_client(
            StdioServerParameters(
                command="uvx",
                args=["strands-agents-mcp-server@latest"],
            )
        ),
        prefix="strands",
    )

    # Crear agente con herramientas MCP (integración gestionada experimental)
    agent = Agent(
        tools=[core_mcp_client, strands_mcp_client],
        system_prompt="""Eres un asistente especializado en AWS y desarrollo con
        Strands Agents.
        Tienes acceso a herramientas avanzadas para:

        AWS (prefijo 'core'):
        - Fundamentos de AWS (aws-foundation)
        - Herramientas de desarrollo (dev-tools)
        - Desarrollo frontend (frontend-dev)
        - Arquitectura de soluciones (solutions-architect)

        Strands Agents (prefijo 'strands'):
        - Documentación de Strands Agents
        - Ejemplos y patrones de uso
        - Guías de implementación

        Usa estas herramientas para proporcionar respuestas precisas y detalladas.""",
    )

    # Interactuar con el agente
    print("🤖 Agente MCP (AWS + Strands) listo. Escribe 'salir' para terminar.\n")

    while True:
        pregunta = input("👤 Pregunta: ").strip()

        if pregunta.lower() in ["salir", "exit", "quit"]:
            print("👋 ¡Hasta luego!")
            break

        if pregunta:
            try:
                respuesta = agent(pregunta)
                content = respuesta.message["content"][0]
                text = content.get("text", str(content))
                print(f"🤖 {text}\n")
            except Exception as e:
                print(f"❌ Error: {e}\n")


if __name__ == "__main__":
    main()
