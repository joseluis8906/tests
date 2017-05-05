#include <iostream>
#include <string>
#include <cppdb/frontend.h>
#include <ctime>


int main()
{
        try {
                cppdb::session sql("postgresql:dbname=edushell_db;user=edushell;host=localhost;password=123456;");
                
                cppdb::result res;
                res = sql << "SELECT first_name, last_name FROM users WHERE id=?" << 1 << cppdb::row;
                
                if(!res.empty()) 
                {
                        std::string first_name = res.get<std::string>("first_name");
                        std::string last_name = res.get<std::string>("last_name");
                        std::cout << "The values are " << first_name << " " << last_name << std::endl;
                }
        }
        catch(std::exception const &e) {
                std::cerr << "ERROR: " << e.what() << std::endl;
                return 1;
        }
        return 0;
}
