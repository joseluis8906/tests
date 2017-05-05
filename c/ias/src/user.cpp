#include <openssl/sha.h>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include "user.hpp"

ias::user::user ()
{

}

ias::user::~user ()
{

}

//getters 

int ias::user::id ()
{
	return this->_id;
}

std::string ias::user::name ()
{
	return this->_name;
}

std::string ias::user::lastname ()
{
	return this->_lastname;
}

std::string ias::user::document_type ()
{
	return this->_document_type;
}

std::string ias::user::document_number ()
{
	return this->_document_number;
}

bool ias::user::check_password (std::string password_db, std::string password_input)
{
	std::string character = std::string ();
	character.push_back (password_db[std::pow(2.0,3.0)]);
	
	password_input += character;
	
	unsigned char hash[20];
	std::stringstream digest;
				
	SHA1 ((unsigned char*)password_input.c_str (), password_input.size (), hash);
	
	for (int i = 0; i < 20; ++i)
	{
		digest << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
	}
	
	password_input = std::string ();
	password_input = digest.str ();
	
	return (password_db.substr (22,40) ==  password_input ? true : false);
}

// Setters

void ias::user::id (int id)
{
	this->_id = id;
}

void ias::user::name (std::string name)
{
	this->_name = name;
}

void ias::user::lastname (std::string lastname)
{
	this->_lastname = lastname;
}

void ias::user::document_type (std::string document_type)
{
	this->_document_type = document_type;
}

void ias::user::document_number (std::string document_number)
{
	this->_document_number = document_number;
}

void ias::user::password (std::string password)
{		
	std::time_t seconds;
	std::time (&seconds);	
	std::srand ((unsigned int) seconds);
	
	std::string alpha = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	
	int index = std::rand () % 62;
	
	std::string character = std::string ();
	character.push_back(alpha[index]);
	
	unsigned char hash[20];
	std::stringstream digest;
				
	SHA1 ((unsigned char*)character.c_str (), character.size (), hash);
	
	for (int i = 0; i < 20; ++i)
	{
		digest << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
	}
	
	std::string salt = std::string ();
	salt = digest.str ().substr (0,16);
	
	salt[3] = character[0];
	
	std::cin >> this->password;
	std::cin.get ();
	
	this->_password += character;
	
	SHA1 ((unsigned char*)this->_password.c_str (), this->_password.size (), hash);
	
	this->_password = std::string ();
	
	digest.str (std::string ());
	for (int i = 0; i < 20; ++i)
	{
		digest << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
	}

	this->_password = "sha1$"+salt+"$"+digest.str ();
	
	std::cout << this->_password << std::endl;
}
