#ifndef IAS_USER_HPP
#define IAS_USER_HPP

#include <iostream>
#include <string>


namespace ias
{

class user
{
private:
	int _id;
	std::string _name;
	std::string _lastname;
	std::string _document_type;
	std::string _document_number;
	std::string _password;
	
public:
	user ();
	~user ();
	int id ();
	std::string name ();
	std::string lastname ();
	std::string document_type ();
	std::string document_number ();
		
	void id (int);
	void name (std::string);
	void lastname (std::string);
	void set_document_type (std::string);
	void set_document_number (std::string);
	void set_password (std::string);
	bool check_password (std::string, std::string);
};

}

#endif
