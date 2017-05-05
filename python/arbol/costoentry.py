import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk

class CostoEntry(Gtk.Entry):

    def __init__(self):
        
        Gtk.Entry.__init__(self)
        
        self.set_hexpand (False)
        self.set_halign (Gtk.Align.START)
        self.set_width_chars (11)
        self.set_max_length (11)
        
        self.set_text ("$")
        
        self.connect("key-release-event", self.UpdateText)

    def UpdateText(self, wg, ev):
        
        prefix = "$"
        original_list = self.get_text()[1:].split(".")
        
        original_str = "".join(original_list)
        
        result = ""
        
        try:
            int(original_str)
        except ValueError:
            original_str = original_str[0:-1]

        if(self.get_text().__len__() == 0):
            result = "$"
            self.set_text (result)
            self.set_position(-1)
            
        elif(original_str.__len__() <= 3):
            result = prefix+original_str
            self.set_text (result)
            self.set_position(-1)
            
        elif(original_str.__len__() == 4):
            result = prefix+original_str[0]+"."+original_str[1:]
            self.set_text (result)
            self.set_position(-1)
            
        elif(original_str.__len__() == 5):
            result = prefix+original_str[0:2]+"."+original_str[2:]
            self.set_text (result)
            self.set_position(-1)
            
        elif(original_str.__len__() == 6):
            result = prefix+original_str[0:3]+"."+original_str[3:]
            self.set_text (result)
            self.set_position(-1)
        
        elif(original_str.__len__() == 7):
            result = prefix+original_str[0]+"."+original_str[1:4]+"."+original_str[4:]
            self.set_text (result)
            self.set_position(-1)
            
        elif(original_str.__len__() == 8):
            result = prefix+original_str[0:2]+"."+original_str[2:5]+"."+original_str[5:]
            self.set_text (result)
            self.set_position(-1)
            
    def GetIntValue(self):
        
        original_list = self.get_text()[1:].split(".")
        
        original_str = "".join(original_list)
        
        result = 0
        
        try:
            result = int(original_str)
        except ValueError:
            print("Return Value Is Not A Number")
        
        return result