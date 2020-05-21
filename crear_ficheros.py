import os

# Creo variable con la ruta en la que se van a guardar los nuevos ficheros de configuracion para cada servidor
global_path = "C:/Users/Carmen/Desktop/PE/crear_ficheros/ficheros_config_creados"

# elimino todos lo archivos de la carpeta donde se han creado los archivos de configuracion para actualizarlos a la lista
files_borrar = os.listdir(global_path)

for name in files_borrar:
    print(name)
    os.remove(global_path+"/"+name) 

# Abro el fichero que contiene el nombre del servidor, el path donde se encuentran las beans a procesar y la template que va a usar
fileName = "servers.txt"
fileObjt = open(fileName)

# Recorro cada linea del fichero, que corresponde a un servidor distinto
for line in fileObjt:
    
    currentline = line.split(",")

    # Creo 4 variables, una para el nombre del fichero, otra para el server,otra para el path y otra para la plantilla a usar
    server = currentline[0].strip()
    path = currentline[1].strip()
    template = currentline[2].strip()
    nombre_fichero = 'logstash_'+server+'.config'
    index_logstash = "prueba_script"

    # Abro el fichero template declarado en servers.txt para sustituir las variables por las que corresponden
    fin = open('templates/'+template, "rt")
    # Creo el fichero que va a ser el de configuracion
    fout = open(global_path+"/"+nombre_fichero, "wt")

    # por cada linea del fihcero template sustituye el valor correspondiente
    for linea in fin:
        fout.write(linea.replace('${path}', path).replace('${server}', server).replace('${index}', index_logstash))

    fout.close()
    fin.close()
    
   
