import gi
gi.require_version ("Gtk", "3.0")
from gi.repository import Gtk, Gio, Gdk, cairo
import math

class Page2(Gtk.DrawingArea):

    def __init__(self):
        
        Gtk.DrawingArea.__init__(self)
        self.set_size_request(10, 10)
        self.connect ("draw", self.OnDraw)
        
        self.text1circle1 = "T1 C1"
        self.text2circle1 = "T2 C1"
        self.text3circle1 = "T3 C1"
        
        self.text1circle2 = "T1 C2"
        self.text2circle2 = "T2 C2"
        self.text3circle2 = "T3 C2"
        
        self.text1circle3 = "T1 C3"
        self.text2circle3 = "T2 C3"
        self.text3circle3 = "T3 C3"
        
        
    def UpdateData (self, t1c1, t2c1, t3c1, t1c2, t2c2, t3c2, t1c3, t2c3, t3c3):
        
        self.text1circle1 = t1c1
        self.text2circle1 = t2c1
        self.text3circle1 = t3c1
        
        self.text1circle2 = t1c2
        self.text2circle2 = t2c2
        self.text3circle2 = t3c2
        
        self.text1circle3 = t1c3
        self.text2circle3 = t2c3
        self.text3circle3 = t3c3
        
        
    def OnDraw(self, widget, cr):
        
        RectWidth = 30
        RectHeight = 30
        
        CircleRadius = 15
        CircleWidth = CircleRadius*2
        CircleAngle = 2*math.pi
        
        WIDTH = widget.get_allocation().width
        HEIGHT = widget.get_allocation().height
        
        cr.set_line_width (1.5)
        cr.select_font_face("Arial")
        cr.set_font_size(12)
        
        #rect1
        cr.new_path()
        Rect1X = (WIDTH*0.01)+(RectWidth/2)
        Rect1Y = (HEIGHT/2)-(RectHeight/2)
        cr.rectangle(Rect1X, Rect1Y, RectWidth, RectHeight)
        cr.set_source_rgba(0,0,0,1)
        cr.stroke_preserve()
        cr.set_source_rgba(255,255,255,0)
        cr.fill()
        cr.close_path()
        
        #text rect 1
        cr.new_path ()
        TextRect1 = "1"
        (TextRect1X, TextRect1Y, TextRect1Width, TextRect1height, TextRect1dx, TextRect1dy) = cr.text_extents(TextRect1)
        cr.move_to ((Rect1X)+(RectWidth/2)-(TextRect1Width/2), (Rect1Y)+(RectHeight/2)+(TextRect1height/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (TextRect1)
        cr.close_path()
        
        #circle 1
        cr.new_path()
        Circle1X = (WIDTH*0.33)+(CircleWidth)
        Circle1Y = (HEIGHT*0.1)+(CircleWidth)
        cr.arc(Circle1X, Circle1Y, CircleRadius, 0, CircleAngle)
        cr.set_source_rgba(0,0,0,1)
        cr.stroke_preserve()
        cr.set_source_rgba(255,255,255,1)
        cr.fill()
        cr.close_path()
        
        #text circle1
        cr.new_path ()
        TextCircle1 = "1"
        (TextCircle1X, TextCircle1Y, TextCircle1Width, TextCircle1height, TextCircle1dx, TextCircle1dy) = cr.text_extents(TextCircle1)
        cr.move_to ((Circle1X)-(TextCircle1Width), (Circle1Y)+(TextCircle1height/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (TextCircle1)
        cr.close_path ()
        
        #linea del rect1 hasta el circle 1
        cr.new_path()
        cr.move_to((Rect1X+RectWidth), (Rect1Y+RectHeight/2))
        cr.line_to((Rect1X)+(RectWidth*1.5), (Rect1Y+RectHeight/2))
        cr.line_to((Rect1X)+(RectWidth*1.5), Circle1Y)
        cr.line_to((Circle1X-CircleRadius), Circle1Y)
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        
        
        #lineas del circle 1
        #line 1
        cr.new_path()
        cr.move_to((Circle1X+CircleRadius), Circle1Y)
        cr.line_to((Circle1X+CircleRadius*2.5), (Circle1Y*0.8))
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        #line 2
        cr.new_path()
        cr.move_to((Circle1X+CircleRadius), Circle1Y)
        cr.line_to((Circle1X+CircleRadius*2.5), (Circle1Y))
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        #line 3
        cr.new_path()
        cr.move_to((Circle1X+CircleRadius), Circle1Y)
        cr.line_to((Circle1X+CircleRadius*2.5), (Circle1Y*1.2))
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        
        #text 1 circle 1
        cr.new_path ()
        Text1Circle1 = self.text1circle1
        (Text1Circle1X, Text1Circle1Y, Text1Circle1Width, Text1Circle1height, Text1Circle1dx, Text1Circle1dy) = cr.text_extents(Text1Circle1)
        cr.move_to ((Circle1X+CircleRadius*3), (Circle1Y*0.8)+(Text1Circle1height/2/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (Text1Circle1)
        cr.close_path ()
        
        #textos de lineas del circle1
        #text 2 circle 1
        cr.new_path ()
        Text2Circle1 = self.text2circle1
        (Text2Circle1X, Text2Circle1Y, Text2Circle1Width, Text2Circle1height, Text2Circle1dx, Text2Circle1dy) = cr.text_extents(Text2Circle1)
        cr.move_to ((Circle1X+CircleRadius*3), (Circle1Y)+(Text2Circle1height/2/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (Text2Circle1)
        cr.close_path ()        
        #text 3 circle 1
        cr.new_path ()
        Text3Circle1 = self.text3circle1
        (Text3Circle1X, Text3Circle1Y, Text3Circle1Width, Text3Circle1height, Text3Circle1dx, Text3Circle1dy) = cr.text_extents(Text3Circle1)
        cr.move_to ((Circle1X+CircleRadius*3), (Circle1Y*1.2)+(Text3Circle1height/2/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (Text3Circle1)
        cr.close_path ()
        #rect 2
        cr.new_path()
        Rect2X = (WIDTH*0.33)+(RectWidth/2)
        Rect2Y = (HEIGHT*0.8)-(RectHeight/2)
        cr.rectangle(Rect2X, Rect2Y, RectWidth, RectHeight)
        cr.set_source_rgba(0,0,0,1)
        cr.stroke_preserve()
        cr.set_source_rgba(255,255,255,1)
        cr.fill()
        cr.close_path()
        
        #text rect 2
        cr.new_path ()
        TextRect2 = "2"
        (TextRect2X, TextRect2Y, TextRect2Width, TextRect2height, TextRect2dx, TextRect2dy) = cr.text_extents(TextRect2)
        cr.move_to ((Rect2X)+(RectWidth/2)-(TextRect2Width/2), (Rect2Y)+(RectHeight/2)+(TextRect2height/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (TextRect2)
        cr.close_path()
        
        #linea del rect 1 hasta el rect 2
        cr.new_path()
        cr.move_to((Rect1X)+(RectWidth*1.5), (Rect1Y+RectHeight/2))
        cr.line_to((Rect1X)+(RectWidth*1.5), (Rect2Y)+(RectWidth*0.5))
        cr.line_to(Rect2X, (Rect2Y)+(RectWidth*0.5))
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        
        #circulo 2
        cr.new_path()
        Circle2X = Rect2X+(Rect2X*0.5)
        Circle2Y = (Rect2Y+CircleRadius)-(Rect2Y*0.1)
        cr.arc(Circle2X, Circle2Y, CircleRadius, 0, CircleAngle)
        cr.set_source_rgba(0,0,0,1)
        cr.stroke_preserve()
        cr.set_source_rgba(255,255,255,1)
        cr.fill()
        cr.close_path()
        
        #text circle2
        cr.new_path ()
        TextCircle2 = "2"
        (TextCircle2X, TextCircle2Y, TextCircle2Width, TextCircle2height, TextCircle2dx, TextCircle2dy) = cr.text_extents(TextCircle2)
        cr.move_to ((Circle2X)-(TextCircle2Width/2), (Circle2Y)+(TextCircle2height/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (TextCircle2)
        cr.close_path ()
        
        #linea del rec2 a subir
        cr.new_path()
        cr.move_to((Rect2X)+(RectWidth), (Rect2Y+RectHeight/2))
        cr.line_to((Rect2X)+(RectWidth*2), (Rect2Y+RectHeight/2))
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        
        #linea del rect 2 hasta el circle 2
        cr.new_path()
        cr.move_to((Rect2X)+(RectWidth*2), (Rect2Y+RectHeight/2))
        cr.line_to((Rect2X)+(RectWidth*2), Circle2Y)
        cr.line_to(Circle2X-(CircleRadius), Circle2Y)
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        
        #lineas del circle 2
        #line 1
        cr.new_path()
        cr.move_to((Circle2X+CircleRadius), Circle2Y)
        cr.line_to((Circle2X+CircleRadius*2.5), (Circle2Y*0.95))
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        #line 2
        cr.new_path()
        cr.move_to((Circle2X+CircleRadius), Circle2Y)
        cr.line_to((Circle2X+CircleRadius*2.5), (Circle2Y))
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        #line 3
        cr.new_path()
        cr.move_to((Circle2X+CircleRadius), Circle2Y)
        cr.line_to((Circle2X+CircleRadius*2.5), (Circle2Y*1.05))
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        
        #textos de lineas del circle2
        #text 1 circle 2
        cr.new_path ()
        Text1Circle2 = self.text1circle2
        (Text1Circle2X, Text1Circle2Y, Text1Circle2Width, Text1Circle2height, Text1Circle2dx, Text1Circle2dy) = cr.text_extents(Text1Circle2)
        cr.move_to ((Circle2X+CircleRadius*3), (Circle2Y*0.95)+(Text1Circle2height/2/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (Text1Circle2)
        cr.close_path ()
        #text 2 circle 2
        cr.new_path ()
        Text2Circle2 = self.text2circle2
        (Text2Circle2X, Text2Circle2Y, Text2Circle2Width, Text2Circle2height, Text2Circle2dx, Text2Circle2dy) = cr.text_extents(Text2Circle2)
        cr.move_to ((Circle2X+CircleRadius*3), (Circle2Y)+(Text2Circle2height/2/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (Text2Circle2)
        cr.close_path ()
        #text 3 circle 2
        cr.new_path ()
        Text3Circle2 = self.text3circle2
        (Text3Circle2X, Text3Circle2Y, Text3Circle2Width, Text3Circle2height, Text3Circle2dx, Text3Circle2dy) = cr.text_extents(Text3Circle2)
        cr.move_to ((Circle2X+CircleRadius*3), (Circle2Y*1.05)+(Text3Circle2height/2/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (Text3Circle2)
        cr.close_path ()
        
        #circulo 3
        cr.new_path()
        Circle3X = Rect2X+(Rect2X*0.5)
        Circle3Y = (Rect2Y+CircleRadius)+(Rect2Y*0.1)
        cr.arc(Circle3X, Circle3Y, CircleRadius, 0, CircleAngle)
        cr.set_source_rgba(0,0,0,1)
        cr.stroke_preserve()
        cr.set_source_rgba(255,255,255,1)
        cr.fill()
        cr.close_path()
        
        #text circle3
        cr.new_path ()
        TextCircle3 = "3"
        (TextCircle3X, TextCircle3Y, TextCircle3Width, TextCircle3height, TextCircle3dx, TextCircle3dy) = cr.text_extents(TextCircle3)
        cr.move_to ((Circle3X)-(TextCircle3Width/2), (Circle3Y)+(TextCircle3height/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (TextCircle3)
        cr.close_path ()
        
        #linea del rect 2 hasta el circle 3
        cr.new_path()
        cr.move_to((Rect2X)+(RectWidth*2), (Rect2Y+RectHeight/2))
        cr.line_to((Rect2X)+(RectWidth*2), Circle3Y)
        cr.line_to(Circle3X-(CircleRadius), Circle3Y)
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        
        #lineas del circle 3
        #line 1
        cr.new_path()
        cr.move_to((Circle3X+CircleRadius), Circle3Y)
        cr.line_to((Circle3X+CircleRadius*2.5), (Circle3Y*0.95))
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        #line 2
        cr.new_path()
        cr.move_to((Circle3X+CircleRadius), Circle3Y)
        cr.line_to((Circle3X+CircleRadius*2.5), (Circle3Y))
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        #line 3
        cr.new_path()
        cr.move_to((Circle3X+CircleRadius), Circle3Y)
        cr.line_to((Circle3X+CircleRadius*2.5), (Circle3Y*1.05))
        cr.set_source_rgba(0,0,0,1)
        cr.stroke()
        cr.close_path()
        
        #textos de lineas del circle2
        #text 1 circle 3
        cr.new_path ()
        Text1Circle3 = self.text1circle3
        (Text1Circle3X, Text1Circle3Y, Text1Circle3Width, Text1Circle3height, Text1Circle3dx, Text1Circle3dy) = cr.text_extents(Text1Circle3)
        cr.move_to ((Circle3X+CircleRadius*3), (Circle3Y*0.95)+(Text1Circle3height/2/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (Text1Circle3)
        cr.close_path ()
        #text 2 circle 2
        cr.new_path ()
        Text2Circle3 = self.text2circle3
        (Text2Circle3X, Text2Circle3Y, Text2Circle3Width, Text2Circle3height, Text2Circle3dx, Text2Circle3dy) = cr.text_extents(Text2Circle3)
        cr.move_to ((Circle3X+CircleRadius*3), (Circle3Y)+(Text2Circle3height/2/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (Text2Circle3)
        cr.close_path ()
        #text 3 circle 2
        cr.new_path ()
        Text3Circle3 = self.text3circle3
        (Text3Circle3X, Text3Circle3Y, Text3Circle3Width, Text3Circle3height, Text3Circle3dx, Text3Circle3dy) = cr.text_extents(Text3Circle3)
        cr.move_to ((Circle3X+CircleRadius*3), (Circle3Y*1.05)+(Text3Circle3height/2/2))
        cr.set_source_rgba(0,0,0,1)
        cr.show_text (Text3Circle3)
        cr.close_path ()
        
        return True