#ifndef IAS_DB_HPP
#define IAS_DB_HPP

#include <iostream>
#include <string>
#include <cppdb/frontend.h>
#include "user.hpp"

namespace ias
{

class db
{
private:
	cppdb::session session;
	ias::user user;
	
public:
	db (std::string);
	~db ();
	bool check_user ();
};

}

#endif

