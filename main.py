import flet as ft
# Importación de las vistas desde sus respectivos módulos (archivos .py)
from views.agenda import AgendaView
from views.perfil import profile_view
from views.detalle import DetalleView

def main(page: ft.Page): # función principal que se ejecuta al iniciar la aplicación
    """Función principal que configura la aplicación Flet."""
    # Configuración de la página
    page.title = "Agenda Psicológica Supérate"
    views = [AgendaView, DetalleView, profile_view]
    current_view = ft.Container(expand=True)
    current_view.content = views[0]()

    def cambiar_vista(evento):# función que cambia la vista según el destino seleccionado en NavigationRail
        """Cambia la vista según el destino seleccionado en NavigationRail."""
        page.clean()
        current_view = views[evento.control.selected_index]()
        page.add(ft.Row([nav, current_view], expand=True))
        page.update()
    # Creación del NavigationRail con destinos y eventos
    # NavigationRail es un componente de navegación vertical que permite seleccionar diferentes vistas
    nav = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.CALENDAR_MONTH, label="Agenda"),
            ft.NavigationRailDestination(icon=ft.Icons.DESCRIPTION, label="Detalle Citas"),
            ft.NavigationRailDestination(icon=ft.Icons.SETTINGS, label="Perfil/Ajustes"),
        ],
        on_change=cambiar_vista, # Evento que se dispara al cambiar la selección en NavigationRail
    )

    # Añadir la vista inicial al contenedor actual contiene current_view y nav
    page.add(ft.Row([nav, current_view],expand=True))
# Ejecutar la aplicación Flet con la función principal
ft.app(target=main)