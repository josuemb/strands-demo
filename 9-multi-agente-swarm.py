#!/usr/bin/env python3
"""
Asesor de Inversiones Multi-Agente - SWARM MULTI-AGENTE
======================================================

Sistema colaborativo con handoff dinámico entre agentes especializados:
Consulta → Investigador Web → Analizador Riesgos → Recomendador → Handoff
"""

import os
import warnings

from strands import Agent
from strands.multiagent import Swarm

os.environ["OTEL_SDK_DISABLED"] = "true"
warnings.filterwarnings("ignore", category=UserWarning, module="opentelemetry")


def crear_investigador_web():
    """Agente que investiga tipos de inversión"""
    return Agent(
        name="investigador_web",
        system_prompt="""
        Eres un investigador financiero especializado en oportunidades de inversión.

        TAREA: Analizar la consulta del usuario e identificar tipos relevantes.

        RESPONDE CON:
        - Tipos de inversión recomendados
        - Breve explicación de cada opción
        - Factores a considerar
        """,
    )


def crear_analizador_riesgos():
    """Agente que evalúa riesgos de inversión"""
    return Agent(
        name="analizador_riesgos",
        system_prompt="""
        Eres un analista de riesgos financieros especializado en inversiones.

        TAREA: Evaluar riesgos y beneficios de las opciones identificadas.

        RESPONDE CON:
        - Nivel de riesgo de cada opción
        - Beneficios potenciales
        - Riesgos específicos
        - Recomendaciones de diversificación
        """,
    )


def crear_recomendador():
    """Agente que genera recomendaciones finales"""
    return Agent(
        name="recomendador",
        system_prompt="""
        Eres un asesor financiero que genera recomendaciones personalizadas.

        TAREA: Crear recomendaciones finales basadas en el análisis previo.

        RESPONDE CON:
        - Recomendaciones específicas
        - Distribución sugerida del portafolio
        - Pasos a seguir
        - Consideraciones importantes
        """,
    )


def crear_swarm_inversiones():
    """Crea el swarm multi-agente para análisis de inversiones"""

    # Crear agentes
    investigador = crear_investigador_web()
    analizador = crear_analizador_riesgos()
    recomendador = crear_recomendador()

    # Crear el swarm
    swarm = Swarm([investigador, analizador, recomendador])

    return swarm


def main():
    """Función principal para probar el asesor de inversiones"""

    print("=" * 60)
    print("💰 ASESOR DE INVERSIONES MULTI-AGENTE")
    print("=" * 60)

    # Crear el swarm
    swarm = crear_swarm_inversiones()

    # Caso de prueba
    consulta = """
    Soy una persona de 30 años con ahorros de 50,000 USD.
    Busco opciones de inversión para hacer crecer mi dinero
    en los próximos 5-10 años.
    Tengo tolerancia media al riesgo.
    """

    print("\n🔍 Procesando consulta de inversión...\n")
    print(f"📝 CONSULTA: {consulta.strip()}")
    print("-" * 50)

    try:
        # Ejecutar el swarm
        resultado = swarm(consulta)

        print("\n✅ Análisis completado!")
        print(f"📊 Status: {resultado.status}")
        print(f"🤖 Agentes participantes: {len(resultado.node_history)}")

        # Mostrar resultado final si está disponible
        if hasattr(resultado, 'result') and resultado.result:
            print("\n💡 Recomendación final:")
            print(resultado.result)

    except Exception as e:
        print(f"❌ Error: {e}")

    print("\n" + "=" * 60)
    print("✅ Análisis de inversiones completado!")
    print("=" * 60)


if __name__ == "__main__":
    main()
