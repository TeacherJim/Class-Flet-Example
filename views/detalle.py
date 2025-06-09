import flet as ft
# Esta vista muestra tarjetas de detalle de citas, incluyendo estudiante, fecha, hora y notas.
def DetalleView() -> ft.Control: # función que crea la vista de detalle de citas
    """Devuelve una vista con tarjetas de detalle de citas."""
    # Datos de ejemplo para las citas
    # Aquí se pueden reemplazar por datos reales o una base de datos CSV
    detalles_citas = [
        {
            "estudiante": "Juan Pérez",
            "fecha_hora": "2025-06-15, 09:00 AM",
            "notas": "Hablar sobre manejo del estrés académico."
        },
        {
            "estudiante": "María López",
            "fecha_hora": "2025-06-15, 10:00 AM",
            "notas": "Revisión de seguimiento emocional."
        },
        {
            "estudiante": "Luis Gómez",
            "fecha_hora": "2025-06-16, 11:00 AM",
            "notas": "Evaluación inicial de ansiedad."
        }
    ]
    # Crear tarjetas para cada cita con detalles
    # Se crea una lista de tarjetas que contendrán los detalles de cada cita
    cards = []
    # Bucle para crear cada tarjeta con los detalles de la cita
    for cita in detalles_citas:
        # Cada tarjeta contiene un contenedor con una columna que muestra los detalles de la cita
        card = ft.Card(
            content=ft.Container(
                content=ft.Column([ft.Row(
                    controls=[ft.Icon(ft.Icons.ACCOUNT_CIRCLE, size=30, color=ft.Colors.BLUE),
                    ft.Text(cita["estudiante"], size=20, weight=ft.FontWeight.BOLD)]),
                    ft.Text(f"Fecha y hora: {cita['fecha_hora']}"),
                    ft.Text(f"Notas: {cita['notas']}")
                ]),
                # Estilos y propiedades de la tarjeta
                padding=15,
                bgcolor=ft.Colors.WHITE60
            )
        )
        # Se añade la tarjeta a la lista de tarjetas
        cards.append(card)
    # Se devuelve un contenedor que contiene todas las tarjetas en una columna con scroll
    return ft.Container(
        content=ft.Column(cards, scroll=ft.ScrollMode.ALWAYS),
        padding=20,
        expand=True
    )