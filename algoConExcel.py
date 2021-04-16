import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

palabra = input("Ingrese lo que desea escribir en el documento: ")

worksheet.write('A1', 'Hello world')
worksheet.write('B2', palabra)
workbook.close() 