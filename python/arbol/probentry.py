import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk

class ProbEntry(Gtk.Entry):

    def __init__(self):
        
        Gtk.Entry.__init__(self)
        
        self.set_hexpand (False)
        self.set_halign (Gtk.Align.CENTER)
        self.set_width_chars (6)
        self.set_max_length (6)
        
        self.set_text ("%")
        
        self.connect("key-release-event", self.UpdateText)

    def UpdateText(self, wg, ev):
        
        posfix = "%"
        original_list = self.get_text()[:-1].split(".")
        original_str = "".join(original_list)
        
        result = ""
        
        try:
            float(original_str)
        except ValueError:
            original_str = original_str[0:-1]
        
        if(self.get_text().__len__() == 0):
            result = "%"
            self.set_text(result)
            self.set_position(0)
            
        elif(self.get_text().__len__() == 1 and self.get_text() != "%"):
            result = self.get_text()+posfix
            self.set_text(result)
            self.set_position(1)
            
        elif(original_str.__len__() == 1):
            result = original_str+posfix
            self.set_text (result)
            self.set_position(1)
            
        elif(original_str.__len__() == 2):
            result = original_str+posfix
            self.set_text (result)
            self.set_position(2)
            
        elif(original_str.__len__() == 3 and original_str == "100"):
            result = original_str+posfix
            self.set_text (result)
            self.set_position(3)
            
        elif(original_str.__len__() == 3):
            result = original_str[0]+"."+original_str[1:]+posfix
            self.set_text (result)
            self.set_position(4)
            
        elif(original_str.__len__() == 4):
            result = original_str[0:2]+"."+original_str[2:]+posfix
            self.set_text (result)
            self.set_position(5)
            
    def GetPercentValue(self):
        
        original_list = self.get_text()[:-1].split(".")
        original_str = ".".join(original_list)
        
        result = 0.0
        
        try:
            result = float(original_str)
        except ValueError:
            print("Return Value Is Not A Percent")
        
        return result