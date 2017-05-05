import wx
from MyFrame import MyFrame

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True