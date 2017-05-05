import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk, Gio, Gdk
from probentry import ProbEntry
from costoentry import CostoEntry

class TblCosSer(Gtk.Grid):

    def __init__(self):
    
        Gtk.Grid.__init__(self)
        
        self.set_column_spacing (1)
        self.set_row_spacing (1)
        self.set_column_homogeneous (False)

        self.insert_column(1)
        self.insert_column(2)
        
        self.insert_row(1)
        self.insert_row(2)
        self.insert_row(3)
        
        self.lbl_costo_del_servicio = Gtk.Label('Tabla Costo Del Servicio')
        self.attach(self.lbl_costo_del_servicio, 0, 0, 3, 1)
        
        self.lbl_costos = Gtk.Label('Costos')
        self.attach(self.lbl_costos, 0, 1, 1, 2)
        
        self.lbl_equipo = Gtk.Label('Equipo')
        self.attach(self.lbl_equipo, 1, 1, 2, 1)
        
        self.lbl_a = Gtk.Label('A')
        self.attach(self.lbl_a, 1, 2, 1, 1)
        
        self.lbl_b = Gtk.Label('B')
        self.attach(self.lbl_b, 2, 2, 1, 1)
        
        self.lbl_c_fijo_x_anio = Gtk.Label('Fijo x Año')
        self.attach(self.lbl_c_fijo_x_anio, 0, 3, 1, 1)
        
        self.lbl_c_var_x_ven = Gtk.Label('Variable x Venta')
        self.attach(self.lbl_c_var_x_ven, 0, 4, 1, 1)
        
        self.txt_c_fijo1 = CostoEntry()
        self.attach(self.txt_c_fijo1, 1, 3, 1, 1)
        self.txt_c_fijo2 = CostoEntry()
        self.attach(self.txt_c_fijo2, 2, 3, 1, 1)
        
        self.txt_c_var_x_ven1 = ProbEntry()
        self.attach(self.txt_c_var_x_ven1, 1, 4, 1, 1)
        self.txt_c_var_x_ven2 = ProbEntry()
        self.attach(self.txt_c_var_x_ven2, 2, 4, 1, 1)

    def GetText(self):
        return([self.txt_c_fijo1.get_text(), self.txt_c_var_x_ven1.get_text(), self.txt_c_fijo2.get_text(), self.txt_c_var_x_ven2.get_text()])
        
        
    def GetValue(self):
        return([self.txt_c_fijo1.GetIntValue(), self.txt_c_var_x_ven1.GetPercentValue(), self.txt_c_fijo2.GetIntValue(), self.txt_c_var_x_ven2.GetPercentValue()])
        
        
        
