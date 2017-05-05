#include "cdi.hpp"
#include "contaduria.hpp"

cdi::cdi (cppcms::service &srv) :
	cppcms::application (srv)
{
	//this->sql.open("postgresql:dbname=edushell_db;user=edushell;host=localhost;password=123456;@pool_size=10");
	//this->sql.open("mysql:dbname=edushell_db;user=edushell;host=localhost;password=administrador123456;@pool_size=10");
	attach (new contaduria (srv), "contaduria", "/contaduria{1}", "/contaduria(/(.*))?", 1);

	dispatcher ().assign ("/home", &cdi::home, this);
	mapper ().assign ("home", "/home");

	mapper ().root ("/cdi");
}


void cdi::home ()
{
	//std::cout << request().post("nombre") << std::endl;
	response ().out () << "hola";
}

/*void get ()
{
	cppcms::json::value my_object;

	cppdb::result res = this->sql << "SELECT first_name, last_name FROM users WHERE id=?" << 1 << cppdb::row;


	if (!res.empty ())
	{
		my_object["first_name"] = res.get<std::string>("first_name");
		my_object["last_name"] = res.get<std::string>("last_name");
	}

  my_object["mesage"] = "hola mundo!";

  response ().set_header ("Content-Type", "application/json");
  response ().set_header ("Server", "server cppcms/1.4.2");

  response ().out () << my_object;
}*/

int main (int argc, char *argv[])
{
	try
	{
		cppcms::service srv(argc, argv);
		srv.applications_pool ().mount (cppcms::applications_factory<cdi>());
		srv.run ();
	}
	catch (std::exception const &e)
	{
		std::cerr << e.what () << std::endl;
	}

	return 0;
}
