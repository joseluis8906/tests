#include <iostream>
#include "db.hpp"
 
int main (int argc, char* argv[])
{
	ias::db db = ias::db ("sqlite3:db=db.sqlite");
	
	if(db.check_user ())
	{
		std::cout << "Acceso permitido" << std::endl;
	}
	else
	{
		std::cout << "Acceso denegado" << std::endl;
	}
	return 0;
}
