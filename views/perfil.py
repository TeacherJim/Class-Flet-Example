import flet as ft

def profile_view() -> ft.Control:
    """Devuelve una vista de perfil y ajustes (en construcción)."""
    return ft.Container(
        content=ft.Text("Perfil/Ajustes (en construcción)", size=18),
        padding=20,
        expand=True
    )