# Sistema Cognitivo de Inventario con MCP y SQLite

## Descripción

Este proyecto implementa un servidor MCP en Python para gestionar y analizar un inventario de productos almacenado en una base de datos SQLite.

El sistema permite realizar operaciones CRUD sobre los productos, además de ejecutar consultas analíticas básicas como calcular el valor total del inventario, identificar productos agotados, encontrar el producto más costoso y obtener estadísticas generales.

El proyecto fue desarrollado como parte del curso de Computación Cognitiva para Big Data, con el propósito de comprender cómo un sistema cognitivo puede conectarse con herramientas externas mediante Model Context Protocol.

## Tecnologías utilizadas

- Python 3.14
- FastMCP
- SQLite
- Visual Studio Code
- Git
- GitHub

## Estructura del proyecto

```text
mcp_inventory/
├── database.py
├── server.py
├── test_db.py
├── requirements.txt
├── README.md
├── .gitignore
└── inventory.db

```markdown
- `database.py`: crea la base de datos SQLite y la tabla `productos`.
- `server.py`: contiene el servidor MCP, las operaciones CRUD y las herramientas analíticas.
- `test_db.py`: ejecuta las pruebas funcionales del sistema.
- `requirements.txt`: registra la dependencia principal del proyecto.
- `README.md`: documenta la instalación, ejecución y funcionamiento.
- `.gitignore`: indica qué archivos y carpetas no deben subirse a GitHub.
- `inventory.db`: almacena localmente la información del inventario.