using GLib;
using Gtk; 

public class MyApp : Gtk.Window
{
    private Gtk.Label Lbl1;
    private Gtk.Entry UserName;
    private Gtk.Entry Password;
    private Gtk.Button Submit;
    
    protected MyApp ()
    {
        var css_provider = new Gtk.CssProvider();
        try
        {
            css_provider.load_from_path ("test.css");
        }
        catch (GLib.Error e)
        {
            warning ("Style css can't load");
        }
        
        Gtk.StyleContext.add_provider_for_screen (
            Gdk.Screen.get_default (),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        );
        
        this.get_style_context ().add_class ("main");
        
        this.set_decorated (false);
        this.set_default_size (256, 375);
        this.window_position = Gtk.WindowPosition.CENTER;
        
        this.Lbl1 = new Gtk.Label ("Material Design Text Input\nWith No Extra Marckup");
        this.Lbl1.get_style_context ().add_class ("l1");
        this.Lbl1.set_justify (Gtk.Justification.CENTER);
        
        var container = new Gtk.Box(Gtk.Orientation.VERTICAL, 10);
        container.pack_start (this.Lbl1, false, false, 0);
        
        var Vbox1 = new Gtk.Box(Gtk.Orientation.VERTICAL, 10);
        Vbox1.set_border_width (25);
        
        container.pack_start (Vbox1, true, true, 0);
        
        this.UserName = new Gtk.Entry ();
        this.UserName.set_placeholder_text ("UserName");
        Vbox1.pack_start (this.UserName, false, false, 25);

        this.Password = new Gtk.Entry ();
        this.Password.set_placeholder_text ("Password");
        Vbox1.pack_start (this.Password, false, false, 25);
        
        this.Submit = new Gtk.Button.with_label ("Submit");
        Vbox1.pack_start (this.Submit, false, false, 25);
        
        this.add (container);
        this.show_all();
        
        this.destroy.connect (Gtk.main_quit);
        //this.Submit.clicked.connect (Gtk.main_quit);
    }
    
    public static int main (string[] args)
    {
        Gtk.init(ref args);
        new MyApp ();
        Gtk.main ();
        return 0;
    }
}
