# AgendaPsicologica

Este repositorio contiene un ejemplo de proyecto en **Flet** dividido en tres partes para ser trabajado por grupos de estudiantes. La aplicación permite gestionar citas de una agenda psicológica sencilla.

## Estructura

```
AgendaPsicologica/
├── main.py          # menú principal con NavigationRail
├── views/
│   ├── agenda.py    # tabla de citas futuras
│   └── detalle.py   # tarjetas con detalles de citas
```

Cada archivo está comentado en español y utiliza componentes básicos de Flet como `ft.DataTable`, `ft.Card` y `ft.Container`.

Para ejecutar el proyecto instale Flet y ejecute:

```bash
pip install flet
python AgendaPsicologica/main.py
```
