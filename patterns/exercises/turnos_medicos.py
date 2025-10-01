"""
Turnos Medicos

Contestar a continuación las siguientes preguntas:

- Qué patrón de diseño podés identificar en el código dado?

#Pude indentificar un patron singleton en la database, y un observer en la notificacion de cambios de turno- 

- Qué patrones de diseño se podrían agregar para mejorar el código?
 se puede implementar un factoty en la seccion de turnos porque evitamos poner los elif y hacemos un codigo mas legible segun las caracteriticas que posee en paciente ya sea la especialidad o la obre social
se podria agregar un decorador  y la mejora de un builder 

Implementar uno o más de estos patrones adicionales para mejorar el código.
"""

from typing import List, Optional


#class TurnosMedicos:
    #@staticmethod
    #def main():
        #print()
        #print("Turnos Medicos")
        #print("=============")
        #print()
        #database = Database.getInstance()

        #paciente = Paciente("Ignacio Segovia", "IOMA", "isegovia@gmail.com")

        #especialidad = "Cardiología"
        #doctor = database.getDoctor(especialidad)
        #if doctor is None:
            #print("No se encontró el doctor de la especialidad", especialidad)
            #return

        # Precio base en base a la especialidad
        #precio_base = 0
        #if doctor.especialidad.contiene("Cardiología"):
            #precio_base = 8000
        #elif doctor.especialidad.contiene("Neumonología"):
            #precio_base = 7000
        #elif doctor.especialidad.contiene("Kinesiología"):
            #precio_base = 7000
        #else:
            #precio_base = 5000

        # Descuento en base a la obra social y la especialidad
        #descuento = 0.0
        #if paciente.obra_social == "OSDE":
            #descuento = 1.0 if doctor.especialidad.contiene("Cardiología") else 0.2
        #elif paciente.obra_social == "IOMA":
            #descuento = 1.0 if doctor.especialidad.contiene("Kinesiología") else 0.15
        #elif paciente.obra_social == "PAMI":
            #descuento = 1.0
        #else:
            #descuento = 0.0

        # Aplico el descuento
        #precio = precio_base - precio_base * descuento

        # Nuevo turno
        #turno = Turno(paciente, doctor, "2025-01-01 10:00", precio)
        #print(turno)

        # Cambio de turno
        #turno.set_fecha_y_hora("2025-01-01 11:00")
        #print() 

class TurnosMedicos:
    @staticmethod
    def main():
        print()
        print("Turnos Medicos")
        print("==============")
        print()

        paciente = Paciente("Ignacio Segovia", "IOMA", "isegovia@gmail.com")
        especialidad = "Cardiología"

        turno = TurnoFactory.crear_turno(paciente, especialidad, "2025-01-01 10:00")
        if turno is None:
            return

        print(turno)

        turno.set_fecha_y_hora("2025-01-01 11:00")
        print()


class TurnoFactory:
    @staticmethod
    def crear_turno(paciente: Paciente, especialidad: str, fecha_y_hora: str) -> Optional[Turno]:
        database = Database.getInstance()
        doctor = database.getDoctor(especialidad)

        if doctor is None:
            print(f"No hay  el doctor de la especialidad {especialidad}")
            return None

    
        if doctor.especialidad.contiene("Cardiologia "):
            precio_base = 8000
        elif doctor.especialidad.contiene("Neumonologia"):
            precio_base = 7000
        elif doctor.especialidad.contiene("Kinesiologia"):
            precio_base = 7000
        else:
            precio_base = 5000

        
        if paciente.obra_social == "OSDE":
            descuento = 1.0 if doctor.especialidad.contiene("Cardiologia") else 0.2
        elif paciente.obra_social == "IOMA":
            descuento = 1.0 if doctor.especialidad.contiene("Kinesiologgia") else 0.15
        elif paciente.obra_social == "PAMI":
            descuento = 1.0
        else:
            descuento = 0.0

        precio = precio_base - (precio_base * descuento)
        return Turno(paciente, doctor, fecha_y_hora, precio)


