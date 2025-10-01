"""
Turnos Medicos

Contestar a continuación las siguientes preguntas:

- Qué patrón de diseño podés identificar en el código dado?
- los patrones que se pueden identificar son el factory que se utiliza para la creación de doctores, el singleton que se utiliza para la base de datos
  y tambien el observer que se utiliza para notificar a los pacientes y doctores sobre cambios en los turnos.

- Qué patrones de diseño se podrían agregar para mejorar el código?
- el patrón strategy podría ser útil para separar la lógica de cálculo de precios y descuentos teniendolas en clases separadas.

Implementar uno o más de estos patrones adicionales para mejorar el código.
"""

from typing import List, Optional

class TurnosMedicos:
    @staticmethod
    def main():
        print()
        print("Turnos Medicos")
        print("=============")
        print()
        database = Database.getInstance()

        paciente = Paciente("Ignacio Segovia", "IOMA", "isegovia@gmail.com")

        especialidad = "Cardiología"
        doctor = database.getDoctor(especialidad) 
        if doctor is None:
            print("No se encontró el doctor de la especialidad", especialidad)
            return
        # precios base por especialidad
        precio_base = 0
        if doctor.especialidad.contiene("Cardiología"):
            precio_base = 8000
        elif doctor.especialidad.contiene("Neumonología"):
            precio_base = 7000
        elif doctor.especialidad.contiene("Kinesiología"):
            precio_base = 7000
        else:
            precio_base = 5000

        # descuento segun OS y especialidad
        descuento = 0.0
        if paciente.obra_social == "OSDE":
            descuento = 1.0 if doctor.especialidad.contiene("Cardiología") else 0.2 
        elif paciente.obra_social == "IOMA":
            descuento = 1.0 if doctor.especialidad.contiene("Kinesiología") else 0.15
        elif paciente.obra_social == "PAMI":
            descuento = 1.0
        else:
            descuento = 0.0
        
        # Aplico el descuento
#       precio = precio_base - precio_base * descuento

        # Nuevo turno
#       turno = Turno(paciente, doctor, "2025-01-01 10:00", precio)
#        print(turno)

        # Cambio de turno
#        turno.set_fecha_y_hora("2025-01-01 11:00")
#        print()#

        #aplicar descuento
        precio = precio_base - precio_base * descuento

        #calculo de precio y descuento (strategy)
        Precio_st = select_precio_st(doctor)
        descuento_st = select_descuento_st(paciente.obra_social)

        precio_base = Precio_st.calcular_precio(doctor)
        descuento = descuento_st.calcular_descuento(doctor)
        precio = precio_base - precio_base * descuento  

#=================================strategy=====================================

#precios
class Preciost:
    def calcular_precio(self, doctor: "Doctor") -> float:
        raise NotImplementedError

class cardiopreciost(Preciost):
    def calcular_precio(self, doctor: "Doctor") -> float:
        return 8000
    
class neumopreciost(Preciost):
    def calcular_precio(self, doctor: "Doctor") -> float:
        return 7000

class kinesiopreciost(Preciost):
    def calcular_precio(self, doctor: "Doctor") -> float:
        return 7000
    
class generalpreciost(Preciost):
    def calcular_precio(self, doctor: "Doctor") -> float:
        return 5000
    
def select_precio_st(doctor: "Doctor") -> Preciost:
    if doctor.especialidad.contiene("Cardiología"):
        return cardiopreciost()
    elif doctor.especialidad.contiene("Neumonología"):
        return neumopreciost()
    elif doctor.especialidad.contiene("Kinesiología"):
        return kinesiopreciost()
    else:
        return generalpreciost()
    
#desduentos
class Descuentost:
    def clacular_descuento(self, paciente: "Paciente" , doctor: "Doctor") -> float:
        raise NotImplementedError
    
class osdedescuentost(Descuentost):
    def calcular_descuento(self, paciente: "Paciente", doctor: "Doctor") -> float:
        return 1.0 if doctor.especialidad.contiene("Cardiología") else 0.2
    
class iomadescuentost(Descuentost):
    def calcular_descuento(self, paciente: "Paciente", doctor: "Doctor") -> float:
        return 1.0 if doctor.especialidad.contiene("Kinesiología") else 0.15
 
class pamidescuentost(Descuentost):
    def calcular_descuento(self, paciente: "Paciente", doctor: "Doctor") -> float:
        return 1.0
class nodescuentost(Descuentost):
    def calcular_descuento(self, paciente: "Paciente", doctor: "Doctor") -> float:
        return 0.0
    
def select_descuento_st(obra_social: str) -> Descuentost:
    if obra_social == "OSDE":
        return osdedescuentost()
    elif obra_social == "IOMA":
        return iomadescuentost()
    elif obra_social == "PAMI":
        return pamidescuentost()
    return nodescuentost()
#======================================================================

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
            f"Mail para {self.email}: El turno para {turno.paciente} se ha cambiado a {turno.fecha_y_hora}"
        )

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"

#=================================OBSERVER=====================================
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

#=================================SINGLETON=====================================
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

#=================================FACTORY=====================================

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


if __name__ == "__main__":
    TurnosMedicos.main()
