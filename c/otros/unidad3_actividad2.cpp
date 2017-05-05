#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

float calcular_promedio_general_del_curso (vector< vector<float> >*);
void calcular_promedio_por_hilera (vector < vector <float> >*);
void calcular_nota_maxima_y_minima (vector < vector <float> >*);
void imprimir_curso_y_notas (vector < vector <float> >*);
int calcular_aprobados (vector < vector <float> >*);

int main (int argc, char *argv[])
{
	int numero_de_hileras;
	cout << "Ingrese el número de hileras del curso:" << endl;
	cin >> numero_de_hileras;
	
	int numero_de_estudiantes_por_hilera;
	cout << "Ingrese el número de estudiantes por hilera:" << endl;
	cin >> numero_de_estudiantes_por_hilera;
	
	vector< vector<float> > curso (numero_de_estudiantes_por_hilera, vector<float> (numero_de_hileras));
	
	for (int i = 0; i < curso[0].size (); i++)
	{
		for (int j = 0; j < curso.size (); j++)
		{
			cout << "Ingrese la nota(0.0 ... 5.0) del estudiante " << j+1 << " de la hilera " << i+1 << endl;
			cin >> curso[j][i];
		}
	}
	
	cout << "El promedio general del curso es " << fixed << setprecision(2) << calcular_promedio_general_del_curso (&curso) << endl;
	cout << "Los promedio por fila son: " << endl;
	calcular_promedio_por_hilera (&curso);
	calcular_nota_maxima_y_minima (&curso);
	imprimir_curso_y_notas (&curso);
	cout << "\nLa cantidad de estudiantes que aprobaron fueron " << calcular_aprobados (&curso) << " estudiantes." << endl;
}

float calcular_promedio_general_del_curso (vector< vector<float> > *curso)
{
	float promedio, sumatoria = 0.0;
	int filas = curso->size (), estudiantes_por_fila = curso->at (0).size ();
	
	for (int i = 0; i < filas; i++)
	{
		for (int j = 0; j < estudiantes_por_fila; j++)
		{
			sumatoria += curso->at (i)[j];
		}
	}

	promedio = float(sumatoria)/(filas*estudiantes_por_fila);
	return promedio;
}

void calcular_promedio_por_hilera (vector < vector<float> > *curso)
{
	float promedio_hilera, sumatoria_hilera;
	int hileras = curso->at(0).size (), estudiantes_por_hilera = curso->size ();
	
	for (int i = 0; i < hileras; i++)
	{
		promedio_hilera = 0.0;
		sumatoria_hilera = 0.0;

		for (int j = 0; j < estudiantes_por_hilera; j++)
		{
			sumatoria_hilera += curso->at(j)[i];
		}
		
		promedio_hilera = float(sumatoria_hilera)/estudiantes_por_hilera;
		cout << "El promedio de la hilera " << i+1 << " es " << fixed << setprecision(2) << promedio_hilera << endl;
	}
}

void calcular_nota_maxima_y_minima (vector < vector <float> > *curso)
{
	float maximo = 0.0;
	int coordenadas_maximo[2];
	float minimo = 0.0;
	int coordenadas_minimo[2];
	int hileras = curso->at(0).size (), estudiantes_por_hilera = curso->size ();
	
	for (int i = 0; i < hileras; i++)
	{
		for (int j = 0; j < estudiantes_por_hilera; j++)
		{
			if (i==0 and j==0)
			{
				minimo = curso->at(j)[i];
				coordenadas_minimo[0] = i + 1;
				coordenadas_minimo[1] = j + 1;
			}
			
			if (curso->at(j)[i] > maximo)
			{
				maximo = curso->at(j)[i];
				coordenadas_maximo[0] = i + 1;
				coordenadas_maximo[1] = j + 1;
			}
			
			if (curso->at(j)[i] < minimo)
			{
				minimo = curso->at(j)[i];
				coordenadas_minimo[0] = i + 1;
				coordenadas_minimo[1] = j + 1;
			}
		}		
	}
	
	cout << "El estudiante con la calificación mas alta fue el de la hilera " << coordenadas_maximo[0] << " puesto " << coordenadas_maximo[1] << ", la nota fue " << maximo << endl;
	cout << "El estudiante con la calificación mas baja fue el de la hilera " << coordenadas_minimo[0] << " puesto " << coordenadas_minimo[1] << ", la nota fue " << minimo << endl;
}

void imprimir_curso_y_notas (vector < vector<float> > *curso)
{
	int filas = curso->size (), estudiante_por_fila = curso->at(0).size ();
	for (int i = 0; i < filas; i++)
	{
		for (int j = 0; j < estudiante_por_fila; j++)
		{
			cout << "(" << j+1 << "," << i+1 << ")(" << curso->at(i)[j] << ")" << "  ";
		}
		cout << endl;
	}
}

int calcular_aprobados (vector < vector<float> > *curso)
{
	int aprobados = 0;
	int filas = curso->size (), estudiante_por_fila = curso->at(0).size ();
	for (int i = 0; i < filas; i++)
	{
		for (int j = 0; j < estudiante_por_fila; j++)
		{
			if (curso->at (i)[j] >= 3.0)
			{
				aprobados += 1;
			}
		}
	}	
	return aprobados;
}
