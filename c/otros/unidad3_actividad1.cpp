#include <iostream>
#include <vector>

using namespace std;

double calcular_promedio_general (vector<int>, vector<int>, vector<int>, vector<int>, vector<int>);
void calcular_informe_por_trabajador (vector<string>, vector<int>, vector<int>, vector<int>, vector<int>, vector<int>);
double calcular_promedio_semanal_individual (vector<int>);
int calcular_cantidad_producida_mas_alta (vector<int>);
string calcular_dia_mas_productivo (vector<int>);
int calcular_dias_por_encima_del_promedio (vector<int>);


int main ()
{
	int numero_de_trabajadores;
	cout << "Ingrese el número de trabajadores a calificar ";
	cin >> numero_de_trabajadores;

	vector<string> nombres (numero_de_trabajadores);
	vector<int> unidades_del_lunes (numero_de_trabajadores);
	vector<int> unidades_del_martes (numero_de_trabajadores);
	vector<int> unidades_del_miercoles (numero_de_trabajadores);
	vector<int> unidades_del_jueves (numero_de_trabajadores);
	vector<int> unidades_del_viernes (numero_de_trabajadores);
	
	for (int i = 0; i < nombres.size(); i++)
	{
		cout << "Ingrese el nombre del trabajador número " << i+1 << endl;
		cin.ignore();
		getline(cin, nombres[i]);
		
		cout << "Ingrese las unidades hechas por " << nombres[i]  << " el día lunes." << endl;
		cin >> unidades_del_lunes[i];
		
		cout << "Ingrese las unidades hechas por " << nombres[i]  << " el día martes." << endl;
		cin >> unidades_del_martes[i];
		
		cout << "Ingrese las unidades hechas por " << nombres[i]  << " el día miércoles." << endl;
		cin >> unidades_del_miercoles[i];
		
		cout << "Ingrese las unidades hechas por " << nombres[i]  << " el día jueves." << endl;
		cin >> unidades_del_jueves[i];
		
		cout << "Ingrese las unidades hechas por " << nombres[i]  << " el día viernes." << endl;
		cin >> unidades_del_viernes[i];
	}
	
	cout << "El promedio general es: " << calcular_promedio_general (unidades_del_lunes, unidades_del_martes, unidades_del_miercoles, unidades_del_jueves, unidades_del_viernes) << " unidades." << endl << endl;
	
	cout << "El informe individual por trabajador es:" << endl;
	
	calcular_informe_por_trabajador (nombres, unidades_del_lunes, unidades_del_martes, unidades_del_miercoles, unidades_del_jueves, unidades_del_viernes);
	
	return 0;
}

double calcular_promedio_general (vector<int> lunes, vector<int> martes, vector<int> miercoles, vector<int> jueves, vector<int> viernes)
{
	int sumatoria = 0;
	double promedio;
	for (int i = 0; i < lunes.size(); i++)
	{
		sumatoria += (lunes[i]+martes[i]+miercoles[i]+jueves[i]+viernes[i]);
	}
	promedio = sumatoria/double(lunes.size()*5);
	
	return promedio;
}

void calcular_informe_por_trabajador (vector<string> nombres, vector<int> lunes, vector<int> martes, vector<int> miercoles, vector<int> jueves, vector<int> viernes)
{
	for(int i = 0; i < nombres.size (); i++)
	{
		vector<int> unidades_personales (5);
		unidades_personales[0] = lunes[i];
		unidades_personales[1] = martes[i];
		unidades_personales[2] = miercoles[i];
		unidades_personales[3] = jueves[i];
		unidades_personales[4] = viernes[i];
		cout << endl << "El informe del trabajador " << nombres[i] << " es: " << endl;
		cout << "Promedio de la semana: " << calcular_promedio_semanal_individual (unidades_personales) << endl;
		cout << "Cantidad producida mas alta: " << calcular_cantidad_producida_mas_alta (unidades_personales) << endl;
		cout << "El día mas productivo fue el " << calcular_dia_mas_productivo (unidades_personales) << endl;
		cout << "El total de dias por encima del promedio es: " << calcular_dias_por_encima_del_promedio (unidades_personales) << endl;
	}
}

double calcular_promedio_semanal_individual (vector<int> valores)
{
	double promedio;
	int sumatoria = 0;
	for (int i = 0; i < valores.size(); i++)
	{
		sumatoria += valores[i];
	}
	promedio = double(sumatoria)/valores.size();
	return promedio;
}

int calcular_cantidad_producida_mas_alta (vector<int> valores)
{
	int maximo = 0;
	for (int k = 0; k < valores.size(); k++)
	{
		if (valores[k] > maximo)
		{
			maximo = valores[k];
		}
	}
	return maximo;
}

string calcular_dia_mas_productivo (vector<int> valores)
{
	int dia = 0;
	int valor_maximo = 0;
	string semana[] = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes"};
	for (int k = 0; k < valores.size(); k++)
	{
		if (valores[k] > valor_maximo)
		{
			valor_maximo = valores[k];
			dia = k;
		}
	}
	return semana[dia];
}
int calcular_dias_por_encima_del_promedio (vector<int> valores)
{
	double promedio = calcular_promedio_semanal_individual (valores);
	int dias_por_encima_del_promedio = 0;
	for (int i = 0; i < valores.size (); i++)
	{
		if(valores[i] > promedio)
		{
			dias_por_encima_del_promedio += 1;
		}
	}
	return dias_por_encima_del_promedio;
}

