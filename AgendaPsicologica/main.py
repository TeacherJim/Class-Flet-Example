import flet as ft
from views.agenda import AgendaView
from views.detalle import DetalleView


def main(page: ft.Page):
    page.title = "Agenda Psicológica Supérate"

    def cambiar_vista(e):
        """Cambia la vista según el destino seleccionado en NavigationRail."""
        seleccion = e.control.selected_index
        page.controls.clear()

        if seleccion == 0:
            page.add(ft.Row([nav, AgendaView()]))
        elif seleccion == 1:
            page.add(ft.Row([nav, DetalleView()]))
        elif seleccion == 2:
            page.add(ft.Row([nav, ft.Text("Perfil/Ajustes (en construcción)", size=18)]))

        page.update()

    nav = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.CALENDAR_MONTH, label="Agenda"),
            ft.NavigationRailDestination(icon=ft.icons.DESCRIPTION, label="Detalle Citas"),
            ft.NavigationRailDestination(icon=ft.icons.SETTINGS, label="Perfil/Ajustes"),
        ],
        on_change=cambiar_vista,
    )

    # Vista por defecto al abrir la app
    page.add(ft.Row([nav, AgendaView()]))


ft.app(target=main)
