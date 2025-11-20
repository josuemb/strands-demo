# Strands Agents Demo

Una colección completa de ejemplos prácticos que demuestran las capacidades de **Strands Agents**, desde agentes simples hasta sistemas multi-agente complejos con integración MCP.

## 🎯 Propósito

Este repositorio contiene 10 ejemplos progresivos que cubren:
- Configuración básica de agentes
- Integración con herramientas personalizadas y MCP
- Patrones multi-agente (Swarm, Workflow, Graph)
- Casos de uso del mundo real

## 🚀 Inicio Rápido

### Prerrequisitos
- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (gestor de paquetes moderno)

### Instalación

```bash
# Clonar el repositorio
git clone <repository-url>
cd strands-demo

# Instalar dependencias
uv sync

# Activar entorno virtual
source .venv/bin/activate  # Linux/macOS
# o
.venv\Scripts\activate     # Windows
```

## 📚 Ejemplos Incluidos

### Nivel Básico

#### 1. Agente Simple (`1-agente-simple.py`)
```python
from strands import Agent

agent = Agent()
agent("¿Cuál es la capital de Francia?")
```
**Aprende**: Creación básica de agentes y consultas simples.

#### 2. Configuración del Modelo (`2-agente-config-model.py`)
**Aprende**: Inspección de configuración del modelo y parámetros.

#### 3. Otros Modelos (`3-agente-otro-modelo.py`)
**Aprende**: Configuración de diferentes proveedores de modelos.

#### 4. Agente Sin Herramientas (`4-agente-sin-herramientas.py`)
**Aprende**: Comportamiento de agentes sin capacidades extendidas.

### Nivel Intermedio

#### 5. Agente con Herramientas (`5-agente-con-herramientas.py`)
```python
from strands_tools import current_time, shell, use_aws

agent = Agent(tools=[current_time, shell, use_aws])
```
**Aprende**: Integración con herramientas predefinidas (tiempo, shell, AWS).

#### 6. Herramientas Personalizadas (`6-agente-herramientas-personalizadas.py`)
```python
@tool
def calculate_date(base_date: str, operation: str) -> str:
    """Calcula fechas agregando o restando períodos de tiempo."""
    # Implementación personalizada
```
**Aprende**: Creación de herramientas personalizadas con decorador `@tool`.

#### 7. Integración MCP (`7-agente-mcp-tools.py`)
```python
from strands.tools.mcp import MCPClient

core_mcp_client = MCPClient(...)
agent = Agent(tools=[core_mcp_client])
```
**Aprende**: Integración con Model Context Protocol para herramientas avanzadas.

### Nivel Avanzado - Multi-Agente

#### 8. Grafo Multi-Agente (`8-multi-agente-grafo.py`)
**Patrón**: Graph-based multi-agent system
**Caso de uso**: Sistema de análisis de mercado con agentes especializados conectados en grafo.

#### 9. Swarm Multi-Agente (`9-multi-agente-swarm.py`)
**Patrón**: Swarm with dynamic handoffs
**Caso de uso**: Asesor de inversiones con handoff dinámico entre investigador, analizador y recomendador.

#### 10. Workflow Multi-Agente (`10-multi-agente-workflow.py`)
**Patrón**: Sequential workflow pipeline
**Caso de uso**: Analizador de recetas con pipeline: Ingredientes → Validador → Nutricional → Sustitutos → Instrucciones.

## 🛠️ Desarrollo

### Flujo de Trabajo Obligatorio

Antes de cualquier modificación:
```bash
uv sync                    # Sincronizar dependencias
```

Después de modificar código:
```bash
ruff format .              # Formatear código
ruff check .               # Verificar calidad
ruff check --fix .         # Corregir automáticamente
```

### Estructura del Proyecto

```
strands-demo/
├── 1-agente-simple.py              # Ejemplo básico
├── 2-agente-config-model.py        # Configuración de modelo
├── 3-agente-otro-modelo.py         # Modelos alternativos
├── 4-agente-sin-herramientas.py    # Agente sin herramientas
├── 5-agente-con-herramientas.py    # Herramientas predefinidas
├── 6-agente-herramientas-personalizadas.py  # Herramientas custom
├── 7-agente-mcp-tools.py           # Integración MCP
├── 8-multi-agente-grafo.py         # Patrón Graph
├── 9-multi-agente-swarm.py         # Patrón Swarm
├── 10-multi-agente-workflow.py     # Patrón Workflow
├── pyproject.toml                   # Configuración del proyecto
└── .kiro/steering/                  # Configuración de desarrollo
```

## 🔧 Configuración

### Variables de Entorno
```bash
# Para herramientas AWS (ejemplo 5 y 7)
export AWS_PROFILE=your-profile
export AWS_REGION=us-east-1

# Para desactivar telemetría (ejemplos multi-agente)
export OTEL_SDK_DISABLED=true
```

### Dependencias Principales
- **strands-agents**: Framework principal para agentes
- **strands-agents-tools**: Herramientas predefinidas
- **mcp**: Model Context Protocol para herramientas avanzadas

## 📖 Recursos Adicionales

- [Documentación Strands Agents](https://docs.strands.ai)
- [Guía MCP](https://modelcontextprotocol.io)
- [Herramientas AWS MCP](https://github.com/awslabs/core-mcp-server)

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Sigue el flujo de trabajo de desarrollo (ruff format + check)
4. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
5. Push a la rama (`git push origin feature/nueva-funcionalidad`)
6. Crea un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.
