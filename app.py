import tkinter as tk
import customtkinter as ctk
import os

from util_openai import organizar_directorio

def obtener_directorios():
    nombres_dirs = os.listdir()
    nombres_dirs = ', '.join(nombres_dirs)
    nombres_dirs = f'Nombres: {nombres_dirs}'
    return nombres_dirs

def agregar_entry(frame):
    entry_frame = ctk.CTkFrame(frame)
    nuevo_entry = ctk.CTkEntry(entry_frame)
    nuevo_entry.pack(padx=5,pady=5, side='left')
    borrar_entry = ctk.CTkButton(entry_frame, text='X', command= lambda:borrar_entry(entry_frame))
    borrar_entry.pack(padx=5, pady=5, side='left')
    entry_frame.pack()

    def borrar_entry(entry):
        entry.destroy()

def organizar_archivos(api, frame):
    clasificaciones = []

    for item in frame.pack_slaves():
        if isinstance(item, ctk.CTkFrame):
            clasificaciones.append(item.children['!ctkentry'].get())

    clasificaciones_dirs = ', '.join(clasificaciones)
    clasificaciones_dirs = f'Clasificaciones: {clasificaciones_dirs}'
    nombres_dirs = obtener_directorios()

    clasificaciones_nombres = f'{clasificaciones_dirs}; {nombres_dirs}'

    print(organizar_directorio(api, clasificaciones_nombres))

def menu():
    ctk.set_appearance_mode('dark')
    ctk.set_appearance_mode('dark-blue')

    root = ctk.CTk()

    root.title('Organizador de Archivos')

    frame = ctk.CTkScrollableFrame(root)
    frame.pack(pady=10)

    agregar_entry_button = ctk.CTkButton(frame, text='Nuevo', command=lambda: agregar_entry(frame))
    agregar_entry_button.pack(padx=10,pady=10)

    api_entry = ctk.CTkEntry(root)
    api_entry.pack(padx=5, pady=5)

    organizar_archivos_button = ctk.CTkButton(root, text='Organizar', command=lambda: organizar_archivos(api_entry.get(), frame))
    organizar_archivos_button.pack(padx=10,pady=10)
    root.mainloop()

if __name__ == '__main__':
    menu()