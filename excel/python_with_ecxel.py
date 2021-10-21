from openpyxl import Workbook
#from openpyxl.workbook.workbook import Workbook
arquiivo = Workbook()
planilha = arquiivo.worksheets[0]
planilha['A1'] = "VOU PAGAR SÓ DIA 13"
planilha['B2'] = "sem choro"

arquiivo.save("C:\Users\Up Agency 2\OneDrive\Documentos\drive\meuarquivo.xlsx")



#C:\Users\Up Agency 2\OneDrive\Área de Trabalho\py com excel