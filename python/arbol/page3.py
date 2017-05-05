import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk, Gio, Gdk

class Page3(Gtk.Box):

    def __init__(self):
    
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.set_border_width (12)
        
        self.lbl_solucion = Gtk.Label("No hay solución");
        self.lbl_solucion.set_hexpand (False)
        self.lbl_solucion.set_halign (Gtk.Align.START)
        self.pack_start (self.lbl_solucion, False, False, 0)
        
        #ingresos sin servicio
        self.ing1_sin = 0
        self.prob1_sin = 0.0
        
        self.ing2_sin = 0
        self.prob2_sin = 0.0
        
        self.ing3_sin = 0
        self.prob3_sin = 0.0
        
        #ingresos con servicio
        self.ing1_con = 0
        self.prob1_con = 0.0
        
        self.ing2_con = 0
        self.prob2_con = 0.0
        
        self.ing3_con = 0
        self.prob3_con = 0.0
        
        #costos con servicio
        self.cos_fij_anioA = 0
        self.cos_var_venA = 0.0
        
        self.cos_fij_anioB = 0
        self.cos_var_venB = 0.0
        
        self.Renderize()


    def UpdateData (self, ing1_sin, prob1_sin, ing2_sin, prob2_sin, ing3_sin, prob3_sin, ing1_con, prob1_con, ing2_con, prob2_con, ing3_con, prob3_con, cos_fij_anioA, cos_var_venA, cos_fij_anioB, cos_var_venB):
        
        self.ing1_sin = ing1_sin
        self.prob1_sin = prob1_sin

        self.ing2_sin = ing2_sin
        self.prob2_sin = prob2_sin
        
        self.ing3_sin = ing3_sin
        self.prob3_sin = prob3_sin
        
        self.ing1_con = ing1_con
        self.prob1_con = prob1_con
        
        self.ing2_con = ing2_con
        self.prob2_con = prob2_con
        
        self.ing3_con = ing3_con
        self.prob3_con = prob3_con
        
        self.cos_fij_anioA = cos_fij_anioA
        self.cos_var_venA = cos_var_venA
        
        self.cos_fij_anioB = cos_fij_anioB
        self.cos_var_venB = cos_var_venB
        
        
    def Renderize(self):
    
        res1_even2 = self.ing1_con - (self.cos_fij_anioA + (self.ing1_con * (self.cos_var_venA/100)))
        res2_even2 = self.ing2_con - (self.cos_fij_anioA + (self.ing2_con * (self.cos_var_venA/100)))
        res3_even2 = self.ing3_con - (self.cos_fij_anioA + (self.ing3_con * (self.cos_var_venA/100)))
        
        res1_even3 = self.ing1_con - (self.cos_fij_anioB + (self.ing1_con * (self.cos_var_venB/100)))
        res2_even3 = self.ing2_con - (self.cos_fij_anioB + (self.ing2_con * (self.cos_var_venB/100)))
        res3_even3 = self.ing3_con - (self.cos_fij_anioB + (self.ing3_con * (self.cos_var_venB/100)))
        
        em_even1 = (self.ing1_sin * (self.prob1_sin/100)) + (self.ing2_sin * (self.prob2_sin/100)) + (self.ing3_sin * (self.prob3_sin/100))
        em_even2 = (res1_even2 * (self.prob1_con/100)) + (res2_even2 * (self.prob2_con/100)) + (res3_even2 * (self.prob3_con/100))
        em_even3 = (res1_even3 * (self.prob1_con/100)) + (res2_even3 * (self.prob2_con/100)) + (res3_even3 * (self.prob3_con/100))
        
        tipo_servicio = ""
        equipo = ""
        
        if(em_even1 > em_even2 and em_even1 > em_even3):
            tipo_servicio = " sin domicilio "
            
        elif(em_even2 > em_even1 and em_even2 > em_even3):
            tipo_servicio = " a domicilio "
            equipo = " con el equipo A "
            
        elif(em_even3 > em_even1 and em_even3 > em_even2):
            tipo_servicio = " a domicilio "
            equipo = "con el equipo B "
        
        self.lbl_solucion.set_text(""+
            "Evaluación de Ingreso y Costo\n"+

            "\nEvento 1\n"+
            "\t${0} ({1}%)\n".format(self.ing1_sin, self.prob1_sin)+
            "\t${0} ({1}%)\n".format(self.ing2_sin, self.prob2_sin)+
            "\t${0} ({1}%)\n".format(self.ing3_sin, self.prob3_sin)+
            
            "\nEvento 2\n"+    
            "\t${0} - ({1} + ({0} x {2}%)) = {3}\n".format(self.ing1_con, self.cos_fij_anioA, self.cos_var_venA, int(res1_even2))+
            "\t${0} - ({1} + ({0} x {2}%)) = {3}\n".format(self.ing2_con, self.cos_fij_anioA, self.cos_var_venA, int(res2_even2))+
            "\t${0} - ({1} + ({0} x {2}%)) = {3}\n".format(self.ing3_con, self.cos_fij_anioA, self.cos_var_venA, int(res3_even2))+
            
            "\nEvento 3\n"+
            "\t${0} - ({1} + ({0} x {2}%)) = {3}\n".format(self.ing1_con, self.cos_fij_anioB, self.cos_var_venB, int(res1_even3))+
            "\t${0} - ({1} + ({0} x {2}%)) = {3}\n".format(self.ing2_con, self.cos_fij_anioB, self.cos_var_venB, int(res2_even3))+
            "\t${0} - ({1} + ({0} x {2}%)) = {3}\n".format(self.ing3_con, self.cos_fij_anioB, self.cos_var_venB, int(res3_even3))+
            
            "\nToma de Decisión\n"+
            "\tE.M Evento 1: ({0} x {1}%) + ({2} x {3}%) + ({4} x {5}%) = ${6}\n".format(int(self.ing1_sin), self.prob1_sin, int(self.ing2_sin), self.prob2_sin, int(self.ing3_sin), self.prob3_sin, int(em_even1))+
            "\tE.M Evento 2: ({0} x {1}%) + ({2} x {3}%) + ({4} x {5}%) = ${6}\n".format(int(res1_even2), self.prob1_con, int(res2_even2), self.prob2_con, int(res3_even2), self.prob3_con, int(em_even2))+
            "\tE.M Evento 3: ({0} x {1}%) + ({2} x {3}%) + ({4} x {5}%) = ${6}\n".format(int(res1_even3), self.prob1_con, int(res2_even3), self.prob2_con, int(res3_even3), self.prob3_con, int(em_even3))+
            
            "\nRespuesta\n"+
            "\tPrestar el servicio{0}{1}por tener mayor utilidad.".format(tipo_servicio, equipo)
        )

