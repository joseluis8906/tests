#include <iostream>
#include <cmath>

using namespace std;

void anualidad ();
void numero_de_anios ();
void capital_restante ();

double calcular_anualidad (int, double, int);
double calcular_nro_de_anios (int, double, int);
int calcular_capital_restante (int, double, int, int);

int main ()
{
	cout << "Selecciones una opción:" << endl;
	cout << "a) Anualidad. \nb) Número de años. \nc) Capital restante." << endl << endl;
	
	char opcion;
	
	cin >> opcion;
	
	switch (opcion)
	{
		case 'a':			
			anualidad ();
			break;

		case 'b':
			numero_de_anios ();
			break;
			
		case 'c':
			capital_restante ();
			break;
			
		default:
			cout << "Opción inválida." << endl;
	}
}

void anualidad ()
{
	int nro_de_anios;
	cout << "Ingrese el número de años a los que desea el crédito: ";
	cin >> nro_de_anios;
	
	double porcentaje_de_interes;
	cout << "Ingrese el porcentaje de interés del crédito: ";
	cin >> porcentaje_de_interes;
	
	int capital;
	cout << "Ingrese el capital del crédito: ";
	cin >> capital;
	
	double valor_anualidad = calcular_anualidad (nro_de_anios, (porcentaje_de_interes/100.0), capital);
	
	cout << "El valor anual a pagar es: $" << int(valor_anualidad) << endl;
}

double calcular_anualidad (int nro_de_anios, double porcentaje_de_interes, int capital)
{
	
	return ((capital * porcentaje_de_interes) / (1 - pow(1 + porcentaje_de_interes, (-nro_de_anios))));
}

void numero_de_anios ()
{
	int capital;
	cout << "Ingrese el capital del crédito: ";
	cin >> capital;
	
	double interes_anual;
	cout << "Ingrese el porcentaje de interés anual del crédito: ";
	cin >> interes_anual;
	
	int valor_de_cuotas;
	cout << "Ingrese el valor de las cuotas: ";
	cin >> valor_de_cuotas;
	
	double nro_de_anios = calcular_nro_de_anios (capital, (interes_anual/100.0), valor_de_cuotas);
	
	cout << "El número de años del crédito es: " << int(nro_de_anios) << endl;
}

double calcular_nro_de_anios (int capital, double interes_anual, int valor_de_cuotas)
{
	return (log(1-((capital*interes_anual)/valor_de_cuotas)) / log(1/(1+interes_anual)));
}

void capital_restante ()
{
	int capital;
	cout << "Ingrese el capital del crédito: ";
	cin >> capital;
	
	double interes;
	cout << "Ingrese el porcentaje de interés del crédito: ";
	cin >> interes;
	
	int valor_de_cuotas;
	cout << "Ingrese el valor de las cuotas: ";
	cin >> valor_de_cuotas;
	
	int nro_cuotas_pagas;
	cout << "Ingrese el número de cuotas que ha pagado: ";
	cin >> nro_cuotas_pagas;
	
	int cp_restante = calcular_capital_restante (capital, (interes/100.0), valor_de_cuotas, nro_cuotas_pagas);
	
	cout << "El capital restante que falta por pagar es: " << cp_restante << " pesos. " << endl;
}

int calcular_capital_restante (int capital, double interes, int valor_de_cuotas, int nro_cuotas_pagas)
{
	return ((valor_de_cuotas + ((capital * interes) - valor_de_cuotas) * pow((1 + interes), nro_cuotas_pagas)) / interes);
}
