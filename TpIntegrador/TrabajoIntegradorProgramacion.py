#TRABAJO INTEGRADOR PROGRAMACION
import csv

#==VARIABLES==
datos = []
salir = False
opcion = ""
continentes = ["America", "Africa", "Asia", "Europa", "Oceania", "Antartida"]
datosFiltrados = []

#==FUNCIONES==
def traerDatos():
 datos.clear()
 with open(r'C:\apache\htdocs\trabajos programacion\models\TpIntegrador\archivo.csv', mode='r', encoding='utf-8') as fichero:
    lector = csv.reader(fichero)
    for fila in lector:
        if(not fila or fila[0] == "nombre" ): continue
        datos.append(fila)
 return datos

def guardarDatos(array):
   with open('C:\\apache\\htdocs\\trabajos programacion\\models\\TpIntegrador\\archivo.csv', mode='a', newline='', encoding='utf-8') as fichero:
    escritor = csv.writer(fichero)
    escritor.writerow(array)
    print("Datos guardados correctamente!")

def actualizarDatos(array):
   with open(r'C:\apache\htdocs\trabajos programacion\models\TpIntegrador\archivo.csv', mode='w', newline='', encoding='utf-8') as fichero:
      escritor = csv.writer(fichero)
      escritor.writerows(array)
      print("Datos actualizados correctamente!")

def buscarPais(string):
  with open(r'C:\apache\htdocs\trabajos programacion\models\TpIntegrador\archivo.csv', mode='r', encoding='utf-8') as fichero:
    lector = csv.reader(fichero)
    for fila in lector:
        if(string in fila[0]): 
           datos.append(fila)
    return datos
def mostrarResultados(array, buscador):
   if(len(array) > 0):
      print(f"==RESULTADOS DE '{buscador}'")
      i = 1
      for datoFiltrado in array:
       print(f"{i}) Pais: {datoFiltrado[0]} | Continente: {datoFiltrado[3]} | Poblacion: {datoFiltrado[1]} | Superficie: {datoFiltrado[2]}")
       i += 1
      print("")
      input("Pulsa una tecla para salir")
   else:
      print(f"No hay resultados para: '{buscador}'")

#==CODIGO OPERABLE==
print("==BIENVENIDO AL DICCIONARIO DE PAISES==")
traerDatos()
#==MENU DE OPCIONES==
while(salir == False):
   print("\n==OPCIONES==")
   print("1) Agregar pais")
   print("2) Actualizar datos pais")
   print("3) Buscar pais")
   print("4) Aplicar filtros")
   print("5) Aplicar Ordenes")
   print("6) Mostrar estadisticas")
   print("7) Salir")
   opcion = input("Que opcion desea elegir: ")
   print("")

