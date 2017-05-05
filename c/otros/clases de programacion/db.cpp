#include "db.hpp"
#include "persona.hpp"

typedef std::vector<std::string> fields;

fields registro;

std::list<persona> personas;

void nuevo_registro()
{
	if (personas.size () == 0)
	{	cargar_datos (); }
	
	persona nueva_persona;

	std::cout << "Ingrese el número de cédula:" << std::endl;
	
	nueva_persona.set_cc ();
	
	if (verificar_cedula (nueva_persona.get_cc ()) == 0)
	{
		std::cout << "Ingrese el nombre completo:" << std::endl;
		nueva_persona.set_nombre ();
		
		std::cout << "Ingrese la edad:" << std::endl;
		nueva_persona.set_edad ();
		
		personas.push_back (nueva_persona);
		
		guardar_datos ();
	}
	else
	{
		std::cout << "Hay un usuario registrado con ese número de cédula" << std::endl;
	}
}

void actualizar_registro ()
{
	if (personas.size () == 0)
	{ cargar_datos (); }
	
	std::string cedula;
	std::cout << "Ingrese el número de cédula:" << std::endl;
	std::cin >> cedula;
	std::cin.get ();
	
	bool encontrado = false;
	
	for (auto it = personas.begin (); it != personas.end (); ++it)
	{
		if (it->get_cc () == cedula)
		{
			encontrado = true;
			std::cout << "El campo nombre es: " << it->get_nombre () << std::endl;
			std::cout << "Escriba un nuevo nombre para modificarlo o presione enter para seguir: " << std::endl;
			
			std::string nuevo_nombre;
			std::getline (std::cin, nuevo_nombre);

			if (nuevo_nombre != "")
			{ it->set_nombre (nuevo_nombre); }
			
			std::cout << "El campo edad es: " << it->get_edad () << std::endl;
			std::cout << "Escriba una nueva edad para modificarla o escriba el 0 para seguir: " << std::endl;
			
			unsigned int nueva_edad;
			std::cin >> nueva_edad;
			std::cin.get ();
			
			if (nueva_edad > 0)
			{ it->set_edad (nueva_edad); }
			
			std::cout << "se cambió a " + it->get_nombre () << " y " << it->get_edad () << std::endl;
			
			guardar_datos ();
			
			break;
		}
	}
	
	if (!encontrado)
	{	std::cout << "El número de cédula no concuerda con ningún registro." << std::endl; }
}

void eliminar_registro ()
{
	if (personas.size () == 0)
	{ cargar_datos (); }
	
	std::string cedula;
	std::cout << "Ingrese el número de cédula:" << std::endl;
	std::cin >> cedula;
	std::cin.get ();
	
	bool encontrado = false;
	
	for (auto it = personas.begin (); it != personas.end (); ++it)
	{
		if (it->get_cc () == cedula)
		{
			encontrado = true;
			personas.erase (it);
			guardar_datos ();
			break;
		}
	}
	
	if (!encontrado)
	{	std::cout << "El número de cédula no concuerda con ningún registro." << std::endl; }
}

void buscar_registro ()
{
	if (personas.size () == 0)
	{ cargar_datos (); }
	
	std::string cedula;
	std::cout << "Ingrese el número de cédula:" << std::endl;
	std::cin >> cedula;
	std::cin.get ();
	
	bool encontrado = false;
	
	for (auto it = personas.begin (); it != personas.end (); ++it)
	{
		if (it->get_cc () == cedula)
		{
			encontrado = true;
			std::cout << "La cédula es: " << it->get_cc () << std::endl;
			std::cout << "El nombre es: " << it->get_nombre () << std::endl;
			std::cout << "La edad es: " << it->get_edad () << std::endl;
			break;			
		}
	}
	
	if (!encontrado)
	{	std::cout << "El número de cédula no concuerda con ningún registro." << std::endl; }
}

void cargar_datos ()
{
	char registro_txt[128];
	std::fstream fichero;
	fichero.open ("db.txt", std::ios::in);

	while (fichero.getline (registro_txt, 128, '\n') != NULL)
	{
		boost::split (registro, registro_txt, boost::is_any_of (","), boost::token_compress_on);
		personas.push_back ( persona ( registro.at (0), registro.at (1), std::stoi (registro.at (2), nullptr, 10) ) );
	}
	fichero.close ();
}

void guardar_datos ()
{
	std::string statement = "";

	std::fstream fichero;
	fichero.open ("db.txt", std::ios::out);
	
	for (auto it = personas.begin(); it != personas.end (); ++it)
	{
		statement += it->get_cc () + "," + it->get_nombre () + "," + std::to_string (it->get_edad ()) + ((it != personas.end ()) ? "\n" : "");
	}
	fichero << statement;
	fichero.close ();
}

void imprimir_registros ()
{
	for (auto it = personas.begin(); it != personas.end (); ++it)
	{
		std::cout << it->get_nombre () << std::endl;
	}
}

int verificar_cedula (std::string cedula)
{
	for (auto it = personas.begin(); it != personas.end (); ++it)
	{
		 if(it->get_cc () == cedula)
		 {
		 	return 1;
		 }
	}
	return 0;
}
