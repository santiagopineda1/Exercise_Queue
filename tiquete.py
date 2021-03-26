#importar la clase nodo
from nodo import Nodo

#crear la clase tiquete
class Tiquete():
 # Constructor de la clase tiquete
  def __init__(self):
    self.front = None # Primer elemento
    self.rear = None # Último elemento
    self.size =0

  # Operación para definir si una cola está vacía
  def colaVacia(self):
    return self.size == 0
  
  # Operación para mostrar la cola
  def mostrar(self):
    aux = self.front
    while aux != None:
      print(aux.nombre, "                  |",aux.codigoAtencion,end=" ")
      print("")
      aux = aux.siguiente
    print ("")
    
      
  # Operación para agregar un elemento en la cola
  # Se agrega el front, la operación es enqueue
  def push(self, nombre,codigoAtencion):
    nuevoNodo = Nodo(nombre,codigoAtencion)
    #validar que la cola si hay datos
    if self.colaVacia():
      self.front = self.rear = nuevoNodo
    else:
      # Asignar el puntero siguiente del último elemento en la cola
      self.rear.siguiente = nuevoNodo
      # El rear pasa a ser el nuevo elemento ingresado
      self.rear = nuevoNodo
    # Aumentar el tamaño de la cola
    self.size += 1 


  # Operación para retirar un elemento de la cola
  # Se retira el rear, la operación es dequeue
  def pop(self):
    # Verificar si la pila está vacía
    if self.colaVacia():
      print("\nError: No es posible eliminar un elemento de una cola vacía.")
    # Verificar si queda solamente un elemento en la pila  
    elif self.front == self.rear:
      self.front = self.rear = None
      self.size -= 1
    # Realizar la operación pop
    else:
      self.front = self.front.siguiente
      self.size -= 1

  # Operación para mostrar el primer elemento en la cola
  def TurnoEnAtencion(self):
    return self.front