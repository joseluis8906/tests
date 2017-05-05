#include <random>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <ctime>
#include <cppdb/frontend.h>

cppdb::session sql("sqlite3:db=db.sqlite");

typedef std::vector<std::string> muestra;

int db_count ()
{
	int total;
	cppdb::result result = sql << "SELECT COUNT(*) AS total FROM sorteo";
	result.next ();
	if (!result.empty ())
	{
		total = result.get<int>("total");
		return total;
	}
	total = 0;
	return total;
}

void db_select (muestra *numeros)
{
	numeros->clear ();
	cppdb::result result = sql << "SELECT numero FROM sorteo";
	while (result.next ())
	{
		numeros->push_back(result.get<std::string>("numero"));
	}
}

void db_insert (std::string numero)
{
	cppdb::statement st = sql << "INSERT INTO sorteo(numero) VALUES(?)" << numero << cppdb::exec;
}

void db_clean ()
{
	cppdb::statement st = sql << "DELETE FROM sorteo WHERE id>?" << 0 << cppdb::exec;
}

void agregar_nuevo (muestra *numeros)
{
	std::string registro;
	std::cout << "ingrese el numero" << std::endl;
	std::cin >> registro;
	std::cin.sync ();
	std::cin.get ();
	
	if (registro.size () != 4)
	{
		std::cout << "Error: numero mayor o menor de 4 cifras" << std::endl;
		std::cin.get ();
	}
	else
	{
		if (db_count ()==1000)
		{
			cppdb::result result = sql << "SELECT id FROM sorteo";
			result.next ();
			if (!result.empty ())
			{
				cppdb::statement st = sql << "DELETE FROM sorteo WHERE id=?" << result.get<int>("id") << cppdb::exec;	
			}
		}
		db_insert (registro);
		db_select (numeros);
	}
}

void generar_numeros (muestra *numeros)
{
	
	std::time_t t;
	std::time (&t);
	unsigned int seed = (unsigned int) t;
	
	std::default_random_engine random_engine (seed);
	
	std::uniform_int_distribution<int> integer_distribution (0,9);
	
	for (int i=0; i < numeros->size (); ++i)
	{
		numeros->at(i) = "";
		for (int j=0; j<4; ++j)
		{	
			numeros->at(i) += std::to_string(integer_distribution (random_engine));
		}
	}
}

void imprimir_numeros (muestra *numeros)
{
	muestra::iterator it;
	
	for (it = numeros->begin (); it < numeros->end ();  ++it)
	{
		std::cout << *it << std::endl;
	}
}

void inicializar_db (muestra *numeros)
{
	db_clean ();
	generar_numeros (numeros);
	
	muestra::iterator it;
	for (it = numeros->begin (); it < numeros->end ();  ++it)
	{
		db_insert(*it);
	}
	
}


