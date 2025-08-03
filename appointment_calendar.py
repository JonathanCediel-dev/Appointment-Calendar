# importaciones externas
import customtkinter as ctk

# importaciones standard
import json
import os

# Definicion del archivo de almacenamiento .json, lista de días de la semana para guardar las citas en diccionarios
ARCHIVO_CITAS = "citas.json"
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
citas = {}

# cargar citas desde el archivo
def cargar_citas():
    global citas
    citas = {dia: {} for dia in dias_semana}
    if os.path.exists(ARCHIVO_CITAS):
        with open(ARCHIVO_CITAS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for dia in datos:
                citas[dia] = datos[dia]

# guardar citas en el archivo
def guardar_citas():
    with open(ARCHIVO_CITAS, "w", encoding="utf-8") as archivo:
        json.dump(citas, archivo, indent=4, ensure_ascii=False)

# generar horas posibles (7:00 a 22:30 con intervalos de 30min)
def generar_horas():
    horas = []
    for h in range(7, 22 + 1): # h hace referencias a horas
        for m in [0, 30]: # m hace referencia a minutos
            hora_formato = f"{h:02}:{m:02}"
            horas.append(hora_formato)
    return horas

# obtener horas disponibles para el día seleccionado
def obtener_horas_disponibles():
    dia = menu_dia.get()
    ocupadas = citas.get(dia, {}).keys()
    return [h for h in generar_horas() if h not in ocupadas]

# agregar una cita 
def agregar_cita():
    dia = menu_dia.get()
    hora = menu_hora.get()
    descripcion = entrada_desc.get().strip()
    if dia and hora and descripcion:
        citas[dia][hora] = descripcion
        guardar_citas()
        actualizar_lista()
        entrada_desc.delete(0, ctk.END)
        actualizar_horas()

# eliminar una cita seleccionada
def eliminar_cita():
    seleccion = caja_citas.get()
    if seleccion:
        dia = menu_dia.get()
        hora = seleccion.split(" - ")[0]
        if hora in citas[dia]:
            del citas[dia][hora]
            guardar_citas()
            actualizar_lista()
            actualizar_horas()

# actualizar la lista de citas para el dia seleccionado
def actualizar_lista():
    caja_citas.set("")
    dia = menu_dia.get()
    lista_ordenada = sorted(citas[dia].items())
    caja_citas.configure(values=[f"{h} - {d}" for h, d in lista_ordenada]) # h hace referecia a hora y d a descripcion

# mostrar todas la citas agendadas
def mostrar_todas():
    ventana_citas = ctk.CTkToplevel(ventana) # se crea una nueva ventana secundaria para mostrar todas las citas
    ventana_citas.title("Todas las citas")
    ventana_citas.geometry("500x600")

    texto = ""
    for dia in dias_semana:
        if citas[dia]:
            texto += f"{dia}:\n"
            for hora, descripcion in sorted(citas[dia].items()): # ordena las citas por hora y las agrega al texto
                texto += f"  {hora} - {descripcion}\n"
            texto += "\n"
    # crea un area de texto para mostrar todas las citas en la ventana 
    area_texto = ctk.CTkTextbox(ventana_citas, width=480, height=580)
    area_texto.insert("2.0", texto.strip() or "No hay citas registradas.")
    area_texto.configure(state="disabled")
    area_texto.pack(padx=10, pady=10)

# actualizar el menu de horas disponibles cuando se cambia el dia
def actualizar_horas(*args):
    horas_disponibles = obtener_horas_disponibles()
    menu_hora.configure(values=horas_disponibles)
    if horas_disponibles:
        menu_hora.set(horas_disponibles[0])
    else:
        menu_hora.set("")

# esta funcion se ejecuta al cambiar el día seleccionado // actualiza las horas como la lista de citas del nuevo dia
def al_cambiar_dia(nuevo_dia):
    actualizar_horas()
    actualizar_lista()

# configuracion inicial
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# creacion de la ventana principal
ventana = ctk.CTk()
ventana.title("Calendario de Citas")
ventana.geometry("440x600")

cargar_citas()

# menu desplegable para seleccionar el dia de la semana 
menu_dia = ctk.CTkOptionMenu(ventana, values=dias_semana, command=al_cambiar_dia)
menu_dia.set("Lunes")
menu_dia.pack(pady=10)

# menu desplegable para seleccionar la hora 
menu_hora = ctk.CTkOptionMenu(ventana, values=[])
menu_hora.pack(pady=5)

# campo de entrada para escribir la descripcion de la cita
entrada_desc = ctk.CTkEntry(ventana, placeholder_text="Descripción de la cita", width=300)
entrada_desc.pack(pady=5)

# boton para agregar una nueva cita
boton_agregar = ctk.CTkButton(ventana, text="Agregar cita", command=agregar_cita)
boton_agregar.pack(pady=10)

# Caja desplegable para mostrar las citas del día seleccionado
caja_citas = ctk.CTkOptionMenu(ventana, values=[], width=360)
caja_citas.pack(pady=10)

# Botón para eliminar la cita seleccionada
boton_eliminar = ctk.CTkButton(ventana, text="Eliminar cita", command=eliminar_cita)
boton_eliminar.pack(pady=10)

# Botón para mostrar todas las citas guardadas en una nueva ventana
boton_mostrar = ctk.CTkButton(ventana, text="Mostrar citas", command=mostrar_todas)
boton_mostrar.pack(pady=20)

actualizar_lista()
actualizar_horas()
ventana.mainloop()
