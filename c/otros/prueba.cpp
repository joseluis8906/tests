#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    vector<char> v;
    for (int x='A'; x<='Z'; x++)
    {
		v.push_back(x);
    }
    
    vector<char>::iterator it;
    
    cout << "\nDesplegando datos" << endl;
    
    for(it = v.begin(); it != v.end(); it++)
    {
		cout << *it << endl;
	}
	
	system("sleep 10");
	return EXIT_SUCCESS;
}
