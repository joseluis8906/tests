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
            css_provider.load_from_path("test.css");
            
        }
        catch (GLib.Error e)
        {
            warning ("Style did not load: %s", e.message); 
        }
        Gtk.StyleContext.add_provider_for_screen (
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        );
        
        this.get_style_context ().add_class ("main1");
        
        this.set_decorated (false);
        this.set_default_size (256,375);
        this.window_position = Gtk.WindowPosition.CENTER;
        
        this.Lbl1 = new Gtk.Label ("Material Design Text Input\nWith No Extra Markup");
        this.Lbl1.get_style_context ().add_class ("l1");
        this.Lbl1.set_justify (Gtk.Justification.CENTER);
        
        var Container = new Gtk.Box (Gtk.Orientation.VERTICAL, 10);
        Container.set_homogeneous (false);
        Container.pack_start (this.Lbl1, false, false, 0);
        
        this.UserName = new Gtk.Entry ();
        this.UserName.set_placeholder_text ("UserName");
        this.Password = new Gtk.Entry ();
        this.Password.set_placeholder_text ("Password");
        this.Submit = new Gtk.Button ();
        this.Submit.set_label ("Submit");
        
        var Vbox1 = new Gtk.Box (Gtk.Orientation.VERTICAL, 5);
        Vbox1.set_homogeneous (true);
        Vbox1.set_border_width (25);
        
        Vbox1.pack_start (this.UserName, false, false, 0);
        Vbox1.pack_start (this.Password, false, false, 0);
        Vbox1.pack_start (this.Submit, false, false, 0);
        
        Container.pack_start (Vbox1);
        this.add (Container);
        this.show_all ();
        
        this.destroy.connect (Gtk.main_quit);
        this.Submit.clicked.connect (Gtk.main_quit);
    }
    
    public static int main (string[] args)
    {
        Gtk.init (ref args);

        var window = new MyApp ();
        window.show_all ();
        
        Gtk.main ();

        return 0;
    }
}
