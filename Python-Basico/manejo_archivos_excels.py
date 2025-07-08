#¿Que es openpyxl?
#Es una libreria para trabajar con archivos excel

#Crear un archivo de Excel 

from openpyxl import Workbook

workbook = Workbook()
workbook.save("./Python-Basico/relatos.xlsx")

#seleccionarlo y 