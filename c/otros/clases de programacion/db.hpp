#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <string>
#include <fstream>
#include <boost/algorithm/string.hpp>

#ifndef INCLUDE_DB_HPP
#define INCLUDE_DB_HPP


void nuevo_registro ();
void eliminar_registro ();
void actualizar_registro ();
void buscar_registro ();
void imprimir_registros ();
void cargar_datos ();
void guardar_datos ();
int verificar_cedula (std::string);

#endif
