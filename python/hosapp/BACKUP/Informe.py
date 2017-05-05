#-*- coding: utf-8 -*-

import codecs
import os
from db.models import session, Orden
from parseo import toWord
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,  Frame,  Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet,  ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch, cm
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
Title = "Orden de pago"

def parrafo(cad, tam=10, ali=TA_CENTER):
    return Paragraph(cad, ParagraphStyle('estilo', fontSize=tam, alignment=ali))

def generar_pdf(orden):
    orden_num = orden.numero
    fecha_ord = str(orden.fecha).split('-')
    nombre_benefi = orden.beneficiario[0].nombre
    nit_benefi = orden.beneficiario[0].nit
    try:
        cerdisp1 = ['', parrafo('%s'%(orden.beneficiario[0].cerdisp[0].numero), 8), parrafo('%s'%(str(orden.beneficiario[0].cerdisp[0].fecha).split('-')[2]), 8), parrafo('%s'%(str(orden.beneficiario[0].cerdisp[0].fecha).split('-')[1]), 8), parrafo('%s'%(str(orden.beneficiario[0].cerdisp[0].fecha).split('-')[0]), 8)]
    except:
        cerdisp1 = ['', '','','','']
    try:
        cerdisp2 = ['', parrafo('%s'%(orden.beneficiario[0].cerdisp[1].numero), 8), parrafo('%s'%(str(orden.beneficiario[0].cerdisp[1].fecha).split('-')[2]), 8), parrafo('%s'%(str(orden.beneficiario[0].cerdisp[1].fecha).split('-')[1]), 8), parrafo('%s'%(str(orden.beneficiario[0].cerdisp[1].fecha).split('-')[0]), 8)]
    except:
        cerdisp2 = ['', '','','','']
    try:
        cerdisp3 = ['', parrafo('%s'%(orden.beneficiario[0].cerdisp[2].numero), 8), parrafo('%s'%(str(orden.beneficiario[0].cerdisp[2].fecha).split('-')[2]), 8), parrafo('%s'%(str(orden.beneficiario[0].cerdisp[2].fecha).split('-')[1]), 8), parrafo('%s'%(str(orden.beneficiario[0].cerdisp[2].fecha).split('-')[0]), 8)]
    except:
        cerdisp3 = ['', '','','','']
    
    try:
        cerreg1 = ['', parrafo('%s'%(orden.beneficiario[0].cerreg[0].numero), 8), parrafo('%s'%(str(orden.beneficiario[0].cerreg[0].fecha).split('-')[2]), 8), parrafo('%s'%(str(orden.beneficiario[0].cerreg[0].fecha).split('-')[1]), 8), parrafo('%s'%(str(orden.beneficiario[0].cerreg[0].fecha).split('-')[0]), 8)]
    except:
        cerreg1 = ['','','','','']
    try:
        cerreg2 = ['', parrafo('%s'%(orden.beneficiario[0].cerreg[1].numero), 8), parrafo('%s'%(str(orden.beneficiario[0].cerreg[1].fecha).split('-')[2]), 8), parrafo('%s'%(str(orden.beneficiario[0].cerreg[1].fecha).split('-')[1]), 8), parrafo('%s'%(str(orden.beneficiario[0].cerreg[1].fecha).split('-')[0]), 8)]
    except:
        cerreg2 = ['','','','','']
    try:
        cerreg3 = ['', parrafo('%s'%(orden.beneficiario[0].cerreg[2].numero), 8), parrafo('%s'%(str(orden.beneficiario[0].cerreg[2].fecha).split('-')[2]), 8), parrafo('%s'%(str(orden.beneficiario[0].cerreg[2].fecha).split('-')[1]), 8), parrafo('%s'%(str(orden.beneficiario[0].cerreg[2].fecha).split('-')[0]), 8)]
    except:
        cerreg3 = ['','','','','']        
    
    f = codecs.open(orden.concepto[0].descripcion, mode='r', encoding='utf-8')
    concepto = f.read()
    f.close()
    bien_servicio = orden.discriminacion[0].bien_servicio
    rubro = orden.rubro
    monto = orden.discriminacion[0].monto
    compromiso = orden.compromiso
    #comprobante = beneficiario.orden[0].comprobante[0].numero
    #comprobante_fecha = str(beneficiario.orden[0].comprobante[0].fecha).split('-')
    #infocond1 = [beneficiario.orden[0].infocond[0].cheque, beneficiario.orden[0].infocond[0].cuenta, beneficiario.orden[0].infocond[0].codigo, beneficiario.orden[0].infocond[0].valor, str(beneficiario.orden[0].infocond[0].fecha).split('-')]
    #try:
    #    infocond2 = [beneficiario.orden[0].infocond[1].cheque, beneficiario.orden[0].infocond[1].cuenta, beneficiario.orden[0].infocond[1].codigo, beneficiario.orden[0].infocond[1].valor, str(beneficiario.orden[0].infocond[1].fecha).split('-')]
    #except:
    #    infocond2 = ['','','','',['','','']]
    
    Paragraph('DIA', ParagraphStyle('estilo', alignment=TA_CENTER, fontSize=8))
    doc = SimpleDocTemplate(u'C:%s\Escritorio\orden.pdf'%(os.environ['HOMEPATH']), pagesize=letter, topMargin=1*cm, leftMargin=1.5*cm, rightMargin=1.8*cm, bottomMargin=1.2*cm, title='Orden De Pago', author='IA')
    style = styles['Normal']
    story = []
    data1 = [[Image("imagenes/logo.jpg"),Paragraph("<strong>REPUBLICA DE COLOMBIA</strong>\
                                <br /><font size=9>Empresa Social Del Estado</font>\
                       <br /><strong>HOSPITAL LOCAL LA CANDELARIA</strong>\
                              <font size=8><br/>Municipio de Rioviejo - Bolivar\
                               <br />Nit: 806.008.153-9\
                               <br /><b>Email: hosriver@hotmail.com - slacandelaria@yahoo.es</b></font>", ParagraphStyle('Tiltulo', alignment=TA_CENTER))]]
    
    t1 = Table(data1, colWidths=["20%", "80%"])
    t1.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
    story.append(t1)
    
    data2 = [[parrafo("<strong>ORDEN DE PAGO</strong>"), parrafo("HL <font color='#ff0000'><b>%s</b></font>"%(orden_num), 14), parrafo("<b>DIA</b>", 8), parrafo("<b>MES</b>", 8), parrafo("<b>AÑO</b>", 8)],
             ['', '', parrafo('%s'%fecha_ord[2], 8), parrafo('%s'%fecha_ord[1], 8), parrafo('%s'%fecha_ord[0], 8)]]
    t2 = Table(data2, style=[('SPAN', (0,0), (0,1)),
                             ('BACKGROUND', (0,0), (-1,0), '#eeeeee'),
                             ('BACKGROUND', (0,1), (1,1), '#eeeeee'),
                             ('SPAN', (1,0), (1,1)),
                             ('GRID',(0,0),(-1,-1), 0.5, '#000000'),
                             ('ALIGN', (0,0), (-1,-1), "CENTER"),
                             ('VALIGN', (0,0), (-1,-1), "MIDDLE")], colWidths=["38%","38%","8%","8%","8%"])
    
    data3 = [[parrafo('<b>BENEFICIARIO:</b>', 9), parrafo("<b>C.C O NIT.</b> &nbsp; %s"%(nit_benefi), 9, TA_LEFT)]]
    t3 = Table(data3, style=[('GRID',(0,0),(-1,-1), 0.5, '#000000'),
                             ('BACKGROUND', (0,0), (0,0), '#eeeeee'),
                             ('ALIGN', (0,0), (-1,-1), "CENTER")], colWidths=["65%", "35%"])
    
    data4 = [[parrafo("%s"%(nombre_benefi), 9, TA_LEFT), parrafo("<b>CERTIFICADO DE DISPONIBILIDAD</b>", 8), "", "", ""],
             ['', parrafo("<b>No.</b>", 8, TA_LEFT), parrafo('<b>DIA</b>', 8), parrafo('<b>MES</b>', 8), parrafo('<b>AÑO</b>', 8)],
             cerdisp1,
             cerdisp2,
             cerdisp3]
    t4 = Table(data4, style=[('GRID',(0,0),(-1,-1), 0.5, '#000000'),
                             ('ALIGN', (0,0), (-1,-1), "CENTER"),
                             ('BACKGROUND', (1,1), (-1,1), "#eeeeee"),
                             ('VALIGN', (0,0), (1,2), "MIDDLE"),
                             ('VALIGN', (2,1), (2,2), "TOP"),
                             ('SPAN', (1,0), (-1,0)),
                             ('SPAN', (0,0), (0,-1))], colWidths=["65%", "11%", "8%", "8%", "8%"])
    data5 = [[parrafo('<b>CONCEPTO</b>', 9), parrafo('<b>CERTIFICADO DE REGISTRO PRESUPUESTAL</b>', 7), '', '', ''],
             [parrafo("%s"%(concepto), 8.5, TA_LEFT), parrafo("<b>No.</b>", 8, TA_LEFT), parrafo('<b>DIA</b>', 8), parrafo('<b>MES</b>', 8), parrafo('<b>AÑO</b>', 8)],
             cerreg1,
             cerreg2,
             cerreg3,
             ['', parrafo('<b>RUBRO</b>', 8), '', parrafo('<b>COMPROMISO</b>', 8), ''],
             ['', parrafo("%s"%(rubro), 8.5), '', parrafo("$ %s"%(compromiso), 8.5), '']]
    t5 = Table(data5, style=[('GRID',(0,0),(-1,-1), 0.5, '#000000'),
                             ('ALIGN', (0,0), (-1,-1), "CENTER"),
                             ('VALIGN', (1,1), (1,2), 'TOP'),
                             ('VALIGN', (0,1), (0,4), 'TOP'),
                             ('BACKGROUND', (0,0), (0,0), '#eeeeee'),
                             ('BACKGROUND', (1,1), (-1,1), "#eeeeee"),
                             ('BACKGROUND', (1,5), (-1,5), "#eeeeee"),
                             ('SPAN', (0,1), (0,-1)),
                             ('SPAN', (1,0), (4,0)),
                             ('SPAN', (1,5), (2,5)),
                             ('SPAN', (3,5), (4,5)),
                             ('SPAN', (1,6), (2,6)),
                             ('SPAN', (3,6), (4,6))], colWidths=["65%", "11%", "8%", "8%", "8%"])
    
    data6 = [[parrafo("<b>EN LETRAS SON:</b><br /><font size=9.5> %s M/L</font>"%(toWord(int(compromiso))), 9, TA_LEFT)]]
    t6 = Table(data6, style=[('GRID',(0,0),(-1,-1), 0.5, '#000000'),
                             ('VALIGN', (0,0), (-1,-1), 'TOP')], colWidths=["100%"])
    
    data7 = [[parrafo("<b>COMPROBANTE No</b><br />", 9, TA_LEFT), parrafo('<b>FECHA</b>', 9), parrafo('<b>DIA</b>', 8), parrafo('<b>MES</b>', 8), parrafo('<b>AÑO</b>', 8)],
             ['', '', '', '', '']]
    t7 = Table(data7, style=[('GRID',(0,0),(-1,-1), 0.5, '#000000'),
                             ('BACKGROUND', (2,0), (-1,0), "#eeeeee"),
                             ('ALIGN', (0,0), (-1,-1), "CENTER"),
                             ('ALIGN', (0,0), (0,1), "LEFT"),
                             ('VALIGN', (0,0), (0,1), "TOP"),
                             ('VALIGN', (1,0), (1,0), "MIDDLE"),
                             ('SPAN', (0,0), (0,1)),
                             ('SPAN', (1,0), (1,1)),], colWidths=["65%", "11%", "8%", "8%", "8%"])
    
    """data8 = [[parrafo('<b>REGISTRO CONTABLE - GIRO</b>', 9)]]
    t8 = Table(data8, style=[('GRID',(0,0),(-1,-1), 0.5, '#000000'),
                             ('BACKGROUND', (0,0), (-1,0), "#eeeeee"),
                             ('ALIGN', (0,0), (-1,-1), "CENTER")], colWidths=["100%"])"""
    
    data9 = [[parrafo('<b>MAYOR</b>', 9), parrafo('<b>SUB</b>', 9), parrafo('<b>SUB</b>', 9), parrafo('<b>AUXILIAR</b>', 9), parrafo('<b>DEBITOS</b>', 9), parrafo('<b>CREDITOS</b>', 9)],
             ['', '', '', '', '', ''],
             ['', '', '', '', '', '']]
    t9 = Table(data9, style=[('GRID',(0,0),(-1,-1), 0.5, '#000000'),
                             ('ALIGN', (0,0), (-1,-1), "CENTER"),
                             ('BACKGROUND', (0,0), (-1,0), "#eeeeee"),
                             ('SPAN', (4,1), (4,2)),
                             ('SPAN', (5,1), (5,2))], colWidths=["12%", "14%", "14%", "20%", "20%", "20%"])
    
    data10 = [[parrafo('<b>INFORMACION CONDENSADA</b>', 9), parrafo('<b>FECHA DE GIRO</b>', 9)]]
    t10 = Table(data10, style=[('GRID',(0,0),(-1,-1), 0.5, '#000000'),
                               ('BACKGROUND', (0,0), (-1,0), "#eeeeee"),
                               ('ALIGN', (0,0), (-1,-1), "CENTER")], colWidths=["76%", "24%"])
    
    data11 = [[parrafo('<b>CHEQUE No.</b>', 9), parrafo('<b>CUENTA No.</b>', 9), parrafo('<b>CODIGO</b>', 9), parrafo('<b>VALOR</b>', 9), parrafo('<b>DIA</b>', 9), parrafo('<b>MES</b>', 9), parrafo('<b>AÑO</b>', 9)],
              ['', '', '', '', '', '', ''],
              ['', '', '', '', '', '', ''],]
    t11 = Table(data11, style=[('GRID',(0,0),(-1,-1), 0.5, '#000000'),
                               ('BACKGROUND', (0,0), (-1,0), "#eeeeee"),
                               ('ALIGN', (0,0), (-1,-1), "CENTER")], colWidths=["22%", "22%", "10%", "22%", "8%", "8%", "8%"])
    
    data12 = [[parrafo('<b>ELABORO</b>', 9), parrafo('<b>CONTROL INTERNO</b>', 8), parrafo('<b>CONTABILIDAD</b>', 9), parrafo('<b>SECCIÓN ADMINISTRATIVA FINANCIERA</b>', 7.5), parrafo('<b>ORDENADOR DEL GASTO</b>', 9)]]
    t12 = Table(data12, style=[('GRID',(0,0),(-1,-1), 0.5, '#000000'),
                               ('ALIGN', (0,0), (-1,-1), "CENTER"),
                               ('VALIGN', (0,0), (-1,0), "TOP")], colWidths=["14%", "18%", "18%", "25%", "25%"], rowHeights=60)
    texto="<b>Costo del bien o servicio</b>\n\
           <br /><b>Iva</b>\n\
           <br /><b>Ret. Iva</b>\n\
           <br /><b>Imp. Municipales</b>\n\
           <br /><b>Otros</b>( %s )\n\
           <br/><b>Ret. Fuente</b>\n\
           <br /><b>Neto a Pagar</b>"%(orden.discriminacion[0].otros_concepto)
    data13 = [[parrafo(texto, 8.5, TA_LEFT), parrafo(get_discriminacion(bien_servicio, monto, orden.discriminacion[0], orden.discriminacion[0].pago_final), 8.5, TA_LEFT), parrafo('<b>RECIBI:</b>', 9, TA_LEFT)],
              ['', '', parrafo('<b>C.C O NIT</b>', 9, TA_LEFT)]]
    t13 = Table(data13, style=[('GRID',(0,0),(-1,-1), 0.5, '#000000'),
                               ('ALIGN', (0,0), (-1,-1), "CENTER"),
                               ('VALIGN', (0,0), (-1,-1), "TOP"),
                               ('SPAN', (0,0), (0,-1)),
                               ('SPAN', (1,0), (1,-1))], colWidths=["35%", "35%", "30%"], rowHeights=[80,20])
    
    story.append(t2)
    story.append(t3)
    story.append(t4)
    story.append(t5)
    story.append(t6)
    story.append(t7)
    #story.append(t8)
    story.append(t9)
    story.append(t10)
    story.append(t11)
    story.append(t12)
    story.append(t13)
    doc.build(story)

