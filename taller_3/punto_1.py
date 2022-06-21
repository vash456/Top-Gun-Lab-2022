"""
Ace quiere  ser  voluntario  para  viajar  a  K-Pax, para  ello  
la Agencia Espacial   Canadiense   requiere   que   llene un 
formulario que ayude a obtener más información de él y su familia. 
Tu debes ayudar a Ace creando un programa para completar   la   
información solicitada sin sobrescribir el archivo. Ten presente 
que los datos con  *  son  los más importantes, si uno de esos 
campos no se llena, no podrá ser admitido, en caso de que el dato 
solicitado no sea importante, el programa deberá poner “unknown”.
"""

# elementos del formulario
family = ["Mother", "Father", "Brother", "Sister"]

# abrir y leer archivo
file = open('required_data.txt', 'r+')
lines = file.readlines()

# ciclo principal para mostrar todo el formulario
for i,line in enumerate(lines):
    # buscar las lineas que tienen el caracter ':'
    search_result = line.find(':')
    if search_result != -1:
        # se busca los campos con asterisco para llenar llenar con data
        if line.find('*') != -1:
            data_ok = True
            # se valida hasta que se ingrese un valor en el campo
            while data_ok:
                data = input(line[:-1] + " ")
                if data != '':
                    data_ok = False
            lines[i] = line[:-1] + " " + data + "\n"
        else:
            # para que no llene de data las lineas en el formulario que tengan las palabras de la lista
            search_family = False
            for fam in family:
                if fam in line:
                    search_family = True
            if search_family:
                print(line[:-1])
            else:
                # se llena con un unknown los campos no obligatorios
                lines[i] = line[:-1] + " unknown\n"
                print(lines[i][:-1])
    else:
        print(line[:-1])
        
file.close()

# se crea otro archivo para guardar el formulario modificado con la data
file = open('required_data2.txt', 'w')

file.writelines(lines)

file.close()

