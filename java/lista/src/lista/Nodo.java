/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lista;

/**
 *
 * @author joseluis
 */
public class Nodo <T>
{
    protected T dato;
    protected Nodo siguiente;
    
    public Nodo ()
    {
        this.dato = null;
        this.siguiente = null;
    }
    
    public Nodo (T dato)
    {
        this.dato = dato;
        this.siguiente = null;
    }
    
}
