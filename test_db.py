# Importamos pprint para mostrar listas y diccionarios de forma legible
from pprint import pprint

# Importamos las herramientas implementadas en server.py
from server import (
    crear_producto,
    consultar_producto,
    actualizar_producto,
    eliminar_producto,
    listar_productos,
    calcular_valor_total_inventario,
    productos_agotados,
    producto_mas_costoso,
    estadisticas_inventario
)

def mostrar_titulo(titulo: str) -> None:
    """
    Muestra un título separado para organizar la salida de las pruebas.
    """

    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)
    
def probar_crud() -> None:
    """
    Ejecuta pruebas de consulta, actualización, eliminación y listado.
    """

    mostrar_titulo("CONSULTAR PRODUCTO CON ID 1")
    pprint(consultar_producto(1), sort_dicts=False)

    mostrar_titulo("ACTUALIZAR CANTIDAD DEL PRODUCTO CON ID 2")
    print(actualizar_producto(2, 18))
    pprint(consultar_producto(2), sort_dicts=False)

    mostrar_titulo("CONSULTAR PRODUCTO INEXISTENTE")
    pprint(consultar_producto(999), sort_dicts=False)

    mostrar_titulo("ELIMINAR PRODUCTO INEXISTENTE")
    print(eliminar_producto(999))

    mostrar_titulo("LISTAR TODOS LOS PRODUCTOS")
    pprint(listar_productos(), sort_dicts=False)

def probar_analiticas() -> None:
    """
    Ejecuta las pruebas de las herramientas analíticas del inventario.
    """

    mostrar_titulo("VALOR TOTAL DEL INVENTARIO")
    pprint(calcular_valor_total_inventario(), sort_dicts=False)

    mostrar_titulo("PRODUCTOS AGOTADOS")
    pprint(productos_agotados(), sort_dicts=False)

    mostrar_titulo("PRODUCTO MÁS COSTOSO")
    pprint(producto_mas_costoso(), sort_dicts=False)

    mostrar_titulo("ESTADÍSTICAS GENERALES DEL INVENTARIO")
    pprint(estadisticas_inventario(), sort_dicts=False)

if __name__ == "__main__":
    probar_crud()
    probar_analiticas()