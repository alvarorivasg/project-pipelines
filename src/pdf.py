import pandas as pd
from fpdf import FPDF

def crearPDF(dataframe):
    pdf = FPDF(format = 'A4', unit = 'cm')
    pdf.add_page('L')
    epw = pdf.w - 2*pdf.l_margin
    col_width = epw/4
    th = 1
    #title
    pdf.set_font('Times','B',14.0) 
    pdf.cell(epw, 0.0, 'Alabado sea el Señor', align='C')
    pdf.set_font('Times','',10.0) 
    pdf.ln(1)
    #creating the columns
    pdf.cell(col_width, th-0.5, 'FECHA', align='C', border = 1)
    pdf.cell(col_width, th-0.5, 'LUGAR DEL ACCIDENTE', align='C', border = 1)
    pdf.cell(col_width, th-0.5, 'NÚMERO DE VÍCTIMAS', align='C', border = 1)
    pdf.cell(col_width, th-0.5, 'DIOS OS ESPERABA EN:', align='C', border = 1)
    #filling the table
    pdf.ln(th+1)
    pdf.set_font('Arial', '', 7)
    for i in range(len(dataframe['FECHA'])):     
        fecha= dataframe['FECHA'].iloc[i]
        lugar = dataframe['LUGAR DEL ACCIDENTE'].iloc[i]
        victimas = dataframe['NUM VICTIMAS'].iloc[i]
        iglesia = dataframe['DIOS OS ESPERABA EN:'].iloc[i]
        pdf.cell(col_width, th+1, '%s' % (fecha), align='C', border = 1)
        pdf.cell(col_width, th+1, '%s' % (lugar), align='C', border = 1)
        pdf.cell(col_width, th+1, '%s' % (victimas), align='C', border = 1)
        pdf.cell(col_width, th+1, '%s' % (iglesia), align='C', border = 1)
        pdf.ln(th+1)


 
    
    return pdf.output('./output/vivacristorey.pdf', 'F')

