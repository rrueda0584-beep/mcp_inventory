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

@mcp.tool()
def crear_producto(
    nombre: str,
    categoria: str,
    cantidad: int,
    precio: float
) -> str:
    """
    Crea un nuevo producto en la base de datos.
    """

    # Abrimos una conexión con la base de datos
    conn = get_connection()

    # Creamos un cursor para ejecutar instrucciones SQL
    cursor = conn.cursor()

    # Insertamos el nuevo producto en la tabla
    cursor.execute(
        """
        INSERT INTO productos (nombre, categoria, cantidad, precio)
        VALUES (?, ?, ?, ?)
        """,
        (nombre, categoria, cantidad, precio)
    )

    # Guardamos los cambios
    conn.commit()

    # Cerramos la conexión
    conn.close()

    return "Producto creado exitosamente"

@mcp.tool()
def consultar_producto(id: int) -> dict:
    """
    Consulta un producto por su identificador.
    """

    # Abrimos una conexión con la base de datos
    conn = get_connection()

    # Creamos un cursor para ejecutar la consulta
    cursor = conn.cursor()

    # Buscamos el producto cuyo id coincida con el valor recibido
    cursor.execute(
        "SELECT * FROM productos WHERE id = ?",
        (id,)
    )

    # Obtenemos un solo registro
    row = cursor.fetchone()

    # Cerramos la conexión
    conn.close()

    # Si se encontró el producto, devolvemos sus datos
    if row:
        return {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }

    # Si no existe el producto, devolvemos un mensaje de error
    return {"error": "Producto no encontrado"}

@mcp.tool()
def actualizar_producto(id: int, cantidad: int) -> str:
    """
    Actualiza la cantidad disponible de un producto.
    """

    # Abrimos una conexión con la base de datos
    conn = get_connection()

    # Creamos un cursor para ejecutar la instrucción SQL
    cursor = conn.cursor()

    # Actualizamos la cantidad del producto indicado
    cursor.execute(
        "UPDATE productos SET cantidad = ? WHERE id = ?",
        (cantidad, id)
    )

    # Guardamos los cambios
    conn.commit()

    # Verificamos si realmente se modificó algún registro
    filas_modificadas = cursor.rowcount

    # Cerramos la conexión
    conn.close()

    # Si no se encontró el id, informamos al usuario
    if filas_modificadas == 0:
        return "Producto no encontrado"

    return "Producto actualizado correctamente"

@mcp.tool()
def eliminar_producto(id: int) -> str:
    """
    Elimina un producto de la base de datos usando su identificador.
    """

    # Abrimos una conexión con la base de datos
    conn = get_connection()

    # Creamos un cursor para ejecutar la instrucción SQL
    cursor = conn.cursor()

    # Eliminamos el producto cuyo id coincida
    cursor.execute(
        "DELETE FROM productos WHERE id = ?",
        (id,)
    )

    # Guardamos los cambios realizados
    conn.commit()

    # Verificamos si se eliminó algún registro
    filas_eliminadas = cursor.rowcount

    # Cerramos la conexión
    conn.close()

    # Si no se encontró el producto, informamos al usuario
    if filas_eliminadas == 0:
        return "Producto no encontrado"

    return "Producto eliminado correctamente"

@mcp.tool()
def listar_productos() -> list:
    """
    Retorna todos los productos registrados en la base de datos.
    """

    # Abrimos una conexión con la base de datos
    conn = get_connection()

    # Creamos un cursor para ejecutar la consulta SQL
    cursor = conn.cursor()

    # Consultamos todos los registros de la tabla productos
    cursor.execute("SELECT * FROM productos")

    # Recuperamos todas las filas encontradas
    rows = cursor.fetchall()

    # Cerramos la conexión
    conn.close()

    # Convertimos cada fila en un diccionario
    return [
        {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }
        for row in rows
    ]

@mcp.tool()
def calcular_valor_total_inventario() -> dict:
    """
    Calcula el valor económico total del inventario.
    """

    # Abrimos una conexión con la base de datos
    conn = get_connection()

    # Creamos un cursor para ejecutar la consulta SQL
    cursor = conn.cursor()

    # Calculamos la suma de cantidad por precio para todos los productos
    cursor.execute(
        "SELECT SUM(cantidad * precio) FROM productos"
    )

    # Obtenemos el resultado de la consulta
    total = cursor.fetchone()[0]

    # Cerramos la conexión
    conn.close()

    # Si la tabla está vacía, SQLite devuelve None; en ese caso retornamos 0
    return {
        "valor_total_inventario": total if total is not None else 0
    }
    
@mcp.tool()
def productos_agotados() -> list:
    """
    Retorna los productos cuya cantidad es igual a cero.
    """

    # Abrimos una conexión con la base de datos
    conn = get_connection()

    # Creamos un cursor para ejecutar la consulta SQL
    cursor = conn.cursor()

    # Consultamos los productos agotados
    cursor.execute(
        "SELECT * FROM productos WHERE cantidad = 0"
    )

    # Recuperamos todos los registros encontrados
    rows = cursor.fetchall()

    # Cerramos la conexión
    conn.close()

    # Convertimos cada fila en un diccionario
    return [
        {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }
        for row in rows
    ]

@mcp.tool()
def producto_mas_costoso() -> dict:
    """
    Retorna el producto con el mayor precio unitario.
    """

    # Abrimos una conexión con la base de datos
    conn = get_connection()

    # Creamos un cursor para ejecutar la consulta SQL
    cursor = conn.cursor()

    # Ordenamos los productos por precio de mayor a menor
    # y seleccionamos únicamente el primero
    cursor.execute(
        "SELECT * FROM productos ORDER BY precio DESC LIMIT 1"
    )

    # Recuperamos el registro encontrado
    row = cursor.fetchone()

    # Cerramos la conexión
    conn.close()

    # Si existe al menos un producto, retornamos sus datos
    if row:
        return {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }

    # Si la tabla está vacía, devolvemos un mensaje de error
    return {"error": "No hay productos registrados"}

@mcp.tool()
def estadisticas_inventario() -> dict:
    """
    Calcula estadísticas generales del inventario.
    """

    # Abrimos una conexión con la base de datos
    conn = get_connection()

    # Creamos un cursor para ejecutar la consulta SQL
    cursor = conn.cursor()

    # Calculamos:
    # 1. Número de productos registrados
    # 2. Promedio de cantidades
    # 3. Promedio de precios
    # 4. Valor económico total del inventario
    cursor.execute("""
        SELECT
            COUNT(*),
            AVG(cantidad),
            AVG(precio),
            SUM(cantidad * precio)
        FROM productos
    """)

    # Guardamos los resultados de la consulta en variables
    total_productos, promedio_cantidad, promedio_precio, valor_total = cursor.fetchone()

    # Cerramos la conexión
    conn.close()

    # Retornamos las estadísticas en un diccionario
    return {
        "total_productos": total_productos,
        "promedio_cantidad": promedio_cantidad if promedio_cantidad is not None else 0,
        "promedio_precio": promedio_precio if promedio_precio is not None else 0,
        "valor_total": valor_total if valor_total is not None else 0
    }

if __name__ == "__main__":
    # Inicia el servidor MCP
    mcp.run()
    

