#!/usr/bin/env python3
"""
Analizador de Sentimientos Multi-Nivel - GRAFO MULTI-AGENTE
==========================================================

Grafo estructurado con ejecución paralela de nodos especializados:
Texto → Detector Idioma → Analizador ES/EN → Clasificador → Re-análisis
"""

import os

os.environ["OTEL_SDK_DISABLED"] = "true"

from strands import Agent
from strands.multiagent import GraphBuilder


def crear_detector_idioma():
    """Agente que detecta el idioma del texto"""
    return Agent(
        name="detector_idioma",
        system_prompt="""
        Eres un detector de idioma especializado.

        TAREA: Detectar si el texto está en español o inglés.

        RESPONDE EXACTAMENTE:
        - "ESPAÑOL" si el texto está en español
        - "INGLÉS" si el texto está en inglés

        IMPORTANTE: Termina tu respuesta con " | "
        - "MIXTO" si hay mezcla de idiomas
        """,
    )


def crear_analizador_español():
    """Agente especializado en análisis de sentimientos en español"""
    return Agent(
        name="analizador_español",
        system_prompt="""
        Eres un experto en análisis de sentimientos en español.

        TAREA: Analizar el sentimiento del texto en español.

        RESPONDE CON UNA DE ESTAS OPCIONES:
        - "POSITIVO" - Sentimiento claramente positivo
        - "NEGATIVO" - Sentimiento claramente negativo
        - "NEUTRO" - Sin carga emocional clara
        - "MIXTO" - Sentimientos contradictorios que requieren re-análisis

        IMPORTANTE: Termina tu respuesta con " | "
        """,
    )


def crear_analizador_ingles():
    """Agente especializado en análisis de sentimientos en inglés"""
    return Agent(
        name="analizador_ingles",
        system_prompt="""
        Eres un experto en análisis de sentimientos en inglés.

        TAREA: Analizar el sentimiento del texto en inglés.

        RESPONDE CON UNA DE ESTAS OPCIONES:
        - "POSITIVO" - Clearly positive sentiment
        - "NEGATIVO" - Clearly negative sentiment
        - "NEUTRO" - No clear emotional charge
        - "MIXTO" - Contradictory sentiments requiring re-analysis

        IMPORTANTE: Termina tu respuesta con " | "
        """,
    )


def crear_grafo_sentimientos():
    """Crea el grafo multi-agente para análisis de sentimientos"""

    # Crear agentes
    detector = crear_detector_idioma()
    analizador_es = crear_analizador_español()
    analizador_en = crear_analizador_ingles()

    # Crear el grafo usando GraphBuilder
    builder = GraphBuilder()

    # Agregar nodos
    builder.add_node(detector, "detector")
    builder.add_node(analizador_es, "español")
    builder.add_node(analizador_en, "ingles")

    # Definir punto de entrada
    builder.set_entry_point("detector")

    # Agregar conexiones simples (sin condiciones por ahora)
    builder.add_edge("detector", "español")
    builder.add_edge("detector", "ingles")

    return builder.build()


def main():
    """Función principal para probar el analizador de sentimientos"""

    print("=" * 60)
    print("ANALIZADOR DE SENTIMIENTOS MULTI-NIVEL")
    print("=" * 60)

    # Crear el grafo
    grafo = crear_grafo_sentimientos()

    # Casos de prueba
    casos_prueba = [
        "Me encanta este producto, es fantástico",
        "I hate this service, it's terrible",
        "Es un producto normal, nada especial",
    ]

    print("\n🔍 Procesando casos de prueba...\n")

    for i, texto in enumerate(casos_prueba, 1):
        print(f"📝 CASO {i}: '{texto}'")
        print("-" * 50)

        try:
            # Ejecutar el grafo
            resultado = grafo(texto)

            print("🔍 Análisis completado:")
            print(f"   Status: {resultado.status}")
            print(f"   Nodos ejecutados: {resultado.completed_nodes}")

            # Mostrar el resultado final si está disponible
            if hasattr(resultado, 'result') and resultado.result:
                print(f"📊 Resultado final: {resultado.result}")

        except Exception as e:
            print(f"❌ Error: {e}")

        print("\n")

    print("=" * 60)
    print("✅ Análisis completado!")
    print("=" * 60)


if __name__ == "__main__":
    main()
