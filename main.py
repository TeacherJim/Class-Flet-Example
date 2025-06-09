import flet as ft
from views.agenda import AgendaView
from views.perfil import profile_view
from views.detalle import DetalleView

def main(page: ft.Page):
    page.title = "Agenda Psicológica Supérate"

    views = [AgendaView, DetalleView, profile_view]
    current_view = ft.Container(expand=True)
    current_view.content = views[0]()

    def cambiar_vista(e):
        page.clean()
        """Cambia la vista según el destino seleccionado en NavigationRail."""
        current_view = views[e.control.selected_index]()
        page.add(ft.Row([nav, current_view], expand=True))
        page.update()

    nav = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.CALENDAR_MONTH, label="Agenda"),
            ft.NavigationRailDestination(icon=ft.Icons.DESCRIPTION, label="Detalle Citas"),
            ft.NavigationRailDestination(icon=ft.Icons.SETTINGS, label="Perfil/Ajustes"),
        ],
        on_change=cambiar_vista,
    )

    # Vista por defecto al abrir la app
    page.add(ft.Row([nav, current_view],expand=True))

ft.app(target=main)