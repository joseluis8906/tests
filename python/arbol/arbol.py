#!/usr/bin/python3

import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk

from page1 import Page1
from page2 import Page2
from page3 import Page3

class ArbolDecision(Gtk.Window):

    def __init__(self):
    
        Gtk.Window.__init__(self, title="Árbol De Decisión")
        
        self.set_default_size(256, 600)
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
       
        self.page1 = Page1()
        self.notebook.append_page(self.page1, Gtk.Label('Tablas'))
        
        self.page2 = Page2()
        self.notebook.append_page(self.page2, Gtk.Label('Gráfico'))
        
        self.page3 = Page3()
        self.notebook.append_page(self.page3, Gtk.Label('Solución'))
        
        self.page1.btn_update.connect("clicked", self.Guardar)
        
    def Guardar(self, ev):
        val_list = self.page1.GetText()
        
        t1c1 = val_list[0][0]+" ("+val_list[0][1]+")"
        t2c1 = val_list[0][2]+" ("+val_list[0][3]+")"
        t3c1 = val_list[0][4]+" ("+val_list[0][5]+")"
        
        t1c2 = val_list[0][6]+" ("+val_list[0][7]+")"
        t2c2 = val_list[0][8]+" ("+val_list[0][9]+")"
        t3c2 = val_list[0][10]+" ("+val_list[0][11]+")"
        
        t1c3 = val_list[0][6]+" ("+val_list[0][7]+")"
        t2c3 = val_list[0][8]+" ("+val_list[0][9]+")"
        t3c3 = val_list[0][10]+" ("+val_list[0][11]+")"
        
        self.page2.UpdateData(t1c1,t2c1,t3c1,t1c2,t2c2,t3c2,t1c3,t2c3,t3c3)
        
        value_list = self.page1.GetValue()
        self.page3.UpdateData(value_list[0][0],value_list[0][1],value_list[0][2],value_list[0][3],value_list[0][4],value_list[0][5],value_list[0][6],value_list[0][7],value_list[0][8],value_list[0][9],value_list[0][10],value_list[0][11],value_list[1][0],value_list[1][1],value_list[1][2],value_list[1][3])
        self.page3.Renderize()

def main():    
    win = ArbolDecision()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
