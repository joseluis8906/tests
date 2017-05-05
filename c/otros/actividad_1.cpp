#include <iostream>
#include <vector>

using namespace std;

struct estudiante
{
	string nro_matricula;
	double notas[5];
	double promedio;
};

// computo de promedios
void computar_promedios (vector<estudiante> &lista_de_estudiantes)
{
	for (int i = 0; i < lista_de_estudiantes.size (); i++)
	{
		double sumatoria_de_notas = 0.0;
		for (int j = 0; j < 5; j++)
		{
			sumatoria_de_notas += lista_de_estudiantes[i].notas[j];
		}
		lista_de_estudiantes[i].promedio = sumatoria_de_notas/5.0;
	}
}

// computo de promedios
void computar_reprobados (vector<estudiante> &lista_de_estudiantes)
{
	int reprobados = 0;
	for (int i = 0; i < lista_de_estudiantes.size (); i++)
	{
		if(lista_de_estudiantes[i].promedio < 3.0)
		{
			reprobados += 1;
		}
	}
	if(reprobados > 0)
	{
		cout << "La cantidad de alumnos reprobados es: " << reprobados << endl;
		return;
	}
	cout << "No hay alumnos reprobados" << endl;
}

//función principal
int main ()
{
	int nro_de_estudiantes;

	cout << "Ingrese el numero de estudiantes a calificar" << endl;
	cin >> nro_de_estudiantes;

	vector<estudiante> lista_de_estudiantes(nro_de_estudiantes);

	for(int i = 0; i < lista_de_estudiantes.size (); i++)
	{
		cout << "Ingrese el código de matrícula del estudiante nro " << i+1 << endl;

		cin >> lista_de_estudiantes[i].nro_matricula;

		for (int j = 0; j < 5; j++)
		{
			cout << "Ingrese la nota número " << j+1 << " del estudiante " << lista_de_estudiantes[i].nro_matricula << endl;
			cin >> lista_de_estudiantes[i].notas[j];
		}
	}

	computar_promedios (lista_de_estudiantes);
	computar_reprobados (lista_de_estudiantes);
}


