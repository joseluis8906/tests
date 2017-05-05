#include <iostream>
#include <gtkmm.h>

int main (int argc, char *argv[])
{
	Glib::RefPtr<Gtk::Application> app = Gtk::Application::create (argc, argv, "Hola mundo!");
	
	Gtk::Window window;
	window.set_default_size (250, 250);
	window.set_title ("Hola mundo!");
	
	return app->run (window);
}