class Paciente:
    def __init__(self, nombre: str, obra_social: str, email: str):
        self.nombre = nombre
        self.obra_social = obra_social
        self.email = email

    def avisar_cambio_de_fecha_y_hora(self, turno: "Turno"):
        print(
            f"Mail para {self.email}: El turno con {turno.doctor} se ha cambiado a {turno.fecha_y_hora}"
        )

    def __str__(self):
        return f"{self.nombre} ({self.obra_social})"


class Especialidad:
    def __init__(self, descripcion: str):
        self.descripcion = descripcion

    def contiene(self, descripcion: str) -> bool:
        return descripcion in self.descripcion

    def __str__(self):
        return self.descripcion


class Doctor:  
    def __init__(self, nombre: str, especialidad: Especialidad, email: str):
        self.nombre = nombre
        self.especialidad = especialidad
        self.email = email

    def avisar_cambio_de_fecha_y_hora(self, turno: "Turno"):
        print(
            f"Mail para {self.email}: El turno para {turno.paciente} se cambio a {turno.fecha_y_hora}"
        )

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"


class Turno:  
    def __init__(
        self, paciente: Paciente, doctor: Doctor, fecha_y_hora: str, precio: float
    ):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha_y_hora = fecha_y_hora
        self.precio = precio

    def set_fecha_y_hora(self, fecha_y_hora: str):
        self.fecha_y_hora = fecha_y_hora
        self.avisar_cambio_de_fecha_y_hora(self)

    def avisar_cambio_de_fecha_y_hora(self, turno: "Turno"):
        self.doctor.avisar_cambio_de_fecha_y_hora(turno)
        self.paciente.avisar_cambio_de_fecha_y_hora(turno)

    def __str__(self):
        return f"Turno para {self.paciente} con {self.doctor} el {self.fecha_y_hora} - ${self.precio}"


class Database:  
    _instance = None
    _doctores: List[Doctor] = []

    def __init__(self):
        self._doctores = [
            CreadorDeDoctores.crear_cardiologo(
                "Dra. Girgenti Liliana",
                "lgirgenti@gmail.com",
            ),
            CreadorDeDoctores.crear_neumonologo(
                "Dr. Jorge Gutierrez",
                "jgutierrez@gmail.com",
            ),
            CreadorDeDoctores.crear_alergista(
                "Dra. Florencia Aranda",
                "faranda@gmail.com",
            ),
            CreadorDeDoctores.crear_clinico_general(
                "Dr. Esteban Quiroga",
                "equiroga@gmail.com",
            ),
            CreadorDeDoctores.crear_traumatologo(
                "Dr. Mario Gómez",
                "mgomez@gmail.com",
            ),
        ]

    @classmethod
    def getInstance(cls) -> "Database":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def getDoctor(self, descripcion_especialidad: str) -> Optional[Doctor]:
        for doctor in self._doctores:
            if doctor.especialidad.contiene(descripcion_especialidad):
                return doctor
        return None


class CreadorDeDoctores:

    @staticmethod
    def crear_cardiologo(nombre: str, email: str):
        return Doctor(nombre, Especialidad("Cardiología > General"), email)

    @staticmethod
    def crear_neumonologo(nombre: str, email: str):
        return Doctor(nombre, Especialidad("Neumonología > General"), email)

    @staticmethod
    def crear_alergista(nombre: str, email: str):
        return Doctor(nombre, Especialidad("Neumonología >Alergias"), email)

    @staticmethod
    def crear_traumatologo(nombre: str, email: str):
        return Doctor(nombre, Especialidad("Kinesiología > Traumatología"), email)

    @staticmethod
    def crear_kinesiologo(nombre: str, email: str):
        return Doctor(nombre, Especialidad("Kinesiología > General"), email)

    @staticmethod
    def crear_clinico_general(nombre: str, email: str):
        return Doctor(nombre, Especialidad("Clínica > General"), email)
    
#aca creo que se podria hacer un builder mas generalizado, en vez de crear un clinico por cada especialidad, se crea un clinico solo, que despues se le agrega el atributo de especialidad. 

#por ejemplo: 
#clino.self = clinico
#especialidad.self = especialidad
#emaiñ.self = email 
#y ahi despues retornar los valores mediante una entrada de valores (perdon no se explicar xd como una estructura paso por paso que funcione para todos) pero tal vez este equivocada 




if __name__ == "__main__":
   TurnosMedicos.main()

