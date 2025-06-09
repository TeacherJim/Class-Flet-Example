import flet as ft


def DetalleView() -> ft.Control:
    """Devuelve una vista con tarjetas de detalle de citas."""
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

    cards = []
    for cita in detalles_citas:
        card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text(cita["estudiante"], size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Fecha y hora: {cita['fecha_hora']}"),
                    ft.Text(f"Notas: {cita['notas']}")
                ]),
                padding=15
            )
        )
        cards.append(card)

    return ft.Container(
        content=ft.Column(cards, scroll=ft.ScrollMode.ALWAYS),
        padding=20,
        expand=True
    )
