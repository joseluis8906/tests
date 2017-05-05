#include "persona.hpp"

persona::persona ()
{
	
}

persona::persona (std::string cc, std::string nombre, unsigned int edad)
{
	this->cc = cc;
	this->nombre = nombre;
	this->edad = edad;
}

persona::~persona ()
{

}

void persona::set_cc ()
{
	std::cin >> this->cc;
	std::cin.get ();
}

void persona::set_cc (std::string cc)
{
	this->cc = cc;
}

std::string persona::get_cc ()
{
	return this->cc;
}

void persona::set_nombre ()
{
	std::getline (std::cin, this->nombre);
}

void persona::set_nombre(std::string nombre)
{
	this->nombre = nombre;
}

std::string persona::get_nombre ()
{
	return this->nombre;
}

void persona::set_edad ()
{
	std::cin >> this->edad;
	std::cin.get ();
}

void persona::set_edad (unsigned int edad)
{
	this->edad = edad;
}

unsigned int persona::get_edad ()
{
	return this->edad;
}
