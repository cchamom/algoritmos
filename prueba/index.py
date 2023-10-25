from tkinter import Tk, Button, Entry, Label, ttk, StringVar, Frame, messagebox
from conexion import Comunicacion
from tkcalendar import Calendar, DateEntry

class Ventana(Frame):
    def __init__(self, master):
        super().__init__(master)
        
  
        self.Nombre = StringVar()
        self.Asunto = StringVar()
        self.Correo = StringVar()
        self.Telefono = StringVar()
        self.Fecha = StringVar()

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=5)

        self.base_datos = Comunicacion()

        self.widgets()

#calendario
    def mostrar_el_calendario(self):
        calendario = Tk()
        calendario.title("Calendario")
        calendario.config(bg="deepskyblue")
        calendario.geometry("110x60")

        def selecionar_fecha():
          fecha_seleccionada = cal.get()
          self.Fecha.set(fecha_seleccionada)
          calendario.destroy()

        cal = DateEntry(calendario, widh="30", bg="darkblue", font=('Arial', 9, 'bold'), fg="whitr", year=2023)
        cal.grid()

        Button(calendario, text="Seleccione la fecha", bg="royalblue",command=selecionar_fecha).grid()
        
        calendario.mainloop()

    def widgets(self):
        self.frame_uno = Frame(self.master, bg='deepskyblue', height=200, width=800)
        self.frame_uno.grid(column=0, row=0, sticky='nsew')
        self.frame_dos = Frame(self.master, bg='white', height=300, width=800)
        self.frame_dos.grid(column=0, row=1, sticky='nsew')

        self.frame_uno.columnconfigure([0, 1, 2], weight=1)
        self.frame_uno.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

        Label(self.frame_uno, text="Opciones", bg="deepskyblue", fg="black", font=("Kaufmann BT", 13, "bold",)).grid(
            column=2, row=0)
        Button(self.frame_uno, text="ACTUALIZAR", font=("Arial", 9, "bold"),
               command=self.actualizar_tabla, fg="black", bg="orange", width=20, bd=3).grid(column=2, row=1, pady=5)
        Label(self.frame_uno, text="REGISTRO DE PACIENTES", fg="black", bg="deepskyblue",
              font=("Rockwell", 20, "bold",)).grid(columnspan=3, column=0, row=0, pady=5)

        Label(self.frame_uno, text="Nombre", fg="black", bg="deepskyblue", font=("Rockwell", 13, "bold",)).grid(column=0,row=1, pady=5)
        Label(self.frame_uno, text="Asunto", fg="black", bg="deepskyblue", font=("Rockwell", 13, "bold",)).grid(column=0,row=2, pady=5)
        Label(self.frame_uno, text="Correo", fg="black", bg="deepskyblue", font=("Rockwell", 13, "bold",)).grid(column=0, row=3, pady=5)
        Label(self.frame_uno, text="Telefono", fg="black", bg="deepskyblue", font=("Rockwell", 13, "bold",)).grid(column=0, row=4, pady=5)
        Label(self.frame_uno, text="Fecha", fg="black", bg="deepskyblue", font=("Rockwell", 13, "bold",)).grid(column=0,row=5, pady=5)

        Entry(self.frame_uno, textvariable=self.Nombre, font=("Comic Sans MS", 12), highlightbackground="blue", bg="white", highlightthickness=5).grid(column=1, row=1)
        Entry(self.frame_uno, textvariable=self.Asunto, font=("Comic Sans MS", 12), highlightbackground="blue", bg="white", highlightthickness=5).grid(column=1, row=2)
        Entry(self.frame_uno, textvariable=self.Correo, font=("Comic Sans MS", 12), highlightbackground="blue", bg="white", highlightthickness=5).grid(column=1, row=3)
        Entry(self.frame_uno, textvariable=self.Telefono, font=("Comic Sans MS", 12), highlightbackground="blue", bg="white", highlightthickness=5).grid(column=1, row=4)
        Entry(self.frame_uno, textvariable=self.Fecha, font=("Comic Sans MS", 12), highlightbackground="blue", bg="white", highlightthickness=5).grid(column=1, row=5)

        Button(self.frame_uno, text='Añadir Datos', font=('Arial', 9, 'bold'), bg='red',
               width=20, bd=3, command=self.agregar_datos).grid(column=2, row=2, pady=5, padx=5)
        Button(self.frame_uno, text='Limpiar Datos', font=('Arial', 9, 'bold'), bg='limegreen',
               width=20, bd=3, command=self.limpiar_campos).grid(column=2, row=3, pady=5, padx=5)
        Button(self.frame_uno, text='Actualizar Datos', font=('Arial', 9, 'bold'), bg='yellow',
               width=20, bd=3, command=self.actualizar_datos).grid(column=2, row=4, pady=5, padx=5)
        Button(self.frame_uno, text='Calendario', font=('Arial', 9, 'bold'), bg='royal blue',
               width=20, bd=3, command=self.mostrar_el_calendario).grid(column=2, row=5, pady=5, padx=5)

        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font=('Helvetica', 10, 'bold'), foreground='black',
                              background='white')
        estilo_tabla.map('Treeview', background=[('selected', 'deep sky blue')],
                         foreground=[('selected', 'black')])
        estilo_tabla.configure('Heading', background='white', foreground='black',
                              padding=3, font=('Arial', 10, 'bold'))

        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_dos, orient='horizontal', command=self.tabla.xview)
        ladox.grid(column=0, row=1, sticky='ew')
        ladoy = ttk.Scrollbar(self.frame_dos, orient='vertical', command=self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky='ns')
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        self.tabla['columns'] = ('Asunto', 'Correo', 'Telefono', 'Fecha')
        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Asunto', minwidth=100, width=120, anchor='center')
        self.tabla.column('Correo', minwidth=100, width=120, anchor='center')
        self.tabla.column('Telefono', minwidth=100, width=120, anchor='center')
        self.tabla.column('Fecha', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text='Nombre', anchor='center')
        self.tabla.heading('Asunto', text='Asunto', anchor='center')
        self.tabla.heading('Correo', text='Correo', anchor='center')
        self.tabla.heading('Telefono', text='Telefono', anchor='center')
        self.tabla.heading('Fecha', text='Fecha', anchor='center')

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        self.tabla.bind("<Double-1>", self.eliminar_datos)

    def obtener_fila(self, event):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        self.Nombre.set(self.data['text'])
        self.Asunto.set(self.data['values'][0])
        self.Correo.set(self.data['values'][1])
        self.Telefono.set(self.data['values'][2])
        self.Fecha.set(self.data['values'][3])

    def eliminar_datos(self, event):
        self.limpiar_campos()
        item = self.tabla.selection()[0]
        x = messagebox.askquestion('Informacion', '¿Desea eliminar al paciente?')
        if x == 'yes':
            self.tabla.delete(item)
            self.base_datos.eliminar_datos(self.data['text'])

    def agregar_datos(self):
        nombre = self.Nombre.get()
        asunto = self.Asunto.get()
        correo = self.Correo.get()
        telefono = self.Telefono.get()
        fecha = self.Fecha.get()
        datos = (asunto, correo, telefono, fecha)
        if nombre and asunto and correo and telefono and fecha != '':
            self.tabla.insert('', 0, text=nombre, values=datos)
            self.base_datos.inserta_datos(nombre, asunto, correo, telefono, fecha)
            self.limpiar_campos()

        if not nombre or not asunto or not correo or not telefono:
            messagebox.showerror("!Upss¡", "Llena los campos para poder ingresar al paciente")

    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.base_datos.mostrar_datos()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in datos:
            i = i + 1
            self.tabla.insert('', i, text=datos[i][1:2][0], values=datos[i][2:6])

    def actualizar_datos(self):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        nombre = self.data['text']
        datos = self.base_datos.mostrar_datos()
        for fila in datos:
            Id = fila[0]
            nombre_bd = fila[1]
            if nombre_bd == nombre:
                if Id is not None:
                    nombre = self.Nombre.get()
                    asunto = self.Asunto.get()
                    correo = self.Correo.get()
                    telefono = self.Telefono.get()
                    fecha = self.Fecha.get()
                    if nombre and asunto and correo and telefono and fecha != '':
                        self.base_datos.actualizar_datos(Id, nombre, asunto, correo, telefono, fecha)
                        self.tabla.delete(*self.tabla.get_children())
                        datos = self.base_datos.mostrar_datos()
                        i = -1
                        for dato in datos:
                            i = i + 1
                            self.tabla.insert('', i, text=datos[i][1:2][0], values=datos[i][2:6])

    def limpiar_campos(self):
        self.Nombre.set('')
        self.Asunto.set('')
        self.Correo.set('')
        self.Telefono.set('')
        self.Fecha.set('')

if __name__ == "__main__":
    ventana = Tk()
    ventana.title('REGISTRO DE PACIENTES')
    ventana.minsize(height=400, width=600)
    ventana.geometry("800x500")
    app = Ventana(ventana)
    app.mainloop()
