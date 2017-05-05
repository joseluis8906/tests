#include <iostream>
#include "persona.hpp"

Persona::Persona ()
{
  
}

int main (int argc, char **argv)
{
	Persona persona1 = Persona();
	std::cout << "ingrese el tamaño de la lista: " << std::endl;
	int tamanio;
	std::cin >> tamanio;
	std::cin.sync ();
	std::cin.get ();
	
	Persona personas[tamanio];
	int length = sizeof(personas)/sizeof(personas[0]);
	
	for (int i = 0; i < length; i++)
	{
		std::cout << "datos de la " << i+1 << " persona." << std::endl;
		std::cout << "nombre: " << std::endl;
		std::getline (std::cin, personas[i].nombre);
		std::cout << "edad: " << std::endl;
		std::cin >> personas[i].edad;
		std::cin.sync ();
		std::cin.get ();
	}
	
	for (int i = 0; i < length; i++)
	{
		std::cout << "Los datos son:" << std::endl;
		std::cout << i+1 << " persona:" << std::endl;
		std::cout << personas[i].nombre << std::endl;
		std::cout << personas[i].edad << std::endl;
	}
	
	return 0;
}
