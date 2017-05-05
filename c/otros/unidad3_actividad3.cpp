#include <iostream>
#include <vector>

using namespace std;

void impresion_de_resultados (vector<string>*, vector<int>*);
int calcular_votos (string, vector<string>*, vector<int>*);
float calcular_porcentaje (string, vector<string>*, vector<int>*);
void candidatos_ganadores (vector<string>*, vector<int>*);

int main ()
{
	vector<string> candidatos (6);
	vector<int> votos (25);
	
	cout << "##################################################################\n" 
	        "# Sistema de elecciones voto-digital, versión 0.1A licence GPL   #\n"
	        "# Autor: Jose Luis Cáceres Escudero, año: 2014                                 #\n"
	        "# Ingrese un nombre y un apellido, puede usar acentos y (ñ)s     #\n"
	        "# En lo posible (nombre+apellido) > 8 letras < 20 letras  para   #\n"
	        "# una buena presentación de datos en la tabla. Nro de votos = 25 #\n"
	        "##################################################################\n";
	
	for (int i = 0; i < (candidatos.size ()-1); i++)
	{
		cout << "Escriba el nombre del candidato numero " << i+1 << endl;
		getline(cin, candidatos[i]);
	}
	candidatos[5] = "Voto en blanco";
    
	for (int i = 0; i < votos.size (); i++)
	{
		cout << "Escriba la opción por quién desea votar:" << endl;	
		cout << "1). " << candidatos[0] << endl;
		cout << "2). " << candidatos[1] << endl;
		cout << "3). " << candidatos[2] << endl;
		cout << "4). " << candidatos[3] << endl;
		cout << "5). " << candidatos[4] << endl;
		cout << "6). Voto en blanco" << endl << endl;
		
		cin >> votos[i];
	}
	
	impresion_de_resultados (&candidatos, &votos);
}

void impresion_de_resultados (vector<string> *candidatos, vector<int> *votos)
{
	cout << "\t\t\tResultado de las Elecciones" << endl;
	cout << "---------------------------------------------------------------------------------" << endl;
	cout << "|\tCandidato\t|\tNúmero de votos\t\t|\tPorcentaje\t|" << endl;
	cout << "---------------------------------------------------------------------------------" << endl;
	
	for (int i = 0; i < candidatos->size (); i++)
	{
		cout << "| " << candidatos->at(i) << "   " << "\t|" << " " << calcular_votos(candidatos->at(i), candidatos, votos) << "\t\t\t\t|" << " " << calcular_porcentaje (candidatos->at(i), candidatos, votos) << "%\t\t\t|" << endl;
	}
	
	cout << "---------------------------------------------------------------------------------" << endl;
	candidatos_ganadores (candidatos, votos);
}

int calcular_votos (string candidato, vector<string> *candidatos, vector<int> *votos)
{
	int posicion_del_candidato;
	int cantidad_de_votos = 0;
	for (int i = 0; i < candidatos->size (); i++)
	{
		if (candidato == candidatos->at(i))
		{
			posicion_del_candidato = i+1;
			break;
		}
	}
	
	for (int j = 0; j < votos->size (); j++)
	{
		if(votos->at(j) == posicion_del_candidato)
		{
			cantidad_de_votos += 1;
		}
	}
	
	return cantidad_de_votos;
}

float calcular_porcentaje (string candidato, vector<string> *candidatos, vector<int> *votos)
{
	int posicion_del_candidato;
	int cantidad_de_votos = 0;
	float porcentaje;
	for (int i = 0; i < candidatos->size (); i++)
	{
		if (candidato == candidatos->at(i))
		{
			posicion_del_candidato = i+1;
			break;
		}
	}
	
	for (int j = 0; j < votos->size (); j++)
	{
		if(votos->at(j) == posicion_del_candidato)
		{
			cantidad_de_votos += 1;
		}
	}
	
	porcentaje = (cantidad_de_votos * 100.0)/votos->size ();
	
	return porcentaje;
}

void candidatos_ganadores (vector<string> *candidatos, vector<int> *votos)
{
	vector<int> votacion (6, 0);
	for (int i = 0; i < candidatos->size (); i++)
	{
		for (int j = 0; j < votos->size (); j++)
		{
			if ((votos->at(j)-1) == i)
			votacion[i] += 1;
		}
	}
	
	int val1 = 0;
	int val2 = 0;
	
	int indice_del_primero = 0;
	int indice_del_segundo = 0;
	
	for (int k = 0; k < votacion.size (); k++)
	{
		if (votacion[k] > val1)
		{
			val1 = votacion[k];
			indice_del_primero = k;
		}
		else if (votacion[k] > val2)
		{
			val2 = votacion[k];
			indice_del_segundo = k;
		}
	}
	
	cout << "Los ganadores son:" << endl;
	cout << "1er Puesto: " << candidatos->at(indice_del_primero) << endl;
	cout << "2do Puesto: " << candidatos->at(indice_del_segundo) << endl << endl;
}
