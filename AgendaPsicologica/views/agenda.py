import flet as ft


def AgendaView():
    """Devuelve una vista con un DataTable de citas futuras."""
    citas = [
        {"fecha": "2025-06-15", "hora": "09:00 AM", "estudiante": "Juan Pérez", "estado": "Pendiente"},
        {"fecha": "2025-06-15", "hora": "10:00 AM", "estudiante": "María López", "estado": "Confirmada"},
        {"fecha": "2025-06-16", "hora": "11:00 AM", "estudiante": "Luis Gómez", "estado": "Pendiente"},
        {"fecha": "2025-06-16", "hora": "12:00 PM", "estudiante": "Ana Torres", "estado": "Cancelada"},
        {"fecha": "2025-06-17", "hora": "01:00 PM", "estudiante": "Pedro Sánchez", "estado": "Confirmada"},
    ]

    rows = [
        ft.DataRow(cells=[
            ft.DataCell(ft.Text(cita["fecha"])),
            ft.DataCell(ft.Text(cita["hora"])),
            ft.DataCell(ft.Text(cita["estudiante"])),
            ft.DataCell(ft.Text(cita["estado"])),
        ]) for cita in citas
    ]

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Fecha")),
            ft.DataColumn(label=ft.Text("Hora")),
            ft.DataColumn(label=ft.Text("Estudiante")),
            ft.DataColumn(label=ft.Text("Estado")),
        ],
        rows=rows,
    )

    return ft.Container(content=tabla, padding=20, expand=True)
