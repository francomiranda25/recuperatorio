# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Inversiones, realiza un estudio de mercado para saber cual será la nueva franquicia que se insertará en el 
mercado argentino y en la cual invertiram.
Las posibles franquicias son las siguientes: 
# Apple,
# Dunkin Donnuts, 
# Ikea o 
# Taco Bell.

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles
son los gustos de los encuestados:

A) Programar el boton "Cargar voto" para poder ingresar los siguientes datos:
    * nombre del encuestado.
    * edad (no menor a 18)
    * esta empleado (SI - NO)
    * voto (APPLE, DUNKIN, IKEA, TACO)   

En esta opción, se ingresará un voto a la vez.

B) Al presionar el boton mostrar se deberan listar todos los datos de los encuestados y su posición en la lista (por terminal) 

Del punto C solo debera realizar 3 informes. Para determinar qué informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal y restele el primer numero. Debera realizar ese informe. 
    En caso de que la resta de negativa, tome el valor positivo de esa resta. 

    Informe 2- Tome el ultimo numero de su DNI Personal y restarselo al numero 9. En caso de que la resta de 9, realizara 
    el informe 7. En caso de que la resta de 8, realizara el informe 6. En caso de que la resta de 3, realizara el informa 4.
    
    Informe 3- Si su DNI personal termina en un numero par, realizará el informe 9. En caso contrario realizar el informe 8.

    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    

    #! 0) - Nombre y situación laboral de las personas que votaron por IKEA con menor edad.
    #! 1) - Nombre y voto, de las personas desempleadas con mayor edad.
    #! 2) - Cuál es la empresa con mas votos.
    #! 3) - Cual es la empresa con menos votos.
    #! 4) - Porcentaje de personas que votaron por TACO, siempre y cuando su edad no se encuentre 
            entre 18 y 25.  
    #! 5) - Porcentaje de personas que no votaron por APPLE, siempre y cuando este empleado o su edad 
            se encuentre entre los 33 y 40.
    #! 6) - Cantidad de encuestados desempleados que votaron por DUNKIN o IKEA, cuya edad este entre 25 y 
            50 años inclusive.
    #! 7) - Cantidad de encuestados con empleo que votaron por APPLE, cuya edad no supere los 35 años.
    #! 8) - Nombre y edad de las personas que votaron DUNKIN o IKEA, cuya edad supere la edad promedio 
            de los que votaron por esas empresas.
    #! 9) - Nombre y edad de las personas empleadas que votaron por DUNKIN, cuya edad este por debajo 
            de la edad promedio de las personas empleadas.
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Inversiones - ENCUESTA")
        self.minsize(320, 200)

        self.label_title = customtkinter.CTkLabel(master=self, text="UTN IT - INVERSIONES", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar encuesta", command=self.btn_cargar_encuesta_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")

        self.nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
                    "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]

        self.edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49,
                    32, 22, 29, 27, 19, 49, 27, 22, 29, 27]
        
        self.trabaja = ["SI", "NO", "NO", "NO", "SI", "NO", "SI", "NO", 
                        "NO", "NO", "SI", "NO", "NO", "NO", "SI", "SI", "SI", 
                        "NO", "SI", "SI"]
        
        self.votos = ["APPLE", "DUNKIN", "IKEA", "APPLE", "TACO", "DUNKIN", "TACO", "APPLE", "TACO", "APPLE",
                    "IKEA", "APPLE", "DUNKIN", "DUNKIN", "APPLE", "IKEA", "APPLE", "DUNKIN", "IKEA", "TACO"]    
        

        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        
    def btn_mostrar_todos_on_click(self):
        i = 0
        while i < len(self.edades):
            print(str(i + 1) + ", nombres: " + self.nombres[i] + ", edades: " + str(self.edades[i]) + ", trabaja?:  " +  self.trabaja[i] + " voto: " + self.votos[i])
            i = i +1
        
        

    def btn_mostrar_informe_1(self):
        # punto 4
        votos = 0
        i = 0
        while i < len(self.nombres):
            if self.votos[i] == "TACO" and self.edades[i] > 25:
                votos = votos +1
            i = i +1
        print(str(votos * 100/ len(self.nombres)) + "%")
                
            
        
            

    def btn_mostrar_informe_2(self):
        # punto 7
        votos = 0
        i = 0
        while i < len(self.nombres):
            if self.votos[i] == "APPLE" and self.edades[i] <= 35 and self.trabaja[i]== "SI" :
                votos = votos +1
            i = i +1
        print(str(votos))

    def btn_mostrar_informe_3(self):
        # punto 9
        acumulador = 0
        i = 0
        while i < len(self.trabaja): 
            if self.trabaja[i] == "SI":
                acumulador = self.edades[i] + acumulador
            i = i+1
        promedio = acumulador / len(self.trabaja)
        i =0
        while i <len(self.trabaja):
            if self.votos[i] == "DUNKIN" and self.edades[i] < promedio:
                print(self.nombres[i]) 
            i = i +1
                

    def btn_cargar_encuesta_on_click(self):
        nombre = prompt("nombre: ", "nombre")
        if nombre == None:
            return 
        edad = prompt("edad: ", "edad")
        if edad == None or int(edad) <18:
            return
        empleado = prompt("empleado?: ", "esta empleado?")
        if empleado == None or (empleado != "SI" and empleado != "NO"):
            return
        voto = prompt("voto: ", "voto")
        if voto == None or (voto != "APPLE" and voto!= "DUNKIN" and voto != "IKEA" and voto != "TACO"):
            return 
        self.nombres.append(nombre)
        self.edades.append(int(edad))
        self.trabaja.append(empleado)
        self.votos.append(voto)


if __name__ == "__main__":
    app = App()
    app.mainloop()
