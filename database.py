# Importamos sqlite3 para trabajar con bases de datos SQLite
import sqlite3

# Nombre del archivo donde se almacenará la base de datos
DB_NAME = "inventory.db"

def init_db():
    
    # Establece la conexión con la base de datos
    conn = sqlite3.connect(DB_NAME)

    # Crea un cursor para ejecutar instrucciones SQL
    cursor = conn.cursor()

    # Crea la tabla productos si aún no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    """)

    # Guarda los cambios realizados
    conn.commit()

    # Cierra la conexión con la base de datos
    conn.close()
    
if __name__ == "__main__":
    init_db()