#include "db.hpp"

ias::db::db (std::string params)
{
	this->session.open(params);
}

ias::db::~db ()
{

}

bool ias::db::check_user ()
{
	this->user = ias::user ();
	
	std::cout << std::endl;
	std::cout << "Ingrese el tipo de documento: " << std::endl;
	this->user.set_document_type ();
	
	std::cout << "Ingrese el número de documento: " << std::endl;
	this->user.set_document_number ();
	
	std::string password_input;
	std::cout << "Ingrese la contraseña: " << std::endl;
	std::cin >> password_input;
	
	//std::cout << user.get_password () << std::endl;

	cppdb::result query = this->session << "SELECT name, lastname, document_type, document_number, password FROM 'user' WHERE 'user'.'document_type'=? AND 'user'.'document_number'=?" << user.get_document_type () << user.get_document_number () << cppdb::row;
	
	//std::cout << query.empty () << std::endl;

	if (!query.empty ())
	{
		std::string password_db = query.get<std::string>("password");
		return ( user.check_password (password_db, password_input) ? true : false );
	}
	else
	{
		return false;
	}
}
