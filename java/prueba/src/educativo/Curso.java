/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package educativo;
import java.awt.Dimension;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
/**
 *
 * @author joseluis
 */
public class Curso extends JFrame{
    
    protected JLabel LblDocuDocente;
    protected JTextField TxtDocuDocente;
    protected JLabel LblCodMateria;
    protected JTextField TxtCodMateria;
    protected JLabel LblAccion;
    protected JComboBox CmbAccion;
    protected JButton BtnAccion;
    
    public Curso ()
    {
        this.setTitle ("Curso");
        this.setSize (300, 320);
        Dimension ss = Toolkit.getDefaultToolkit().getScreenSize();
        this.setLocation((ss.width/2) - (this.getWidth()/2), (ss.height/2) - (this.getHeight()/2));
        this.setLayout (null);
        this.setResizable (false);
        this.setDefaultCloseOperation (JFrame.HIDE_ON_CLOSE);
        
        this.LblDocuDocente = new JLabel ("Documento Docente");
        this.LblDocuDocente.setSize(250, 24);
        this.LblDocuDocente.setLocation(25, 12);
        
        this.TxtDocuDocente = new JTextField ();
        this.TxtDocuDocente.setSize (250, 24);
        this.TxtDocuDocente.setLocation(25, 36);
        
        this.LblCodMateria = new JLabel ("Código Materia");
        this.LblCodMateria.setSize (250, 24);
        this.LblCodMateria.setLocation (25, 72);
        
        this.TxtCodMateria = new JTextField ();
        this.TxtCodMateria.setSize (250, 24);
        this.TxtCodMateria.setLocation(25, 108);
        
        this.LblAccion = new JLabel ("Acción");
        this.LblAccion.setSize (250, 24);
        this.LblAccion.setLocation (25, 144);
        
        String[] acciones = {"Guardar", "Actualizar", "Eliminar", "Buscar"};
        this.CmbAccion = new JComboBox (acciones);
        this.CmbAccion.setSize(250, 24);
        this.CmbAccion.setLocation(25, 180);
        
        this.BtnAccion = new JButton ("Ejecutar");
        this.BtnAccion.setSize (128, 24);
        this.BtnAccion.setLocation(25, 228);
        this.BtnAccion.addActionListener(new ActionListener() {
            @Override public void actionPerformed(ActionEvent e) {
                ActionSql(e);
            }
        });
        
        this.add (this.LblDocuDocente);
        this.add (this.TxtDocuDocente);
        this.add (this.LblCodMateria);
        this.add (this.TxtCodMateria);
        this.add (this.LblAccion);
        this.add (this.CmbAccion);
        this.add (this.BtnAccion);
    }
    
    private void ActionSql (ActionEvent e)
    {
        
    }
}
