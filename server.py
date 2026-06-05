# Importamos FastMCP para crear el servidor MCP
from fastmcp import FastMCP

# Importamos sqlite3 para conectarnos con la base de datos
import sqlite3

# Importamos la función que inicializa la base de datos
# y el nombre del archivo de la base de datos
from database import init_db, DB_NAME

# Verificamos que la base de datos y la tabla productos existan
init_db()

# Creamos el servidor MCP y le asignamos un nombre
mcp = FastMCP("InventarioDB")

def get_connection():
    """
    Crea y retorna una conexión con la base de datos SQLite.
    """
    return sqlite3.connect(DB_NAME)