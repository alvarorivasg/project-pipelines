import pandas as pd
import argparse
from src.dframe import filtro
from src.dframe import asignaTemplo
from src.dframe import columnaDivina
from src.dframe import limpiaFinal
from src.pdf import crearPDF
from src.mail import checkMail
from src.mail import sendEmail
def recibeargumentos():
    parser = argparse.ArgumentParser(description="Bienaventurados aquellos que confían en el Señor para salvar sus vidas. Si vas a coger la bici, procura rezar antes. Aquí encontrarás el destino de aquellos que desoyeron mi divino consejo.")
    parser.add_argument('--mes', help='Mes sobre el que mostraremos los datos', default= 'ENERO',type=str, choices=['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'])
    parser.add_argument('--distrito', help='Distrito de Madrid que analizaremos.\nPor favor, utilicen comillas si el distrito elegido consta de dos o más palabras' , default='CIUDAD LINEAL', type=str, choices=['CARABANCHEL', 'RETIRO', 'VICALVARO', 'VILLAVERDE', 'CENTRO', 'CIUDAD LINEAL', 'LATINA', 'CHAMARTIN', 'MONCLOA-ARAVACA', 'SALAMANCA', 'PUENTE DE VALLECAS', 'VILLA DE VALLECAS', 'MORATALAZ', 'HORTALEZA', 'ARGANZUELA', 'USERA', 'FUENCARRAL-EL PARDO', 'TETUAN', 'BARAJAS', 'CHAMBERI', 'SAN BLAS'])
    parser.add_argument("--email", help="Dios usará esta vía para comunicarse con usted")
    args = parser.parse_args()
    return args


def main():
    #recibo argumentos
    argumentos=recibeargumentos()
    #configuro mi dataframe (filtro+creación de columna divina)
    dataframe=filtro(argumentos.mes,argumentos.distrito)
    dataframe=columnaDivina(dataframe)
    dataframe=limpiaFinal(dataframe)
    #saco el dataframe como output
    crearPDF(dataframe)
    if dataframe.empty:
        print("Bendito sea el Señor. No existen accidentes que se ajusten a su búsqueda")
    if argumentos.email != None:
        mail = checkMail(argumentos.email)
        sendEmail(mail,["./output/vivacristorey.pdf", "vivacristorey.pdf"])
    else: print("Busque su PDF en la carpeta output")
if __name__=='__main__':
    main()