import sqlite3
from tkinter import messagebox


class HandlerDB:

    def __init__(self, db_path='db/gestion_est.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS estudiantes(
            legajo INTEGER PRIMARY KEY NOT NULL,
            dni INTEGER NOT NULL,
            nombre_apellido VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            domicilio VARCHAR NOT NULL,
            fecha_nac DATE NOT NULL, 
            carrera VARCHAR NOT NULL,
            ingreso DATE NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS carrera (
            id VARCHAR PRIMARY KEY,
            carrera_id INTEGER NOT NULL,
            nombre VARCHAR NOT NULL,
            cant_alumnos INTEGER NOT NULL,
            FOREIGN KEY (carrera_id) REFERENCES estudiantes(legajo))''')

        self.conn.commit()
        print("Tablas creadas correctamente")

    def create_students(self, legajo, dni, nombre_apellido, email, domicilio, fecha_nac, carrera, ingreso ):
        try:
            self.cursor.execute('''
                            INSERT INTO estudiantes (legajo, dni, nombre_apellido, email, domicilio, fecha_nac, carrera, ingreso)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (legajo, dni, nombre_apellido, email, domicilio, fecha_nac, carrera, ingreso))
            self.conn.commit()
            messagebox.showinfo("Exito", "Estudiante agregado correctamente")
        except sqlite3.Error as e:
            print(f"Error en la base de datos: {e}")

    def get_data_student(self, legajo, dni):
        try:
            self.cursor.execute('''
            SELECT legajo, dni, nombre_apellido, email, domicilio, fecha_nac, carrera, ingreso FROM estudiantes WHERE legajo = ? or dni = ?''', (legajo, dni,))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            return f"Error en la base de datos: {e}"

    def show_students(self):
        try:
            self.cursor.execute('''SELECT legajo, dni, nombre_apellido, email, domicilio, fecha_nac, carrera, 
            ingreso FROM estudiantes''')
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            return f"Error en la base de datos {e}"





