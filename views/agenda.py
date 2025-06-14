import flet as ft
# Esta vista muestra un DataTable con citas futuras, incluyendo fecha, hora, estudiante y estado de la cita.
def AgendaView()->ft.Control:# es la creación de la vista de agenda
    """Devuelve una vista con un DataTable de citas futuras."""
    # Datos de ejemplo para las citas
    # Aquí se pueden reemplazar por datos reales o una base de datos CSV
    citas = [
        {"fecha": "2025-06-15", "hora": "09:00 AM", "estudiante": "Juan Pérez", "estado": "Pendiente"},
        {"fecha": "2025-06-15", "hora": "10:00 AM", "estudiante": "María López", "estado": "Confirmada"},
        {"fecha": "2025-06-16", "hora": "11:00 AM", "estudiante": "Luis Gómez", "estado": "Pendiente"},
        {"fecha": "2025-06-16", "hora": "12:00 PM", "estudiante": "Ana Torres", "estado": "Cancelada"},
        {"fecha": "2025-06-17", "hora": "01:00 PM", "estudiante": "Pedro Sánchez", "estado": "Confirmada"},
    ]
    # Crear las filas del DataTable a partir de los datos de citas
    rows = [
        ft.DataRow(cells=[
            ft.DataCell(ft.Text(cita["fecha"],color=ft.Colors.WHITE)),
            ft.DataCell(ft.Text(cita["hora"],color=ft.Colors.WHITE)),
            ft.DataCell(ft.Text(cita["estudiante"],color=ft.Colors.WHITE)),
            ft.DataCell(ft.Text(cita["estado"],color=ft.Colors.WHITE)),
        ], color="#ff005396") for cita in citas # bucle para crear cada fila
    ]
    # Crear el DataTable con las filas y columnas definidas
    tabla = ft.DataTable(
        # Definición de las columnas del DataTable
        columns=[
            ft.DataColumn(label=ft.Text("Fecha",color=ft.Colors.WHITE)),
            ft.DataColumn(label=ft.Text("Hora",color=ft.Colors.WHITE)),
            ft.DataColumn(label=ft.Text("Estudiante",color=ft.Colors.WHITE)),
            ft.DataColumn(label=ft.Text("Estado",color=ft.Colors.WHITE)),
        ],
        # Estilos y propiedades del DataTable
        rows=rows,
        vertical_lines=ft.BorderSide(width=3, color=ft.Colors.WHITE),
        horizontal_lines=ft.BorderSide(width=3, color=ft.Colors.WHITE),
        heading_row_color="#ff8ac300",
    )
    # se Devuelve un contenedor que contiene el DataTable con un padding y expand=True
    return ft.Container(content=tabla, padding=20, expand=True)