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
public class Profesor extends JFrame {
    
    protected JLabel LblDocumento;
    protected JTextField TxtDocumento;
    protected JLabel LblNombre;
    protected JTextField TxtNombre;
    protected JLabel LblAccion;
    protected JComboBox CmbAccion;
    protected JButton BtnAccion;
    
    public Profesor ()
    {
        this.setTitle ("Profesor");
        this.setSize (300, 300);
        Dimension ss = Toolkit.getDefaultToolkit().getScreenSize();
        this.setLocation((ss.width/2) - (this.getWidth()/2), (ss.height/2) - (this.getHeight()/2));
        this.setLayout (null);
        this.setResizable (false);
        this.setDefaultCloseOperation (JFrame.HIDE_ON_CLOSE);
        
        this.LblDocumento = new JLabel ("Documento");
        this.LblDocumento.setSize(250, 24);
        this.LblDocumento.setLocation(25, 12);
        
        this.TxtDocumento = new JTextField ();
        this.TxtDocumento.setSize (250, 24);
        this.TxtDocumento.setLocation(25, 36);
        
        this.LblNombre = new JLabel ("Nombre");
        this.LblNombre.setSize (250, 24);
        this.LblNombre.setLocation (25, 72);
        
        this.TxtNombre = new JTextField ();
        this.TxtNombre.setSize (250, 24);
        this.TxtNombre.setLocation(25, 108);
        
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
        
        this.add (this.LblDocumento);
        this.add (this.TxtDocumento);
        this.add (this.LblNombre);
        this.add (this.TxtNombre);
        this.add (this.LblAccion);
        this.add (this.CmbAccion);
        this.add (this.BtnAccion);
    }
    
    private void ActionSql (ActionEvent e)
    {
        
    }
}
