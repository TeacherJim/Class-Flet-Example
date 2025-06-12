import flet as ft


def PerfilView(page: ft.Page):
    """Devuelve una vista de perfil con campos editables y modo oscuro."""
    # estado local para modo oscuro
    is_dark = ft.Ref[bool](False)

    # controles de texto para editar perfil
    nombre = ft.TextField(label="Nombre", width=300)
    apellido = ft.TextField(label="Apellido", width=300)
    edad = ft.TextField(label="Edad", width=150)
    grado = ft.TextField(label="Grado", width=150)

    def toggle_tema(e):
        """Cambia el modo claro/oscuro."""
        is_dark.current = e.control.value
        page.theme_mode = ft.ThemeMode.DARK if is_dark.current else ft.ThemeMode.LIGHT
        page.update()

    switch = ft.Switch(label="🌙 Modo oscuro", on_change=toggle_tema)

    perfil_icono = ft.Text("👤", size=80)

    contenido = ft.Column([
        perfil_icono,
        nombre,
        apellido,
        edad,
        grado,
        ft.Row([switch]),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    return ft.Container(content=contenido, padding=20, expand=True)
