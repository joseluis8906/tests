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
public class Lista {

    protected Nodo cabeza;
    protected int size;
   
    public Lista ()
    {
        this.cabeza = null;
        this.size = 0;
    }
    
    public void Insertar (Nodo n)
    {   
        if (this.cabeza == null)
        {
            this.cabeza = n;
            this.size++;
        }
        else
        {
            Nodo it = this.cabeza;
            
            for (int i = 0; i < this.size-1; i++)
            {
                it = it.siguiente;
            }
            it.siguiente = n;
            this.size++;
        }
    }
    
    public void Imprimir ()
    {   
        Nodo tmp = this.cabeza;
        for (int i = 0; i < this.size; i++)
        {
            System.out.println (tmp.dato.toString());
            tmp = tmp.siguiente;
        }
    }
    
    public static void main(String[] args) 
    {
        // TODO code application logic here
        Lista l = new Lista ();
        l.Insertar(new Nodo(3));
        l.Insertar(new Nodo(4));
        l.Insertar(new Nodo(5));
        l.Insertar(new Nodo(7));
        l.Imprimir();
    }
    
}
