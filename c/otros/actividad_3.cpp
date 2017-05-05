#include <iostream>
#include <string>
#include <vector>

using namespace std; 

double celcius_a_fahrenheit (double celcius)
{
	double fahrenheit = ((celcius * 9.0)/5.0) + 32.0;
	return fahrenheit;
}


//función principal
int main ()
{
	double grados_celcius;
	cout << "Ingrese los grados celcius para pasarlos a Fahrenheit" << endl;
	cin >> grados_celcius;

	cout << "La conversión es: " << grados_celcius << "ºC" << " = " << celcius_a_fahrenheit (grados_celcius) << "ºF." << endl;
}


