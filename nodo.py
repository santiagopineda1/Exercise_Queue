class Nodo():

  # Definir el constructor de la clase
  def __init__(self,codigoAtencion, nombre, siguiente = None):
    
    self.codigoAtencion = codigoAtencion
    self.nombre = nombre
    self.siguiente = siguiente
  
  # Formato de la salida en pantalla para el nodo
  def __str__(self):
    return str(self.codigoAtencion)