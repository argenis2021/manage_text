import csv, operator
csvarchivo = open('ventas.csv')  # Abrir archivo csv
entrada = csv.reader(csvarchivo)  # Leer todos los registros
reg = next(entrada)  # Leer registro (lista)
print(reg)  # Mostrar registro
Fecha, CodCli, Cliente, Telefono, Cantidad, Descripción, Precio, Locación, Semana = next(entrada)  # Leer campos
print(Fecha, CodCli, Cliente, Telefono, Cantidad, Descripción, Precio, Locación, Semana)  # Mostrar campos
#del nombre, provincia, consumo, entrada  # Borrar objetos
csvarchivo.close()  # Cerrar archivo
#del csvarchivo  # Borrar objeto