#==VALIDACION DE OPCIONES==
   if(opcion == "1"):
    pais = []
    datos = traerDatos()
    print("")
    print("==AÑADIR PAIS==")
    nombrePais = input("Dame el nombre del pais: ")
    if(nombrePais.isalpha() and nombrePais != "" and not any(nombrePais.title() in dato for dato in datos)):
        pais.append(nombrePais.title())
        poblacionPais = input(f"De cuanto es la poblacion de {nombrePais.title()}: ")
        if(poblacionPais.isdigit() and int(poblacionPais) > 0):
           pais.append(poblacionPais)
           superficiePais = input(f"De cuanto es la superficie de {nombrePais.title()} (en km cuadrados): ")
           if(superficiePais.isdigit() and int(superficiePais) > 0):
              pais.append(superficiePais)
              contienentePais = input(f"En que continente esta ubicado {nombrePais.title()}: ")
              if(contienentePais.isalpha and contienentePais != "" and contienentePais.title() in continentes):
                 pais.append(contienentePais.title())
                 print("==RESULTADO FINAL==")
                 print(f"Pais: {pais[0]} | Poblacion: {pais[1]} | Poblacion: {pais[2]} | Continente: {pais[3]}")
                 opcion = input("Desea guardar el pais?(si/no)")
                 if(opcion == "si"):
                    guardarDatos(pais)
                 else:
                  print("No se guardaron los datos")
              else:
                 print("Contiente no válido")
           else:
              print("Superficie no válida")
        else:
           print("Poblacion no válida")
    else:
       print("Nombre de pais no válido")
   elif(opcion == "2"):
      print("")
      print("==ACTUALIZAR PAIS==")
      datos = traerDatos()
      datosFiltrados = []
      nombrePais = input("Dime el nombre del pais a actualizar: ")
      for dato in datos:
         if(nombrePais.isalpha() and nombrePais != "" and nombrePais.title() in dato[0]):
            datosFiltrados.append(dato)
      if(len(datosFiltrados) > 0):
         i = 1
         print("")
         print("==RESULTADOS==")
         for datoFiltrado in datosFiltrados:
            print(f"{i}) Pais: {datoFiltrado[0]} | Poblacion: {datoFiltrado[1]} | Superficie: {datoFiltrado[2]} | Continente : {datoFiltrado[3]}")
            i += 1  
         try: 
            opcion = int(input("Que pais deseas actualizar: "))
         except ValueError:
            print("La opcion no es válida")
         except IndexError:
            print("La opcion esta fuera de las opciones disponibles")
         else:
            paisSeleccionado = datosFiltrados[opcion - 1]
            print(f"Poblacion actual de '{paisSeleccionado[0]}': {paisSeleccionado[1]}")
            nuevaPoblacion = input("Introduzca la nueva poblacion(Enter para saltar): ")
            if(nuevaPoblacion.isdigit() and int(nuevaPoblacion) > 0):
               paisSeleccionado[1] = nuevaPoblacion
            print("")
            print(f"Superficie actual de '{paisSeleccionado[0]}': {paisSeleccionado[2]}")
            nuevaSuperficie = input("Introduzca la nueva superficie(Enter para saltar): ")
            if(nuevaSuperficie.isdigit() and int(nuevaSuperficie) > 0):
               paisSeleccionado[2] = nuevaSuperficie
            print("")
            print(f"Continente actual de '{paisSeleccionado[0]}': {paisSeleccionado[3]}")
            nuevoContinente = input("Introduzca el nuevo continente(Enter para saltar): ")
            if(nuevoContinente.isalpha and nuevoContinente != "" and nuevoContinente.title() in continentes):
               paisSeleccionado[3] = nuevoContinente.title()
            for i in range(len(datos)):
               if datos[i][0] == paisSeleccionado[0]:
                datos[i] = paisSeleccionado
            actualizarDatos(datos)
      else:
         print(f"No hay coincidencias para '{nombrePais.title()}'")
   elif(opcion == "3"):
    i = 1
    datos = traerDatos()
    datosFiltrados = []
    print("")
    print("==BUSCAR PAIS==") 
    nombrePais = input("Dime el nombre del pais a buscar: ")
    for dato in datos:
         if(nombrePais.isalpha() and nombrePais != "" and nombrePais.title() in dato[0]):
            datosFiltrados.append(dato)
    if(len(datosFiltrados) > 0):
      print("==RESULTADOS==")
      for datoFiltrado in datosFiltrados:
         print(f"{i}) Pais: {datoFiltrado[0]} | Poblacion: {datoFiltrado[1]} | Superficie: {datoFiltrado[2]} | Continente : {datoFiltrado[3]}")
         i += 1 
      print("")
    else:
       print(f"No hay resultados para: '{nombrePais}'")
   elif(opcion == "4"):
      print("")
      datosFiltrados = []
      datos = traerDatos()
      print("==APLICAR FILTROS==")
      opcion = input("Por que deseas filtrar: 1) Continente 2) Poblacion 3) Superficie : ")
      if(opcion == "1"):
         print("==CONTINENTES==")
         for continente in continentes:
            print(f"-{continente}")
         opcion = input("Por que continente deseas filtrar: ")
         if(opcion.isalpha() and opcion != ""):
            for dato in datos:
               if(opcion.title() == dato[3]):
                  datosFiltrados.append(dato)
            mostrarResultados(datosFiltrados, opcion.title())
         else:
                  print("Continente no válido")
      elif(opcion == "2"):
         print("==POBLACION==")
         rangoInicial = 0
         rangoFinal = 0
         try:
            rangoInicial = int(input("Dime el rango inicial: "))
         except Exception:
            print("Numero no válido")
         else:
           if(rangoInicial >= 0):
            try:
               rangoFinal = int(input("Dime el rango final: "))
            except Exception:
               print("Numero no válido") 
            else:
               if(rangoFinal > 0 and rangoFinal > rangoInicial):
                  for dato in datos:
                     if(rangoInicial <= int(dato[1]) and int(dato[1]) <= rangoFinal):
                        datosFiltrados.append(dato)
                  mostrarResultados(datosFiltrados, f"{rangoInicial} - {rangoFinal}")
               else:
                  print("Rango final no válido")
           else:
                  print("Rango inicial no válido")
      elif(opcion == "3"):
         print("==SUPERFICIE==")
         rangoInicial = 0
         rangoFinal = 0
         try:
            rangoInicial = int(input("Dime el rango inicial: "))
         except Exception:
            print("Numero no válido")
         else:
           if(rangoInicial >= 0):
            try:
               rangoFinal = int(input("Dime el rango final: "))
            except Exception:
               print("Numero no válido") 
            else:
               if(rangoFinal > 0 and rangoFinal > rangoInicial):
                  for dato in datos:
                     if(rangoInicial <= int(dato[2]) and int(dato[2]) <= rangoFinal):
                        datosFiltrados.append(dato)
                  mostrarResultados(datosFiltrados, f"{rangoInicial} - {rangoFinal}")
               else:
                  print("Rango final no válido")
           else:
              print("Rango inicial no válido")
      else:
         print("Opcion no válida")
   elif(opcion == "5"):
      traerDatos()
      print("==ORDENAR PAISES==")
      opcion = input("A cual elemento del pais deseas aplicar el orden(nombre/poblacion/superficie): ")
      if(opcion.lower() == "nombre"):
         print("\n==ORDEN APLICADO: 'nombres'==")
         datosOrdenados = sorted(datos, key=lambda pais: pais[0])
         for datosOrdenado in datosOrdenados:
            print(f"Pais: {datosOrdenado[0]} | Poblacion: {datosOrdenado[1]} | Superficie: {datosOrdenado[2]} | Continente: {datosOrdenado[3]}")
      elif(opcion.lower() == "poblacion"):
         print("\n==ORDEN APLICADO: 'poblacion'==")
         datosOrdenados = sorted(datos, key=lambda pais: int(pais[1]))
         for datosOrdenado in datosOrdenados:
            print(f"Poblacion: {datosOrdenado[1]} | Pais: {datosOrdenado[0]} | Superficie: {datosOrdenado[2]} | Continente: {datosOrdenado[3]}")
      elif(opcion.lower() == "superficie"):
         orden = input("Orden ascendente o descendente: ")
         print("\n==ORDEN APLICADO: 'superficie'==")
         datosOrdenados = sorted(datos, key=lambda pais: int(pais[2]))
         if(orden.lower() == "ascendente"):
            for datosOrdenado in datosOrdenados:
               print(f"Superficie: {datosOrdenado[2]} | Pais: {datosOrdenado[0]} | Poblacion: {datosOrdenado[1]} | Continente: {datosOrdenado[3]}")
         elif(orden.lower() == "descendente"):
               datosOrdenados.reverse()
               for datosOrdenado in datosOrdenados:
                  print(f"Superficie: {datosOrdenado[2]} | Pais: {datosOrdenado[0]} | Poblacion: {datosOrdenado[1]} | Continente: {datosOrdenado[3]}") 
         else:
            print("Opcion no válida")
      else:
         print("Opcion no válida") 
   elif(opcion == "6"):
      traerDatos()
      print("==ESTADISTICAS GENERALES==")
      paisMayorPob, paisMenorPoblacion = "", ""
      promedioHab = 0
      promedioSup = 0
      paisCont = {}
      menorPoblacion = min(datos, key=lambda pais: pais[1])
      mayorPoblacion = max(datos, key=lambda pais: pais[1])

      print(mayorPoblacion)
      
      for i in range(len(datos)):
         # if int(datos[i][1]) < menorPoblacion:
         #    menorPoblacion = int(datos[i][1])
         #    paisMenorPoblacion = datos[i][0]
         # if int(datos[i][1]) > mayorPoblacion: 
         #    mayorPoblacion = int(datos[i][1])
         #    paisMayorPob = datos[i][0]
         promedioHab += int(datos[i][1])
         promedioSup += int(datos[i][2])
      for dato in datos:
            if dato[3] in paisCont:
               paisCont[dato[3]] += 1
            else:
               paisCont[dato[3]] = 1
      print("==MENOR POBLACION==")
      print(f"- {paisMenorPoblacion} con un total de {menorPoblacion} habitantes\n")
      print("==MAYOR POBLACION==")
      print(f"- {paisMayorPob} con un total de {mayorPoblacion} habitantes\n")
      print("==PROMEDIO DE POBLACION==")
      print(f"El promedio de habitantes entre los paises es de: {promedioHab / len(datos)} habitantes\n")
      print("==PROMEDIO DE SUPERFICIE==")
      print(f"El promedio de superficie entre los paises es de: {promedioSup / len(datos)} Km\n")
      print("==PAISES POR CONTINENTES==")
      for pais in paisCont:
         print(f"{pais}: {paisCont[pais]} paises")
   elif(opcion == "7"):
      salir = True
   else:
      print("Opcion no registrada")
      



                 
