from patron import Patron

if __name__ == "__main__":
    personaje = (
        Patron()
        .set_nombre("Sunday")
        .set_rol("Soporte")
        .set_elemento("Imaginario")
        .set_via("Armonia")
        .set_planeta("Colonipenal")
        .build()
        )
    
    print(personaje) 


    #aca ya le asignamos los valores 