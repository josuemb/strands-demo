#!/usr/bin/env python3
"""
Analizador de Recetas de Cocina - WORKFLOW TOOL
==============================================

Pipeline automatizado que transforma ingredientes en receta completa:
Ingredientes → Validador → Nutricional → Sustitutos → Instrucciones → Presentación
"""

import os
import warnings

from strands import Agent
from strands_tools import workflow

os.environ["OTEL_SDK_DISABLED"] = "true"
warnings.filterwarnings("ignore", category=UserWarning, module="opentelemetry")


def crear_analizador_recetas():
    """Crea el agente principal con capacidad de workflow"""
    return Agent(
        name="analizador_recetas",
        system_prompt="""
        Eres un chef experto que coordina el análisis completo de recetas.
        Usas un workflow multi-agente para transformar ingredientes completos.
        """,
        tools=[workflow]
    )


def definir_tareas_workflow():
    """Define las tareas del workflow de análisis de recetas"""
    return [
        {
            "task_id": "validacion",
            "description": "Validar y categorizar ingredientes proporcionados",
            "system_prompt": "Chef experto. Categoriza ingredientes y lista faltantes.",
            "priority": 5
        },
        {
            "task_id": "nutricional",
            "description": "Analizar valor nutricional de los ingredientes validados",
            "dependencies": ["validacion"],
            "system_prompt": "Nutricionista. Evalúa calorías, macros y beneficios.",
            "priority": 4
        },
        {
            "task_id": "sustitutos",
            "description": "Generar sustitutos y mejoras para los ingredientes",
            "dependencies": ["validacion"],
            "system_prompt": "Chef creativo. Sugiere alternativas y variaciones.",
            "priority": 3
        },
        {
            "task_id": "instrucciones",
            "description": "Crear instrucciones paso a paso para cocinar",
            "dependencies": ["validacion", "nutricional", "sustitutos"],
            "system_prompt": "Chef instructor. Crea pasos de preparación y cocción.",
            "priority": 2
        },
        {
            "task_id": "presentacion",
            "description": "Generar presentación final atractiva de la receta",
            "dependencies": ["instrucciones"],
            "system_prompt": "Chef presentación. Crea nombre, emplatado y maridaje.",
            "priority": 1
        }
    ]


def procesar_receta_con_workflow(agente, ingredientes):
    """Procesa ingredientes usando el workflow tool"""

    workflow_id = f"receta_{hash(ingredientes) % 10000}"

    print(f"🔄 Creando workflow: {workflow_id}")

    # Crear workflow
    agente.tool.workflow(
        action="create",
        workflow_id=workflow_id,
        tasks=definir_tareas_workflow()
    )

    print(f"▶️  Iniciando procesamiento de: {ingredientes}")

    # Ejecutar workflow
    agente.tool.workflow(
        action="start",
        workflow_id=workflow_id,
        input_data=ingredientes
    )

    # Obtener status
    status = agente.tool.workflow(action="status", workflow_id=workflow_id)

    return status, workflow_id


def main():
    """Función principal para probar el analizador de recetas"""

    print("=" * 60)
    print("🍳 ANALIZADOR DE RECETAS - WORKFLOW TOOL")
    print("=" * 60)

    # Crear agente con workflow
    agente = crear_analizador_recetas()

    # Casos de prueba
    casos_prueba = [
        "pollo, arroz, brócoli, ajo, aceite de oliva",
        "salmón, quinoa, espinacas, limón, jengibre",
        "lentejas, tomate, cebolla, zanahoria, comino",
    ]

    print("\n🔍 Procesando ingredientes...\n")

    for i, ingredientes in enumerate(casos_prueba, 1):
        print(f"🥘 RECETA {i}: '{ingredientes}'")
        print("-" * 50)

        try:
            # Procesar con workflow tool
            status, workflow_id = procesar_receta_con_workflow(agente, ingredientes)

            print("✅ Workflow completado!")
            print(f"📊 ID: {workflow_id}")
            print(f"🎯 Status: {status.get('status', 'Unknown')}")

            # Limpiar workflow
            agente.tool.workflow(action="delete", workflow_id=workflow_id)

        except Exception as e:
            print(f"❌ Error en workflow: {e}")

        print("\n" + "=" * 60 + "\n")

    print("✅ Análisis de recetas completado!")


if __name__ == "__main__":
    main()
