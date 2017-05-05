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
public class Materia extends JFrame{
    
    protected JLabel LblCodigo;
    protected JTextField TxtCodigo;
    protected JLabel LblNombre;
    protected JTextField TxtNombre;
    protected JLabel LblAccion;
    protected JComboBox CmbAccion;
    protected JButton BtnAccion;
    
    public Materia ()
    {
        this.setTitle ("Materia");
        this.setSize (300, 300);
        Dimension ss = Toolkit.getDefaultToolkit().getScreenSize();
        this.setLocation((ss.width/2) - (this.getWidth()/2), (ss.height/2) - (this.getHeight()/2));
        this.setLayout (null);
        this.setResizable (false);
        this.setDefaultCloseOperation (JFrame.HIDE_ON_CLOSE);
        
        this.LblCodigo = new JLabel ("Código");
        this.LblCodigo.setSize(250, 24);
        this.LblCodigo.setLocation(25, 12);
        
        this.TxtCodigo = new JTextField ();
        this.TxtCodigo.setSize (250, 24);
        this.TxtCodigo.setLocation(25, 36);
        
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
        
        this.add (this.LblCodigo);
        this.add (this.TxtCodigo);
        this.add (this.LblNombre);
        this.add (this.TxtNombre);
        this.add (this.LblAccion);
        this.add (this.CmbAccion);
        this.add (this.BtnAccion);
    }
    
    private void ActionSql (ActionEvent e)
    {
        String sql = "INSERT INTO `materia` (`codigo_m`, `nombre`) VALUES (%0, \"%1\");".replaceAll("%0", this.TxtCodigo.getText()).replaceAll("%1", this.TxtNombre.getText());
        System.out.println (sql);
    }
}
