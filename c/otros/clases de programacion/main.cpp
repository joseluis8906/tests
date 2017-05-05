#include <iostream>
#include "db.hpp"

int main (int argc, char* argv[])
{	
	bool continuar = true;

	while (continuar)
	{
		std::cout << "Que desea hacer:" << std::endl;
		std::cout << "a). Crear un nuevo registro." << std::endl;
		std::cout << "b). Actualizar un registro existente." << std::endl;
		std::cout << "c). Eliminar un registro existente." << std::endl;
		std::cout << "d). Buscar un registro existente." << std::endl;
		std::cout << "e). Salir." << std::endl;
		
		char opcion;
		std::cin >> opcion;
		
		switch (opcion)
		{
			case 'a':
				nuevo_registro ();
				break;
				
			case 'b':
				actualizar_registro ();
				break;
				
			case 'c':
				eliminar_registro ();
				break;
				
			case 'd':
				buscar_registro ();
				break;
				
			case 'e':
				continuar = false;
				break;
				
			default:
				std::cout << "Elija una opción válida" << std::cout;
		}
		
	}
	
	return 0;
}
