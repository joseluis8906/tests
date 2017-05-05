#include <iostream>
#include <string>
#include <ctime>

#ifndef INCLUDE_PERSONA_HPP
#define INCLUDE_PERSONA_HPP

class persona
{
protected:
	std::string cc;
	std::string nombre;
	unsigned int edad;
	
public:
	persona ();
	persona (std::string, std::string, unsigned int);
	~persona ();
	
	void set_cc ();
	void set_cc (std::string);
	std::string get_cc ();
	
	void set_nombre ();
	void set_nombre (std::string);
	std::string get_nombre ();
	
	void set_edad ();
	void set_edad (unsigned int);
	unsigned int get_edad ();
};

#endif
