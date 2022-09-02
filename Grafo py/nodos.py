import json

graph={}
cargar= []
usuario = input("Ingrese su nombre:\n")
print()
n = input("Digite la cantidad de nodos:\n")
print("--------------------------------------------------")


def Fill(n):

  Menu = True
  while Menu == True:
    print("1.Inicio del programa\n2.Consultar las rutas \n3.Salir del programa\n")
    opc = int(input("Respuesta: "))
    print("------------------------------------------------------")
    if opc == 1:
    
        nodo_conexiones=[]
        graph.clear()
        print("Bienvenido(a):" + usuario)
        print()
        it_is = False 
        
        while it_is == False:  
            try:
                int(n)
                it_is = True
            except ValueError: 
                it_is = False
                print("Oh, al parecer no ingresaste el número.\n")
                n = input("Digite la cantidad de nodos\n") 
            
        n = int(n) 
    
        for i in range(n): 
            it_is = False 
    
            while it_is == False: 
                print("--------Has iniciado el programa--------")
                valor=input("Nodo "+str(i+1)+"\nDigite el nombre del nodo en mayuscula: "+str("")).upper()
                print()
                if valor.isnumeric(): 
                    print("Agrega una letra por favor")
                elif len(valor) <= 0: 
                    print("")
                    print("-----------------------------")
                   
                else:
                    nodo = valor 
                    it_is = True
    
            state = True
            while state == True:
                print(nodo+str(nodo_conexiones)) 
                rpta=input("Selecciona una opción:\n1.Agregar conexion de nodo\n2.No agregar conexion de nodo\n3.Eliminar camino de nodo\n\nOpción:") #vALIDAR
                print()
                if rpta.isalpha():
                    print("Elige la opción con un número")
                else:
                    rpta = int(rpta)
                    if rpta == 1: 
                        print(nodo+str(nodo_conexiones))
                        print("¿Qué camino desea conectar con el nodo "+nodo+"?\n\nCamino:")
                        nodo_unir=input()
                        nodo_conexiones.append(nodo_unir)
                        
                    if rpta == 2: 
                        state = False
                    if rpta == 3: 
                        if not nodo_conexiones:
                            
                            print("\nLa lista está vacía\n")
                        else:
                            quitar = input("Digita el camino que deseas eliminar: \n").upper()
                            nodo_conexiones.remove(quitar)
                            print("Se ha eliminado el nodo "+quitar+"\n")                                
            graph.update({nodo: set(nodo_conexiones)})
            nodo_conexiones.clear()
            print(graph)
            print("--------------------------------------------------------")
        vi = input("Digite el nodo inicial del recorrido:").upper()
        vf = input("Digite el nodo final del recorrido:").upper()
        print("-----------------------------------------------------")
        busq = list(dfs_paths(graph, vi, vf))
        data_json(usuario, vi, vf, n, busq)
      
    if opc == 2:
      print("--------------Consulta de rutas-------------")
      state_2 = True
      while state_2 == True:
        print("Elige una opción \n1.Mostrar todos los registros del JSON\n2.Regresar al menu principal\n")
        opcionsubmenu = int(input("Respuesta: "))
        if opcionsubmenu == 1:
            ShowAllJson()    
            print("----------------------------------------") 
            break
        if opcionsubmenu == 2:
          print("Regresar al menú principal")
          break

    if opc == 3:
      print("Saliste del programa")
      exit()
      
def ShowAllJson():
  if Verify() == True:
    with open('prueba.json') as archivo:
      jsoninicio = json.load(archivo)
    jsonfinal = json.dumps(jsoninicio, indent = 3)
    return print(str(jsonfinal)) 
    
def dfs_paths(graph, start, goal):

    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]
        for next in graph[node] - set(path):

            if next == goal:
                yield path + [next]
            else:
                stack.append(path + [next])


def Verify():
    try:
        with open ('prueba.json') as archivo:
            return True     
    except FileNotFoundError as e:
        return False

def Data( usuario, n, vi, vf,  busq):

    dictionary = {'Usuario': usuario, 
    'Cantidad de nodos': n,
    'Valor inicial': vi, 
    'Valor final': vf, 
    'Busqueda': busq}
    return dictionary

def data_json( usuario,n, vi, vf, busq):

    if Verify() == True:
        with open ("prueba.json") as archivo:
            datos = json.load(archivo)
        datos.append(Data(usuario,n, vi, vf,busq))

        with open("prueba.json", 'w') as archivo_nuevo:
            json.dump(datos, archivo_nuevo, indent = 3)
            print("Los datos fueron guardados en "+archivo_nuevo.name)
            print("------------------------------------------------")
    else:
        with open("prueba.json", 'w') as archivo_nuevo:
            cargar.append(Data(usuario, n, vi, vf, busq))
            json.dump(cargar, archivo_nuevo, indent = 3)     
            print("Se ha creado el historial en el archivo " +archivo_nuevo.name)


Fill(n)