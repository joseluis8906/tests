import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk, Gio, Gdk
from probentry import ProbEntry
from costoentry import CostoEntry

class TblCifVen(Gtk.Grid):

    def __init__(self):
    
        Gtk.Grid.__init__(self)
        
        self.set_column_spacing (1)
        self.set_row_spacing (1)
        self.set_column_homogeneous (False)

        self.insert_column(1)
        self.insert_column(2)
        self.insert_column(3)
        
        self.insert_row(1)
        self.insert_row(2)
        self.insert_row(3)
        self.insert_row(4)
        
        self.lbl_cifra_de_ventas = Gtk.Label('Tabla Cifra De Ventas')
        self.attach(self.lbl_cifra_de_ventas, 0, 0, 4, 1)
        
        
        ####### sin servicio
        self.lbl_sin_servicio = Gtk.Label('Sin Servicio')
        self.attach(self.lbl_sin_servicio, 0, 1, 2, 1)
        
        self.lbl_ingresos1 = Gtk.Label('Ingresos')
        self.attach(self.lbl_ingresos1, 0, 2, 1, 1)
        
        self.lbl_prob1 = Gtk.Label('Probabilidad')
        self.attach(self.lbl_prob1, 1, 2, 1, 1)
        
        self.txt_ingreso1_sin = CostoEntry()
        self.attach(self.txt_ingreso1_sin, 0, 3, 1, 1)
        self.txt_ingreso2_sin = CostoEntry()
        self.attach(self.txt_ingreso2_sin, 0, 4, 1, 1)
        self.txt_ingreso3_sin = CostoEntry()
        self.attach(self.txt_ingreso3_sin, 0, 5, 1, 1)
        
        self.txt_prob1_sin = ProbEntry()
        self.attach(self.txt_prob1_sin, 1, 3, 1, 1)
        self.txt_prob2_sin = ProbEntry()
        self.attach(self.txt_prob2_sin, 1, 4, 1, 1)
        self.txt_prob3_sin = ProbEntry()
        self.attach(self.txt_prob3_sin, 1, 5, 1, 1)
        
        
        ##### con servicio 
        self.lbl_con_servicio = Gtk.Label('Con Servicio')
        self.attach(self.lbl_con_servicio, 2, 1, 2, 1)
        
        self.lbl_ingresos2 = Gtk.Label('Ingresos')
        self.attach(self.lbl_ingresos2, 2, 2, 1, 1)
        
        self.lbl_prob2 = Gtk.Label('Probabilidad')
        self.attach(self.lbl_prob2, 3, 2, 1, 1)
        
        self.txt_ingreso1_con = CostoEntry()
        self.attach(self.txt_ingreso1_con, 2, 3, 1, 1)
        self.txt_ingreso2_con = CostoEntry()
        self.attach(self.txt_ingreso2_con, 2, 4, 1, 1)
        self.txt_ingreso3_con = CostoEntry()
        self.attach(self.txt_ingreso3_con, 2, 5, 1, 1)
        
        self.txt_prob1_con = ProbEntry()
        self.attach(self.txt_prob1_con, 3, 3, 1, 1)
        self.txt_prob2_con = ProbEntry()
        self.attach(self.txt_prob2_con, 3, 4, 1, 1)
        self.txt_prob3_con = ProbEntry()
        self.attach(self.txt_prob3_con, 3, 5, 1, 1)
        
        
    def GetText(self):
        return([self.txt_ingreso1_sin.get_text(), self.txt_prob1_sin.get_text(), self.txt_ingreso2_sin.get_text(), self.txt_prob2_sin.get_text(), self.txt_ingreso3_sin.get_text(), self.txt_prob3_sin.get_text(), self.txt_ingreso1_con.get_text(), self.txt_prob1_con.get_text(), self.txt_ingreso2_con.get_text(), self.txt_prob2_con.get_text(), self.txt_ingreso3_con.get_text(), self.txt_prob3_con.get_text()])
        
        
    def GetValue(self):
        return([self.txt_ingreso1_sin.GetIntValue(), self.txt_prob1_sin.GetPercentValue(), self.txt_ingreso2_sin.GetIntValue(), self.txt_prob2_sin.GetPercentValue(), self.txt_ingreso3_sin.GetIntValue(), self.txt_prob3_sin.GetPercentValue(), self.txt_ingreso1_con.GetIntValue(), self.txt_prob1_con.GetPercentValue(), self.txt_ingreso2_con.GetIntValue(), self.txt_prob2_con.GetPercentValue(), self.txt_ingreso3_con.GetIntValue(), self.txt_prob3_con.GetPercentValue()])
        
        
              
