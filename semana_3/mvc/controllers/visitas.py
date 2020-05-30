'''
Nombre del alumno: Adolfo León Barrón 
Profesor: Salvador Hernández Mendoza
Materia: Aplicaciones web para I4.0
Grupo: TIBIS-51
'''
import web
from datetime import date #Importamos date que es la libreria de donde obtendremos la fecha
from datetime import datetime #Con datetime vamos a obtener la hora

class Visitas:
  def GET(self, nombre):
    try:
      cookie = web.cookies() #Establecemos el nombre de la cookie
      visitas = "0" #Inicializamos el numero de visitas en 0
      fecha = date.today() #Obtenemos la fecha del dia de hoy
      now = datetime.now()
      format = now.strftime("Hora: %H, Minutos: %M, Segundos: %S")

      #Se define el campo de "nombre" en la cookie en caso de no existir se inicializa como "Anonimo"
      if nombre:
        web.setcookie("nombre", nombre, expires = "", domain=None)
      else:
        nombre = "Anonimo"
        web.setcookie("nombre", nombre, expires = "", domain=None) 

      #Se anexa a la cookie el numero de visitas realizadas en caso de ser la primer visita se inicializa en 1
      if cookie.get("visitas"):
        visitas = int(cookie.get("visitas"))
        visitas += 1
        web.setcookie("visitas", str(visitas),expires = "",  domain = None)
      else:
        web.setcookie("visitas", str(1), expires = "", domain = None)
        visitas = "1"
        

      #Se anexa a la cookie la fecha actual, exista o no la fecha se inicializa en la fecha actual
      if cookie.get("fecha"):
        web.setcookie("fecha", fecha, expires="", domain=None)
      else:
        web.setcookie("fecha", fecha, expires="", domain=None)

      #Se anexa a la cookie la hora actual, de igual manera que la fecha se inicializa siempre en la hora actual
      if cookie.get("Hora"):
        web.setcookie("Hora", format, expires="", domain=None)
      else:
        web.setcookie("Hora", format, expires="", domain=None)
      
      #Mostrar los resultados (Nombre, numero de visitas fecha y hora)
      return "Numero de visitas: " + str(visitas) + "\nNombre: " + str(nombre) + "\nFecha actual: "+ str(fecha) + "\n" + str(format)
      print(cookie)
    
    #En caso de presentar un error en la pantalla se mostrará dicho error
    except Exception as e:
      return "error "+str(e.args)
