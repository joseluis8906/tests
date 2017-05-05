#include <iostream>
#include <ctime>

using namespace std;

void calcular_edad (int anio_nacimiento, int mes_nacimiento, int dia_nacimiento)
{
	time_t tiempo_en_bruto = time(0);

	tm* fecha_actual;
	
	fecha_actual = localtime (&tiempo_en_bruto);
	
	int anio_actual = fecha_actual->tm_year + 1900;
	int mes_actual = fecha_actual->tm_mon + 1;
	int dia_actual = fecha_actual->tm_mday;
	
	if(dia_nacimiento > dia_actual)
	{
		mes_actual -= 1;
		dia_actual += 30;
	}
	if(mes_nacimiento > mes_actual)
	{
		anio_actual -= 1;
		mes_actual += 12;
	}
	
	int anios_de_edad, meses_de_edad, dias_de_edad;
	
	anios_de_edad = anio_actual - anio_nacimiento;
	meses_de_edad = mes_actual - mes_nacimiento;
	dias_de_edad = dia_actual - dia_nacimiento;
	
	string respuesta;
	
	if(anios_de_edad > 0)
	{
		cout << anios_de_edad << " año(s)";  
	}
	if(anios_de_edad > 0 and meses_de_edad > 0)
	{
		cout << " y ";
	}
	if(meses_de_edad > 0)
	{
		cout << meses_de_edad << " mes(es)";
	}
	cout << " de edad.";
}

int main()
{
	int anio, mes, dia;
	cout << "Datos del estudiante, ingrese el año de nacimiento: ";
	cin >> anio;
	cout << "Ingrese el mes de nacimiento: ";
	cin >> mes;
	cout << "Ingrese el día de nacimiento: ";
	cin >> dia;
	
	cout << "La edad del estudiante es: ";

	calcular_edad(anio, mes, dia);
	
	cout << endl;
	
	return 0;	
}