def get_discriminacion(bien_servicio, monto, lista, pago_final):
    if pago_final:
        total = int(monto)
    else:
        total = int(bien_servicio)
    
    parrafo = "$ %s \n"%(total)
        
    if str(lista.iva).__len__()>1:
        iva = lista.iva
        #print iva
        parrafo += "<br />$ %s \n"%(iva)
    else:
        iva = 0
        parrafo += "<br />\n"
        
    if lista.ret_iva:
        ret_iva = ((iva*50)/100)
        parrafo += "<br />$ %s \n"%(ret_iva)
    else:
        ret_iva = 0
        parrafo += "<br/>"
        
    if lista.imp_municipales:
        imp_munic = ((total*4)/100)
        parrafo += "<br />$ %s \n"%(imp_munic)
    else:
        imp_munic = 0
        parrafo += "<br />\n"
        
    #if lista.est_pdf:
     #   est_pdf = ((total*1)/100)
     #   parrafo += "<br /><b>Estampilla P.D.F ---------------</b> $ %s \n"%(est_pdf)
    #else:
     #   est_pdf = 0
     #   parrafo += "<br /><b>Estampilla P.D.F </b>"
        
    #if lista.com_recaudo:
    #    com_rec = ((total*0.5)/100)
    #    parrafo += "<br /><b>Comisión por recaudo ---------------</b> $ %s \n"%(com_rec)
    #else:
    #   com_rec = 0
    #    parrafo += "<br /><b>Comisión por recaudo </b>"
    
    if str(lista.otros).__len__()>1:
        parrafo+='<br />\n'
        parrafo+='$ '
        listadesc = str(lista.otros).split('+')
        otros = 0
        for descuento in listadesc:
            otros += int(descuento)
            if listadesc[-1]==descuento:
                parrafo += "%s"%(descuento)
            else:
                parrafo += "%s+"%(descuento)
    else:
        otros = 0
        parrafo += "<br />\n"
        
    if str(lista.ret_fuente).__len__()>0:
        ret_fuen = int((total*float(lista.ret_fuente))/100)
        parrafo += "<br />$ %s\n"%(ret_fuen)
    else:
        ret_fuen = 0
        parrafo += "<br />\n"
        
    total += iva
    total -= ret_iva
    total -= imp_munic
    #grantotal -= est_pdf
    #grantotal -= com_rec
    total -= otros
    total -= int(ret_fuen)
    parrafo +=   "<br />$ %s"%(int(total))
    
    return parrafo
    

def comprobacion(orden):
    if int(orden.numero) < int(session.query(Orden).first().numero) or int(orden.numero) > int(session.query(Orden).all()[-1].numero+1):
        print u"El número de la ordén está por fuera del rango permitido."
        return False
    return True