# importar la clase tiquete y importar el clear de la pantalla
from tiquete import Tiquete
from os import system

system("clear")
#El clear sirve para limpiar pantalla

# Crear una instancia de la clase "Tiquete" 
tiquete = Tiquete()

print("-"*50)
print ("***Bienvenido***")
print("-"*50)
print (" Codigo | Tipo Atencion")
print ("  1     | Compra de un Nuevo Celular")
print ("  2     | Reposion celular")
print ("  3     | Adquisición o cambio de plan")
print ("  4     | Quejas o reclamos")
print ("  5     | Otro tipo de atención")
print("-"*50)

# Ingresa elementos a la cola
#Registrar Usuarios
tiquete.push("Santiago Pineda",1)
tiquete.push("Leidy Castaño ",4)
tiquete.push("Alicia Davila",2)
tiquete.push("Diego Cruz",1)
tiquete.push("Ana Perez",5)


# Mostrar todos los usuarios registrados
print("\nUsuarios en lista: ")
print (" Codigo de Atención | Nombre")
tiquete.mostrar()

#Mostrar en pantalla la información del primer turno ingresado
print("El turno activo en este momento es:",tiquete.TurnoEnAtencion())
print("-"*50)

# Eliminar el primer turno
tiquete.pop()

#Volver a mostrar la lista de los usuarios en turno
print("\nLista de usuarios en espera: ")
print (" Codigo de Atención | Nombre")
tiquete.mostrar()
print("-"*50)