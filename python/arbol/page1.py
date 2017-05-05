import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk, Gio, Gdk
from tblcifven import TblCifVen
from tblcosser import TblCosSer

class Page1(Gtk.Box):

    def __init__(self):
    
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.set_border_width (12)
        
        self.tables = Gtk.Box (orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        self.btn_update = Gtk.Button("Guardar")
        self.btn_update.set_hexpand (False)
        self.btn_update.set_halign (Gtk.Align.START)
        
        self.pack_start(self.tables, False, True, 0)
        self.pack_start(self.btn_update, False, True, 12)
        
        self.tbl1 = TblCifVen()
        self.tbl2 = TblCosSer()
        
        self.tables.pack_start(self.tbl1, True, False, 0)
        self.tables.pack_start(self.tbl2, True, False, 0)
        
                
        style_provider = Gtk.CssProvider()
        css = """
            grid {
                background: rgba(240,240,240,1);
                border: solid rgba(200,200,200,1) 1px;
            }
        """      
        style_provider.load_from_data(css.encode())
        Gtk.StyleContext.add_provider_for_screen (
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        
        
    def GetText(self):
        return([self.tbl1.GetText(), self.tbl2.GetText()])
        
    def GetValue(self):
        return([self.tbl1.GetValue(), self.tbl2.GetValue()])
        
