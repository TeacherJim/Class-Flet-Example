import flet as ft
# Esta vista muestra una vista de perfil y ajustes (en construcción).
def profile_view() -> ft.Control:
    """Devuelve una vista de perfil y ajustes (en construcción)."""
    # Contenido de la vista de perfil y ajustes
    # Aquí se puede agregar más contenido o controles según sea necesario
    return ft.Container(
        content=ft.Text("Perfil/Ajustes (en construcción)", size=18),
        padding=20,
        expand=True
    )