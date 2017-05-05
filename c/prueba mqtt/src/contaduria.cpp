#include "contaduria.hpp"

contaduria::contaduria (cppcms::service &srv) : 
	cppcms::application (srv)
{
	//this->sql.open("postgresql:dbname=edushell_db;user=edushell;host=localhost;password=123456;@pool_size=10");
		
	dispatcher ().assign ("/home", &contaduria::home, this);
	mapper ().assign ("home", "/home");
}

void contaduria::home ()
{
	response ().out () << "hola desde contaduria";
}


