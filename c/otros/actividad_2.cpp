#include <iostream>
#include <string>
#include <vector>


using namespace std;

struct estudiante
{
	string nombre;
	char sexo;
	unsigned short int edad;
	unsigned short int peso;
	float altura;
	bool admitido;
};

// computo de admitidos
void computar_admitidos (vector<estudiante> &lista_de_estudiantes)
{
	for (int i = 0; i < lista_de_estudiantes.size (); i++)
	{
		if (lista_de_estudiantes[i].edad >= 15 and lista_de_estudiantes[i].edad <= 18 and lista_de_estudiantes[i].peso >= 73 and lista_de_estudiantes[i].peso <= 110 and lista_de_estudiantes[i].altura >= 1.83)
		{
			lista_de_estudiantes[i].admitido = true;
		}
		else
		{
			lista_de_estudiantes[i].admitido = false;
		}
			
	}
}

// impresion de admitidos
void imprimir_lista_de_admitidos (vector<estudiante> &lista_de_estudiantes)
{
	int admitidos = 0;
	for (int i = 0; i < lista_de_estudiantes.size (); i++)
	{
		if(lista_de_estudiantes[i].admitido)
		{
			admitidos += 1;
		}
	}
	if(admitidos > 0)
	{
		cout << "La cantidad de estudiantes admitidos es: " << admitidos << " la lista es:" << endl;

		for (int i = 0; i < lista_de_estudiantes.size (); i++)
		{
			if (lista_de_estudiantes[i].admitido)
			{
				cout << "Nombre: " << lista_de_estudiantes[i].nombre << endl;
				cout << "Sexo: " << lista_de_estudiantes[i].sexo << endl;
				cout << "Edad: " << lista_de_estudiantes[i].edad << endl;
				cout << "Peso: " << lista_de_estudiantes[i].peso << endl;
				cout << "Altura: " << lista_de_estudiantes[i].altura << endl;
			}
		}
		
		return;
	}
	cout << "Ningún estudiante fue admitido." << endl;
}

//función principal
int main ()
{
	int nro_de_estudiantes;

	cout << "¿Cuantos estudiantes desea admitir?" << endl;
	cin >> nro_de_estudiantes;

	vector<estudiante> lista_de_estudiantes(nro_de_estudiantes);

	for(int i = 0; i < lista_de_estudiantes.size (); i++)
	{
		cin.ignore();
		cout << "Ingrese el nombre del estudiante nro " << i+1 << endl;
		getline(cin, lista_de_estudiantes[i].nombre);
	
		cout << "Ingrese el sexo (F/M) del estudiante nro " << i+1 << endl;
		cin >> lista_de_estudiantes[i].sexo;

		cout << "Ingrese la edad del estudiante nro " << i+1 << endl;
		cin >> lista_de_estudiantes[i].edad;

		cout << "Ingrese el peso (en cifras enteras) del estudiante nro " << i+1 << endl;
		cin >> lista_de_estudiantes[i].peso;

		cout << "Ingrese la altura del estudiante nro " << i+1 << endl;
		cin >> lista_de_estudiantes[i].altura;
	}

	computar_admitidos (lista_de_estudiantes);
	imprimir_lista_de_admitidos (lista_de_estudiantes);
}