void consultar_estadisticas (muestra *numeros)
{
	db_select (numeros);
	imprimir_numeros (numeros);
	unsigned int tamanio = numeros->size ();
	
	struct cifra {
		unsigned int cero;
		unsigned int uno;
		unsigned int dos;
		unsigned int tres;
		unsigned int cuatro;
		unsigned int cinco;
		unsigned int seis;
		unsigned int siete;
		unsigned int ocho;
		unsigned int nueve;
		
		cifra ()
		{
			this->cero = 0;
			this->uno = 0;
			this->dos = 0;
			this->tres = 0;
			this->cuatro = 0;
			this->cinco = 0;
			this->seis = 0;
			this->siete = 0;
			this->ocho = 0;
			this->nueve = 0;
		}
	};
	
	cifra primera = cifra ();
	cifra segunda = cifra ();
	cifra tercera = cifra ();
	cifra cuarta = cifra ();
	
	muestra::iterator it;
	for (it = numeros->begin (); it < numeros->end (); ++it)
	{
		switch (it->at(0))
		{
			case '0':
				primera.cero++;
				break;
				
			case '1':
				primera.uno++;
				break;
				
			case '2':
				primera.dos++;
				break;
				
			case '3':
				primera.tres++;
				break;
				
			case '4':
				primera.cuatro++;
				break;
				
			case '5':
				primera.cinco++;
				break;
				
			case '6':
				primera.seis++;
				break;	
				
			case '7':
				primera.siete++;
				break;
			
			case '8':
				primera.ocho++;
				break;
			
			case '9':
				primera.nueve++;
				break;
				
			default:
				break;
		}
		
		switch (it->at(1))
		{
			case '0':
				segunda.cero++;
				break;
				
			case '1':
				segunda.uno++;
				break;
				
			case '2':
				segunda.dos++;
				break;
				
			case '3':
				segunda.tres++;
				break;
				
			case '4':
				segunda.cuatro++;
				break;
				
			case '5':
				segunda.cinco++;
				break;
				
			case '6':
				segunda.seis++;
				break;	
				
			case '7':
				segunda.siete++;
				break;
			
			case '8':
				segunda.ocho++;
				break;
			
			case '9':
				segunda.nueve++;
				break;
				
			default:
				break;
		}
		
		switch (it->at(2))
		{
			case '0':
				tercera.cero++;
				break;
				
			case '1':
				tercera.uno++;
				break;
				
			case '2':
				tercera.dos++;
				break;
				
			case '3':
				tercera.tres++;
				break;
				
			case '4':
				tercera.cuatro++;
				break;
				
			case '5':
				tercera.cinco++;
				break;
				
			case '6':
				tercera.seis++;
				break;	
				
			case '7':
				tercera.siete++;
				break;
			
			case '8':
				tercera.ocho++;
				break;
			
			case '9':
				tercera.nueve++;
				break;
				
			default:
				break;
		}
		
		switch (it->at(3))
		{
			case '0':
				cuarta.cero++;
				break;
				
			case '1':
				cuarta.uno++;
				break;
				
			case '2':
				cuarta.dos++;
				break;
				
			case '3':
				cuarta.tres++;
				break;
				
			case '4':
				cuarta.cuatro++;
				break;
				
			case '5':
				cuarta.cinco++;
				break;
				
			case '6':
				cuarta.seis++;
				break;	
				
			case '7':
				cuarta.siete++;
				break;
			
			case '8':
				cuarta.ocho++;
				break;
			
			case '9':
				cuarta.nueve++;
				break;
				
			default:
				break;
		}
	}
	std::cout << std::endl;
	std::cout << "Cantidad de numeros: " << tamanio << std::endl << std::endl;
	
	std::cout << "-----------------------------------------------------------------" << std::endl;
	std::cout << "                            Tabla estadistica                    " << std::endl;
	std::cout << "-----------------------------------------------------------------" << std::endl;
	std::cout << std::setw (9) << std::setfill (' ') << "|" << std::setw (14) << std::setfill (' ') << "cifra 1|" << 
				 std::setw(14) << std::setfill (' ') << "cifra 2|" << std::setw (14) << std::setfill (' ') << "cifra 3|" <<
				 std::setw (14) << std::setfill (' ') << "cifra 4" << std::endl;
	std::cout << "-----------------------------------------------------------------" << std::endl;
	
	std::cout << std::setw (9) << std::setfill (' ') << "cero|" << std::setw(12) << std::setfill (' ') << std::setprecision (4) << (primera.cero/(float)tamanio)*100 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(segunda.cero/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(tercera.cero/(float)tamanio)*100.0 << "%|" 
			  << std::setw(13) << std::setfill (' ') << std::setprecision (4) <<(cuarta.cero/(float)tamanio)*100.0 << "%" << std::endl;

	std::cout << std::setw (9) << std::setfill (' ') << "uno|" << std::setw(12) << std::setfill (' ') << std::setprecision (4) << (primera.uno/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(segunda.uno/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(tercera.uno/(float)tamanio)*100.0 << "%|" 
			  << std::setw(13) << std::setfill (' ') << std::setprecision (4) <<(cuarta.uno/(float)tamanio)*100.0 << "%" <<  std::endl;
			  
	std::cout << std::setw (9) << std::setfill (' ') << "dos|" << std::setw(12) << std::setfill (' ') << std::setprecision (4) << (primera.dos/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(segunda.dos/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(tercera.dos/(float)tamanio)*100.0 << "%|" 
			  << std::setw(13) << std::setfill (' ') << std::setprecision (4) <<(cuarta.dos/(float)tamanio)*100.0 << "%" << std::endl;
			  
	std::cout << std::setw (9) << std::setfill (' ') << "tres|" << std::setw(12) << std::setfill (' ') << std::setprecision (4) << (primera.tres/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(segunda.tres/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(tercera.tres/(float)tamanio)*100.0 << "%|" 
			  << std::setw(13) << std::setfill (' ') << std::setprecision (4) <<(cuarta.tres/(float)tamanio)*100.0 << "%" << std::endl;
			  
	std::cout << std::setw (9) << std::setfill (' ') << "cuatro|" << std::setw(12) << std::setfill (' ') << std::setprecision (4) << (primera.cuatro/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(segunda.cuatro/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(tercera.cuatro/(float)tamanio)*100.0 << "%|" 
			  << std::setw(13) << std::setfill (' ') << std::setprecision (4) <<(cuarta.cuatro/(float)tamanio)*100.0 << "%" << std::endl;
			  
	std::cout << std::setw (9) << std::setfill (' ') << "cinco|" << std::setw(12) << std::setfill (' ') << std::setprecision (4) << (primera.cinco/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(segunda.cinco/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(tercera.cinco/(float)tamanio)*100.0 << "%|" 
			  << std::setw(13) << std::setfill (' ') << std::setprecision (4) <<(cuarta.cinco/(float)tamanio)*100.0 << "%" << std::endl;
			  
	std::cout << std::setw (9) << std::setfill (' ') << "seis|" << std::setw(12) << std::setfill (' ') << std::setprecision (4) << (primera.seis/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(segunda.seis/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(tercera.seis/(float)tamanio)*100.0 << "%|" 
			  << std::setw(13) << std::setfill (' ') << std::setprecision (4) <<(cuarta.seis/(float)tamanio)*100.0 << "%" << std::endl;
			  
	std::cout << std::setw (9) << std::setfill (' ') << "siete|" << std::setw(12) << std::setfill (' ') << std::setprecision (4) << (primera.siete/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(segunda.siete/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(tercera.siete/(float)tamanio)*100.0 << "%|" 
			  << std::setw(13) << std::setfill (' ') << std::setprecision (4) <<(cuarta.siete/(float)tamanio)*100.0 << "%" << std::endl;
			  
	std::cout << std::setw (9) << std::setfill (' ') << "ocho|" << std::setw(12) << std::setfill (' ') << std::setprecision (4) << (primera.ocho/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(segunda.ocho/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(tercera.ocho/(float)tamanio)*100.0 << "%|" 
			  << std::setw(13) << std::setfill (' ') << std::setprecision (4) <<(cuarta.ocho/(float)tamanio)*100.0 << "%" << std::endl;
			  
	std::cout << std::setw (9) << std::setfill (' ') << "nueve|" << std::setw(12) << std::setfill (' ') << std::setprecision (4) << (primera.nueve/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(segunda.nueve/(float)tamanio)*100.0 << "%|" 
			  << std::setw(12) << std::setfill (' ') << std::setprecision (4) <<(tercera.nueve/(float)tamanio)*100.0 << "%|" 
			  << std::setw(13) << std::setfill (' ') << std::setprecision (4) <<(cuarta.nueve/(float)tamanio)*100.0 << "%" << std::endl;
}

int main (int argc, char *argv[])
{
	muestra numeros;
	
	bool salir = false;
	
	while (!salir)
	{
		std::cout << "1). inicializar base de datos" << std::endl;
		std::cout << "2). agregar registro" << std::endl;
		std::cout << "3). consultar estadisticas" << std::endl;
		std::cout << "4). salir" << std::endl;
		
		int input;
		std::cin >> input;
		std::cin.sync ();
		std::cin.get ();
		
		switch (input)
		{
			case 1:
				std::cout << "Advertencia: borrará todos los datos, desea continuar s/n" << std::endl;
				char input;
				std::cin >> input;
				std::cin.sync ();
				std::cin.get ();
				switch (input)
				{
					case 's':
						inicializar_db (&numeros);
						break;
					case 'n':
						break;
					default:
						std::cout << "Respesta incorrecta" << std::endl;
						break;
				}
				break;
			
			case 2:
				agregar_nuevo (&numeros);
				break;
			
			case 3:
				consultar_estadisticas (&numeros);
				std::cout << std::endl;
				break;
				
			case 4:
				salir = true;
				std::cout << "Adios!" << std::endl;
				break;
				
			default:
				std::cout << "Error de numero" << std::endl;
				break;
		}
	}
}