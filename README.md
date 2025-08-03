# Appointment-Calendar
Este es un programa simple para tener un cronograma fácil de manejar y de interpretar, ideal para llevar un control de citas u ordenar nuestro día a día. Las citas se guardan automáticamente en un archivo local (`citas.json`), por lo que se conservan incluso si cierras el programa.

## Características
* Interfaz gráfica construida con `customtkinter`
* Selección del día de la semana
* Elegir una hora disponible (de 7:00 a 22:30, en intervalos de 30 minutos)
* Anotar una cita con una descripción
* Eliminar una cita seleccionada
* Ver todas las citas guardadas organizadas por día y hora

### Como Usar
1. Ejecutar el programa
```bash
python3 appointment_calendar.py
```
2. Selecciona el día de la semana
3. Elige una hora disponible
4. Escribe la descripción de la cita
5. Haz clic en **Agregar Cita**
6. Debajo del botón **Agregar Cita** hay otro botón para consultar o seleccionar una cita para luego eliminarla, si deseas eliminarla entonces debes seleccionar la cita y luego presionar en **Eliminar Cita**
7. Haz clic en **Mostrar Citas** para ver todas las citas que tienes durante la semana
