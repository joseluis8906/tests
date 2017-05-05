#-*- coding: utf-8 -*-
import wx
import wx.grid
from encodings import utf_8
import datetime
import codecs
from Informe import generar_pdf, comprobacion
from db.models import session, Beneficiario, Orden, Cerdisp, Cerreg, Concepto, Comprobante, Infocond, Discriminacion

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_contenedor = wx.Panel(self, -1)
        self.imagen_encabezado = wx.StaticBitmap(self.panel_contenedor, -1, wx.Bitmap(u"imagenes/encabezado.png", wx.BITMAP_TYPE_ANY))
        self.staticbox_fila3 = wx.StaticBox(self.panel_contenedor, -1, 'Beneficiario', (5,110), (580,185))
        staticbox_fila4 = wx.StaticBox(self.panel_contenedor, -1, 'Concepto', (5,300), (580,100))
        staticbox_fila6 = wx.StaticBox(self.panel_contenedor, -1, u'Información Condensada', (5,435), (580,100))
        staticbox_fila11 = wx.StaticBox(self.panel_contenedor, -1, u'Descuentos y adiciones', (5,540), (580,85))
        self.label_orden = wx.StaticText(self.panel_contenedor, -1, "Orden",)
        self.text_orden = wx.TextCtrl(self.panel_contenedor, -1, "")
        self.label_fecha = wx.StaticText(self.panel_contenedor, -1, "Fecha")
        self.date_fecha = wx.DatePickerCtrl(self.panel_contenedor, -1)
        self.label_compromiso = wx.StaticText(self.panel_contenedor, -1, "Compromiso $")
        self.text_compromiso = wx.TextCtrl(self.panel_contenedor, -1, "")
        self.label_nit = wx.StaticText(self.panel_contenedor, -1, "Nit o C.C")
        self.text_nit = wx.TextCtrl(self.panel_contenedor, -1, "")
        self.label_nombre = wx.StaticText(self.panel_contenedor, -1, "Nombre")
        self.text_nombre = wx.TextCtrl(self.panel_contenedor, -1, "")
        self.label_cerdisp = wx.StaticText(self.panel_contenedor, -1, "Certificado De Disponibilidad")
        self.label_cerreg = wx.StaticText(self.panel_contenedor, -1, "Certificado De Registro Presupuestal")
        self.grid_cerdisp = wx.grid.Grid(self.panel_contenedor, -1, size=(-1, -1))
        self.grid_cerreg = wx.grid.Grid(self.panel_contenedor, -1, size=(-1, -1))
        self.text_concepto = wx.TextCtrl(self.panel_contenedor, -1, "", style=wx.TE_MULTILINE)
        self.label_comprobante = wx.StaticText(self.panel_contenedor, -1, "Comprobante")
        self.text_comprobante = wx.TextCtrl(self.panel_contenedor, -1, "")
        self.label_fechacomp = wx.StaticText(self.panel_contenedor, -1, "Fecha")
        self.date_fechacomp = wx.DatePickerCtrl(self.panel_contenedor, -1)
        self.label_rubro = wx.StaticText(self.panel_contenedor, -1, "Rubro")
        self.text_rubro = wx.TextCtrl(self.panel_contenedor, -1, "")
        self.grid_infocond = wx.grid.Grid(self.panel_contenedor, -1, size=(-1, -1))
        self.label_costo_bien = wx.StaticText(self.panel_contenedor, -1, "Bien o Servicio $")
        self.text_costo_bien = wx.TextCtrl(self.panel_contenedor, -1, "")
        self.label_iva = wx.StaticText(self.panel_contenedor, -1, "Iva $")
        self.text_iva = wx.TextCtrl(self.panel_contenedor, -1, "")
        self.check_ret_iva = wx.CheckBox(self.panel_contenedor, -1, "Ret. Iva")
        self.check_imp_munic = wx.CheckBox(self.panel_contenedor, -1, "Imp. Munic")
        self.label_retfuente = wx.StaticText(self.panel_contenedor, -1, "Ret. Fuente %")
        self.text_retefuente = wx.TextCtrl(self.panel_contenedor, -1, "")
        #self.check_est_pdf = wx.CheckBox(self.panel_contenedor, -1, "Est. P.D.F")
        #self.check_com_rec = wx.CheckBox(self.panel_contenedor, -1, "Com. por recaudo")
        self.label_otros_concepto = wx.StaticText(self.panel_contenedor, -1, "Concep. Otros")
        self.text_otros_concepto = wx.TextCtrl(self.panel_contenedor, -1, "")
        self.label_otros_valor = wx.StaticText(self.panel_contenedor, -1, "Val. Otros $")
        self.text_otros = wx.TextCtrl(self.panel_contenedor, -1, "")
        self.label_monto = wx.StaticText(self.panel_contenedor, -1, "Monto Total $")
        self.text_monto = wx.TextCtrl(self.panel_contenedor, -1, "")
        self.check_pago_final = wx.CheckBox(self.panel_contenedor, -1, "Pago Final")
        #self.check_solo_generar = wx.CheckBox(self.panel_contenedor, -1, "Solo Generar")
        self.button_generar = wx.Button(self.panel_contenedor, -1, "Generar")
        
        self.Bind(wx.EVT_BUTTON, self.guardar_orden, self.button_generar)
        wx.EVT_KILL_FOCUS(self.text_orden, self.sobre_escribir)
        
        
        self.__set_properties()
        self.__do_layout()
        
    def __set_properties(self):
        self.SetTitle("Orden De Pago")
        self.SetSize((600, 730))
        self.text_compromiso.SetMinSize((100,-1))
        self.text_nit.SetMinSize((200,-1))
        self.text_nombre.SetMinSize((450,-1))
        self.malla_cerdisp()
        self.malla_cerreg()
        self.text_concepto.SetMinSize((570,76))
        self.text_comprobante.SetMinSize((150,-1))
        self.malla_infocond()
        self.ini_num_orden()
        self.text_retefuente.SetMinSize((40,-1))

    def __do_layout(self):
        sizer_panel = wx.BoxSizer(wx.VERTICAL)
        self.staticbox_fila3.SetExtraStyle(wx.LEFT)
        sizer_panel.Add(self.fila1(),0,wx.ALIGN_CENTER_HORIZONTAL|wx.TOP,5)
        sizer_panel.Add(self.fila2(),0,wx.TOP|wx.ALIGN_CENTER_HORIZONTAL,10)
        sizer_panel.Add(self.fila3(),0,wx.TOP, 20)
        sizer_panel.Add(self.fila4(),0,wx.TOP,5)
        sizer_panel.Add(self.fila5(),0,wx.TOP,7)
        sizer_panel.Add(self.fila6(),0,wx.TOP,5)
        sizer_panel.Add(self.fila7(),0,wx.TOP,30)
        sizer_panel.Add(self.fila8(),0,wx.TOP,15)
        sizer_panel.Add(self.fila9(),0,wx.TOP,25)
        sizer_panel.Add(self.fila10(),0,wx.TOP,30)
        sizer_panel.Add(self.fila11(),0,wx.TOP,15)
        sizer_panel.Add(self.fila12(),0,wx.TOP|wx.ALIGN_RIGHT,35)
        self.panel_contenedor.SetSizer(sizer_panel)
        self.panel_contenedor.Layout()
        
    def malla_cerdisp(self):
        self.grid_cerdisp.CreateGrid(3, 4)
        self.grid_cerdisp.SetLabelBackgroundColour(wx.Colour(215, 238, 244))
        self.grid_cerdisp.SetRowLabelSize(30)
        self.grid_cerdisp.SetColLabelSize(30)
        self.grid_cerdisp.SetColLabelValue(0, "Numero")
        self.grid_cerdisp.SetColLabelValue(1, u"Año")
        self.grid_cerdisp.SetColSize(1, 50)
        self.grid_cerdisp.SetColLabelValue(2, "Mes")
        self.grid_cerdisp.SetColSize(2, 40)
        self.grid_cerdisp.SetColLabelValue(3, u"Día")
        self.grid_cerdisp.SetColSize(3, 40)
        
    def malla_cerreg(self):
        self.grid_cerreg.CreateGrid(3, 4)
        self.grid_cerreg.SetLabelBackgroundColour(wx.Colour(215, 238, 244))
        self.grid_cerreg.SetRowLabelSize(30)
        self.grid_cerreg.SetColLabelSize(30)
        self.grid_cerreg.SetColLabelValue(0, "Numero")
        self.grid_cerreg.SetColLabelValue(1, u"Año")
        self.grid_cerreg.SetColSize(1, 50)
        self.grid_cerreg.SetColLabelValue(2, "Mes")
        self.grid_cerreg.SetColSize(2, 40)
        self.grid_cerreg.SetColLabelValue(3, u"Día")
        self.grid_cerreg.SetColSize(3, 40)
    
    def malla_infocond(self):
        self.grid_infocond.CreateGrid(2, 7)
        self.grid_infocond.SetLabelBackgroundColour(wx.Colour(215, 238, 244))
        self.grid_infocond.SetRowLabelSize(30)
        self.grid_infocond.SetColLabelSize(30)
        self.grid_infocond.SetColLabelValue(0, "Cheque No.")
        self.grid_infocond.SetColLabelValue(1, "Cuenta No.")
        self.grid_infocond.SetColLabelValue(2, u"Código")
        self.grid_infocond.SetColLabelValue(3, "Valor")
        self.grid_infocond.SetColLabelValue(4, u"Año")
        self.grid_infocond.SetColLabelValue(5, "Mes")
        self.grid_infocond.SetColLabelValue(6, u"Día")
        self.grid_infocond.SetColSize(0, 100)
        self.grid_infocond.SetColSize(1, 100)
        self.grid_infocond.SetColSize(2, 100)
        self.grid_infocond.SetColSize(3, 100)
        self.grid_infocond.SetColSize(4, 50)
        self.grid_infocond.SetColSize(5, 40)
        self.grid_infocond.SetColSize(6, 40)
    
    def fila1(self):
        sizer_fila1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_fila1.Add(self.imagen_encabezado,1,wx.EXPAND|wx.LEFT,10)
        return sizer_fila1
    
    def fila2(self):
        sizer_fila2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_fila2.Add(self.label_orden,0,wx.ALIGN_CENTER_VERTICAL,0)
        sizer_fila2.Add(self.text_orden,0,wx.LEFT,5)
        sizer_fila2.Add(self.label_fecha,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,15)
        sizer_fila2.Add(self.date_fecha,0,wx.LEFT,5)
        sizer_fila2.Add(self.label_compromiso,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,15)
        sizer_fila2.Add(self.text_compromiso,0,wx.LEFT,5)
        return sizer_fila2
    
    def fila3(self):
        sizer_fila3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_fila3.Add(self.label_nit,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,30)
        sizer_fila3.Add(self.text_nit,0,wx.LEFT,5)
        return sizer_fila3
    
    def fila4(self):
        sizer_fila4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_fila4.Add(self.label_nombre,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,30)
        sizer_fila4.Add(self.text_nombre,0,wx.LEFT,5)
        return sizer_fila4
    
    def fila5(self):
        sizer_fila5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_fila5.Add(self.label_cerdisp,0,wx.LEFT,70)
        sizer_fila5.Add(self.label_cerreg,0,wx.LEFT,150)
        return sizer_fila5
    
    def fila6(self):
        sizer_fila6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_fila6.Add(self.grid_cerdisp,0,wx.EXPAND|wx.LEFT,30)
        sizer_fila6.Add(self.grid_cerreg,0,wx.EXPAND|wx.LEFT,50)
        return sizer_fila6
        
    
    def fila7(self):
        sizer_fila7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_fila7.Add(self.text_concepto,0,wx.LEFT,10)
        return sizer_fila7
    
    def fila8(self):
        sizer_fila8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_fila8.Add(self.label_comprobante,0,wx.ALIGN_CENTER_VERTICAL|wx.LEFT,30)
        sizer_fila8.Add(self.text_comprobante,0,wx.LEFT,5)
        sizer_fila8.Add(self.label_fechacomp,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,25)
        sizer_fila8.Add(self.date_fechacomp,0,wx.LEFT,5)
        sizer_fila8.Add(self.label_rubro,0,wx.ALIGN_CENTER_VERTICAL|wx.LEFT,25)
        sizer_fila8.Add(self.text_rubro,0,wx.LEFT,5)
        return sizer_fila8
    
    def fila9(self):
        sizer_fila9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_fila9.Add(self.grid_infocond,0,wx.LEFT,12)
        return sizer_fila9
    
    def fila10(self):
        sizer_fila10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_fila10.Add(self.label_costo_bien,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,30)
        sizer_fila10.Add(self.text_costo_bien,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,5)
        sizer_fila10.Add(self.label_iva,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,15)
        sizer_fila10.Add(self.text_iva,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,5)
        sizer_fila10.Add(self.check_ret_iva,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,15)
        sizer_fila10.Add(self.check_imp_munic,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,15)
        #sizer_fila10.Add(self.check_est_pdf,0,wx.LEFT,15)
        #sizer_fila10.Add(self.check_com_rec,0,wx.LEFT,15)
        return sizer_fila10
    
    def fila11(self):
        sizer_fila11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_fila11.Add(self.label_retfuente,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,30)
        sizer_fila11.Add(self.text_retefuente,0,wx.LEFT,5)
        sizer_fila11.Add(self.label_otros_concepto,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,15)
        sizer_fila11.Add(self.text_otros_concepto,0,wx.LEFT,5)
        sizer_fila11.Add(self.label_otros_valor,0,wx.LEFT|wx.ALIGN_CENTER_VERTICAL,15)
        sizer_fila11.Add(self.text_otros,0,wx.LEFT,5)
        return sizer_fila11
    
    def fila12(self):
        sizer_fila12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_fila12.Add(self.label_monto,0,wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_fila12.Add(self.text_monto,0,wx.RIGHT, 10)
        sizer_fila12.Add(self.check_pago_final,0,wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 220)
        sizer_fila12.Add(self.button_generar,0,wx.RIGHT,15)
        return sizer_fila12


    def guardar_orden(self, event):
        #Extraer el valor del campo fecha del frame y crear un nuevo objeto tipo date con los datos obtenidos
        orden_fecha = datetime.date(int('20'+str(self.date_fecha.GetValue()).split(' ')[0].split('/')[2]), int(str(self.date_fecha.GetValue()).split(' ')[0].split('/')[0]), int(str(self.date_fecha.GetValue()).split(' ')[0].split('/')[1]))
        #Generación del diccionario orden con los datos brindados por el frame
        try:
            orden_dic = {'numero': int(self.text_orden.GetValue()),
                         'fecha': orden_fecha,
                         'compromiso': int(self.text_compromiso.GetValue()),
                         'rubro': str(self.text_rubro.GetValue())}
        except:
            print u"Ocurrió un error mientras se intentaba generar la órden."
            return
        
        try:
            orden = session.query(Orden).filter(Orden.numero==int(self.text_orden.GetValue()))[0]
            self.limpiar_orden(orden)
            #print u'La orden es antigua'
        except:
            orden = Orden(orden_dic['numero'], orden_dic['fecha'], orden_dic['compromiso'], orden_dic['rubro'])
            #print u'La orden no es antigua'
        
        #Generación del diccionario beneficiario con los datos brindados por el frame
        try:
            beneficiario_dic = {'nombre': unicode(self.text_nombre.GetValue()),
                                'nit': unicode(self.text_nit.GetValue())}
        except:
            print u"Ocurrió un error mientras se intentaba generar el beneficiario."
            return

        ### Certificados de disponibilidad ###
        #Si es posible, crear el primer diccionario tipo cerdisp con los datos brindados por el frame
        if unicode(self.grid_cerdisp.GetCellValue(0,0)).__len__()>0 :
            try:
                cerdisp1_fecha = datetime.date(int(self.grid_cerdisp.GetCellValue(0,1)), int(self.grid_cerdisp.GetCellValue(0,2)), int(self.grid_cerdisp.GetCellValue(0,3)))
            except:
                print 'La fecha del certificado de disponibilidad 1 es incorrecta'
                return
            cerdisp1_dic = {'numero': unicode(self.grid_cerdisp.GetCellValue(0,0)),
                            'fecha':cerdisp1_fecha}
            
        
        #Si es posible, crear el segundo diccionario tipo cerdisp con los datos brindados por el frame
        if unicode(self.grid_cerdisp.GetCellValue(1,0)).__len__()>0 :
            try:
                cerdisp2_fecha = datetime.date(int(self.grid_cerdisp.GetCellValue(1,1)), int(self.grid_cerdisp.GetCellValue(1,2)), int(self.grid_cerdisp.GetCellValue(1,3)))
            except:
                print 'La fecha del certificado de disponibilidad 2 es incorrecta'
                return
            cerdisp2_dic = {'numero': unicode(self.grid_cerdisp.GetCellValue(1,0)),
                        'fecha':cerdisp2_fecha}
        
        #Si es posible, crear el tercer diccionario tipo cerdisp con los datos brindados por el frame
        if unicode(self.grid_cerdisp.GetCellValue(2,0)).__len__()>0 :
            try:
                cerdisp3_fecha = datetime.date(int(self.grid_cerdisp.GetCellValue(2,1)), int(self.grid_cerdisp.GetCellValue(2,2)), int(self.grid_cerdisp.GetCellValue(2,3)))
            except:
                print 'La fecha del certificado de disponibilidad 3 es incorrecta'
                return
            cerdisp3_dic = {'numero': unicode(self.grid_cerdisp.GetCellValue(2,0)),
                        'fecha':cerdisp3_fecha}
        
        #### certificados de registro presupuestal ####
        #Si es posible, crear el primer diccionario tipo cerreg con los datos brindados por el frame
        if unicode(self.grid_cerreg.GetCellValue(0,0)).__len__()>0 :
            try:
                cerreg1_fecha = datetime.date(int(self.grid_cerreg.GetCellValue(0,1)), int(self.grid_cerreg.GetCellValue(0,2)), int(self.grid_cerreg.GetCellValue(0,3)))
            except:
                print 'La fecha del certificado de registo presupuestal 1 es incorrecta'
                return
            cerreg1_dic = {'numero': unicode(self.grid_cerreg.GetCellValue(0,0)),
                        'fecha':cerreg1_fecha}
    
        #Si es posible, crear el segundo diccionario tipo cerreg con los datos brindados por el frame
        if unicode(self.grid_cerreg.GetCellValue(1,0)).__len__()>0 :
            try:
                cerreg2_fecha = datetime.date(int(self.grid_cerreg.GetCellValue(1,1)), int(self.grid_cerreg.GetCellValue(1,2)), int(self.grid_cerreg.GetCellValue(1,3)))
            except:
                print 'La fecha del certificado de registo presupuestal 2 es incorrecta'
                return
            cerreg2_dic = {'numero': unicode(self.grid_cerreg.GetCellValue(1,0)),
                        'fecha':cerreg2_fecha}
            
        #Si es posible, crear el tercer diccionario tipo cerreg con los datos brindados por el frame
        if unicode(self.grid_cerreg.GetCellValue(2,0)).__len__()>0 :
            try:
                cerreg3_fecha = datetime.date(int(self.grid_cerreg.GetCellValue(2,1)), int(self.grid_cerreg.GetCellValue(2,2)), int(self.grid_cerreg.GetCellValue(2,3)))
            except:
                print 'La fecha del certificado de registo presupuestal 3 es incorrecta'
                return
            cerreg3_dic = {'numero': unicode(self.grid_cerreg.GetCellValue(2,0)),
                       'fecha':cerreg3_fecha}
            
        #Si se escribe algo en el campo concepto, crear un nuevo diccionario tipo concepto con los datos brindados por el frame
        if unicode(self.text_orden.GetValue()).__len__()>0:
            file_concepto = codecs.open("concepto/%s.txt"%(self.text_orden.GetValue()), mode='w', encoding='utf-8')
            file_concepto.write(unicode(self.text_concepto.GetValue()))
            file_concepto.close()
            concepto_dic = {'descripcion': unicode(file_concepto.name)}
            
        #Si es posible, crear el primer diccionario tipo infocond con los datos brindados por el frame
        if unicode(self.grid_infocond.GetCellValue(0,0)).__len__()>0 or unicode(self.grid_infocond.GetCellValue(0,1)).__len__()>0 or unicode(self.grid_infocond.GetCellValue(0,2)).__len__()>0 or unicode(self.grid_infocond.GetCellValue(0,3)).__len__()>0:
            try:
                infocond1_dic = {'cheque': unicode(self.grid_infocond.GetCellValue(0,0)),
                                 'cuenta': unicode(self.grid_infocond.GetCellValue(0,1)),
                                 'codigo': unicode(self.grid_infocond.GetCellValue(0,2)),
                                 'valor': int(self.grid_infocond.GetCellValue(0,3))}
            except:
                print "Ocurrió un error mientras se intentaba generar el registro 1 de información condesada."
                return
            if unicode(self.grid_infocond.GetCellValue(0,4)).__len__()>0 and unicode(self.grid_infocond.GetCellValue(0,5)).__len__()>0 and unicode(self.grid_infocond.GetCellValue(0,6)).__len__()>0:
                try:
                    infocond1_fecha = datetime.date(int(self.grid_infocond.GetCellValue(0,4)), int(self.grid_infocond.GetCellValue(0,5)), int(self.grid_infocond.GetCellValue(0,6)))
                except:
                    print 'La fecha del registro 1 de informacion condensada es incorrecta'
                    return
                infocond1_dic['fecha'] = infocond1_fecha
            else:
                infocond1_dic['fecha'] = ''
                
        #Si es posible, crear el segundo diccionario tipo infocond con los datos brindados por el frame
        if unicode(self.grid_infocond.GetCellValue(1,0)).__len__()>0 or unicode(self.grid_infocond.GetCellValue(1,1)).__len__()>0 or unicode(self.grid_infocond.GetCellValue(1,2)).__len__()>0 or unicode(self.grid_infocond.GetCellValue(1,3)).__len__()>0:
            infocond2_dic = {'cheque': unicode(self.grid_infocond.GetCellValue(1,0)),
                             'cuenta': unicode(self.grid_infocond.GetCellValue(1,1)),
                             'codigo': unicode(self.grid_infocond.GetCellValue(1,2)),
                             'valor': int(self.grid_infocond.GetCellValue(1,3))}
            if unicode(self.grid_infocond.GetCellValue(1,4)).__len__()>0 and unicode(self.grid_infocond.GetCellValue(1,5)).__len__()>0 and unicode(self.grid_infocond.GetCellValue(1,6)).__len__()>0:
                try:
                    infocond2_fecha = datetime.date(int(self.grid_infocond.GetCellValue(1,4)), int(self.grid_infocond.GetCellValue(1,5)), int(self.grid_infocond.GetCellValue(1,6)))
                except:
                    print 'La fecha del registro 2 de informacion condensada es incorrecta'
                    return
                infocond2_dic['fecha'] = infocond2_fecha
            else:
                infocond2_dic['fecha'] = ''
        
        #Crear el diccionario discriminacion con los datos brindados por el frame
        if unicode(self.text_iva.GetValue()).__len__()>0 or unicode(self.text_retefuente.GetValue()).__len__()>0 or self.check_ret_iva.GetValue() or self.check_imp_munic.GetValue() or unicode(self.text_otros.GetValue()) or unicode(self.text_costo_bien.GetValue()) or unicode(self.text_monto.GetValue()):
            if unicode(self.text_costo_bien.GetValue()).__len__()>0:
                bien_servicio = int(self.text_costo_bien.GetValue())
            else:
                bien_servicio = ''
                
            if unicode(self.text_monto.GetValue()).__len__()>0:
                monto = int(self.text_monto.GetValue())
            else:
                monto = ''
            
            try:    
                discriminacion_dic = {'iva': unicode(self.text_iva.GetValue()),
                                      'ret_fuente': unicode(self.text_retefuente.GetValue()),
                                      'ret_iva': self.check_ret_iva.GetValue(),
                                      'imp_municipales': self.check_imp_munic.GetValue(),
                                      'otros_concepto': unicode(self.text_otros_concepto.GetValue()),
                                      'otros': unicode(self.text_otros.GetValue()),
                                      'monto': monto,
                                      'bien_servicio': bien_servicio,
                                      'pago_final': self.check_pago_final.GetValue()}
            except:
                print u"Ocurrió un error mientras se intentaba generar el registro de adiciones y descuentos."
        
        
        if comprobacion(orden):
            if orden.id!=None:
                orden.fecha=orden_dic['fecha']
                orden.compromiso = orden_dic['compromiso']
                orden.rubro = orden_dic['rubro']

            try:
                orden.beneficiario.append(Beneficiario(beneficiario_dic['nombre'], beneficiario_dic['nit']))
            except:
                pass
            try:
                orden.beneficiario[0].cerdisp.append(Cerdisp(cerdisp1_dic['numero'], cerdisp1_dic['fecha']))
            except:
                pass
            try:
                orden.beneficiario[0].cerdisp.append(Cerdisp(cerdisp2_dic['numero'], cerdisp2_dic['fecha']))
            except:
                pass
            try:
                orden.beneficiario[0].cerdisp.append(Cerdisp(cerdisp3_dic['numero'], cerdisp3_dic['fecha']))
            except:
                pass
            try:
                orden.beneficiario[0].cerreg.append(Cerreg(cerreg1_dic['numero'], cerreg1_dic['fecha']))
            except:
                pass
            try:
                orden.beneficiario[0].cerreg.append(Cerreg(cerreg2_dic['numero'], cerreg2_dic['fecha']))
            except:
                pass
            try:
                orden.beneficiario[0].cerreg.append(Cerreg(cerreg3_dic['numero'], cerreg3_dic['fecha']))
            except:
                pass
            try:
                orden.concepto.append(Concepto(concepto_dic['descripcion']))
            except:
                pass
            try:
                orden.discriminacion.append(Discriminacion(discriminacion_dic['iva'], discriminacion_dic['ret_fuente'], discriminacion_dic['ret_iva'], discriminacion_dic['imp_municipales'], discriminacion_dic['otros_concepto'], discriminacion_dic['otros'], discriminacion_dic['monto'], discriminacion_dic['bien_servicio'], discriminacion_dic['pago_final']))
            except:
                pass
            
            session.add(orden)
            session.commit()
            generar_pdf(orden)
            self.post_guardado()
                
    def sobre_escribir(self, orden):
        try:
            orden = session.query(Orden).filter(Orden.numero==int(self.text_orden.GetValue()))[0]
            print u'La orden es antigua'
        except:
            print u'La orden no es antigua'
            return
        
        if unicode(orden.compromiso).__len__()>0:
            self.text_compromiso.SetValue(unicode(orden.compromiso))
        
        fecha_antigua = wx.DateTime().Today()
        fecha_antigua.SetYear(int(str(orden.fecha).split('-')[0]))
        fecha_antigua.SetMonth(int(str(orden.fecha).split('-')[1])-1)
        fecha_antigua.SetDay(int(str(orden.fecha).split('-')[2]))
        self.date_fecha.SetValue(fecha_antigua)
        
        if orden.beneficiario.__len__()>0:
            self.text_nit.SetValue(unicode(orden.beneficiario[0].nit))
            self.text_nombre.SetValue(unicode(orden.beneficiario[0].nombre))
            if orden.beneficiario[0].cerdisp.__len__()>0:
                try:
                    self.grid_cerdisp.SetCellValue(0,0, orden.beneficiario[0].cerdisp[0].numero)
                    self.grid_cerdisp.SetCellValue(0,1, str(orden.beneficiario[0].cerdisp[0].fecha).split('-')[0])
                    self.grid_cerdisp.SetCellValue(0,2, str(orden.beneficiario[0].cerdisp[0].fecha).split('-')[1])
                    self.grid_cerdisp.SetCellValue(0,3, str(orden.beneficiario[0].cerdisp[0].fecha).split('-')[2])
                except:
                    pass
                try:
                    self.grid_cerdisp.SetCellValue(1,0, orden.beneficiario[0].cerdisp[1].numero)
                    self.grid_cerdisp.SetCellValue(1,1, str(orden.beneficiario[0].cerdisp[1].fecha).split('-')[0])
                    self.grid_cerdisp.SetCellValue(1,2, str(orden.beneficiario[0].cerdisp[1].fecha).split('-')[1])
                    self.grid_cerdisp.SetCellValue(1,3, str(orden.beneficiario[0].cerdisp[1].fecha).split('-')[2])
                except:
                    pass
                try:
                    self.grid_cerdisp.SetCellValue(2,0, orden.beneficiario[0].cerdisp[2].numero)
                    self.grid_cerdisp.SetCellValue(2,1, str(orden.beneficiario[0].cerdisp[2].fecha).split('-')[0])
                    self.grid_cerdisp.SetCellValue(2,2, str(orden.beneficiario[0].cerdisp[2].fecha).split('-')[1])
                    self.grid_cerdisp.SetCellValue(2,3, str(orden.beneficiario[0].cerdisp[2].fecha).split('-')[2])
                except:
                    pass
                
            if orden.beneficiario[0].cerreg.__len__()>0:
                try:
                    self.grid_cerreg.SetCellValue(0,0, orden.beneficiario[0].cerreg[0].numero)
                    self.grid_cerreg.SetCellValue(0,1, str(orden.beneficiario[0].cerreg[0].fecha).split('-')[0])
                    self.grid_cerreg.SetCellValue(0,2, str(orden.beneficiario[0].cerreg[0].fecha).split('-')[1])
                    self.grid_cerreg.SetCellValue(0,3, str(orden.beneficiario[0].cerreg[0].fecha).split('-')[2])
                except:
                    pass
                try:
                    self.grid_cerreg.SetCellValue(1,0, orden.beneficiario[0].cerreg[1].numero)
                    self.grid_cerreg.SetCellValue(1,1, str(orden.beneficiario[0].cerreg[1].fecha).split('-')[0])
                    self.grid_cerreg.SetCellValue(1,2, str(orden.beneficiario[0].cerreg[1].fecha).split('-')[1])
                    self.grid_cerreg.SetCellValue(1,3, str(orden.beneficiario[0].cerreg[1].fecha).split('-')[2])
                except:
                    pass
                try:
                    self.grid_cerreg.SetCellValue(2,0, orden.beneficiario[0].cerreg[2].numero)
                    self.grid_cerreg.SetCellValue(2,1, str(orden.beneficiario[0].cerreg[2].fecha).split('-')[0])
                    self.grid_cerreg.SetCellValue(2,2, str(orden.beneficiario[0].cerreg[2].fecha).split('-')[1])
                    self.grid_cerreg.SetCellValue(2,3, str(orden.beneficiario[0].cerreg[2].fecha).split('-')[2])
                except:
                    pass
        if orden.concepto.__len__()>0:
            try:
                file_concepto = codecs.open("concepto/%s.txt"%(self.text_orden.GetValue()), mode='r', encoding='utf-8')
                self.text_concepto.SetValue(unicode(file_concepto.read()))
                file_concepto.close()
            except:
                pass
            
        if orden.discriminacion.__len__()>0:
            self.text_costo_bien.SetValue(unicode(orden.discriminacion[0].bien_servicio))
            self.text_iva.SetValue(unicode(orden.discriminacion[0].iva))
            self.check_ret_iva.SetValue(orden.discriminacion[0].ret_iva)
            self.check_imp_munic.SetValue(orden.discriminacion[0].imp_municipales)
            self.text_retefuente.SetValue(unicode(orden.discriminacion[0].ret_fuente))
            self.text_otros_concepto.SetValue(unicode(orden.discriminacion[0].otros_concepto))
            self.text_otros.SetValue(unicode(orden.discriminacion[0].otros))
            self.text_monto.SetValue(unicode(orden.discriminacion[0].monto))
            self.check_pago_final.SetValue((orden.discriminacion[0].pago_final))
            
        return True
    
    def limpiar_orden(self, orden):
        for beneficiario in orden.beneficiario:
            session.delete(beneficiario)
        for concepto in orden.concepto:
            session.delete(concepto)
        for discriminacion in orden.discriminacion:
            session.delete(discriminacion)
        session.commit()
    
    def ini_num_orden(self):
        orden = session.query(Orden).all()[-1]
        self.text_orden.SetValue(str(int(orden.numero)+1))
    
    def post_guardado(self):
        self.ini_num_orden()
        self.date_fecha.SetValue(wx.DateTime().Today())
        self.text_compromiso.SetValue('')
        self.text_nit.SetValue('')
        self.text_nombre.SetValue('')
        self.grid_cerdisp.SetCellValue(0,0,'')
        self.grid_cerdisp.SetCellValue(0,1,'')
        self.grid_cerdisp.SetCellValue(0,2,'')
        self.grid_cerdisp.SetCellValue(0,3,'')
        self.grid_cerdisp.SetCellValue(1,0,'')
        self.grid_cerdisp.SetCellValue(1,1,'')
        self.grid_cerdisp.SetCellValue(1,2,'')
        self.grid_cerdisp.SetCellValue(1,3,'')
        self.grid_cerreg.SetCellValue(0,0,'')
        self.grid_cerreg.SetCellValue(0,1,'')
        self.grid_cerreg.SetCellValue(0,2,'')
        self.grid_cerreg.SetCellValue(0,3,'')
        self.grid_cerreg.SetCellValue(1,0,'')
        self.grid_cerreg.SetCellValue(1,1,'')
        self.grid_cerreg.SetCellValue(1,2,'')
        self.grid_cerreg.SetCellValue(1,3,'')
        self.text_concepto.SetValue('')
        self.text_comprobante.SetValue('')
        self.date_fechacomp.SetValue(wx.DateTime().Today())
        self.grid_infocond.SetCellValue(0,0,'')
        self.grid_infocond.SetCellValue(0,1,'')
        self.grid_infocond.SetCellValue(0,2,'')
        self.grid_infocond.SetCellValue(0,3,'')
        self.grid_infocond.SetCellValue(0,4,'')
        self.grid_infocond.SetCellValue(0,5,'')
        self.grid_infocond.SetCellValue(0,6,'')
        self.grid_infocond.SetCellValue(1,0,'')
        self.grid_infocond.SetCellValue(1,1,'')
        self.grid_infocond.SetCellValue(1,2,'')
        self.grid_infocond.SetCellValue(1,3,'')
        self.grid_infocond.SetCellValue(1,4,'')
        self.grid_infocond.SetCellValue(1,5,'')
        self.grid_infocond.SetCellValue(1,6,'')
        self.text_costo_bien.SetValue('')
        self.text_iva.SetValue('')
        self.check_ret_iva.SetValue(False)
        self.check_imp_munic.SetValue(False)
        #self.check_est_pdf.SetValue(False)
        #self.check_com_rec.SetValue(False)
        self.text_retefuente.SetValue('')
        self.text_otros_concepto.SetValue('')
        self.text_otros.SetValue('')