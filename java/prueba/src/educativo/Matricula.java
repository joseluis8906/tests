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
public class Matricula extends JFrame{
    
    protected JLabel LblCurso;
    protected JComboBox CmbCurso;
    protected JLabel LblDocuEstudiante;
    protected JTextField TxtDocuEstudiante;
    protected JLabel LblAccion;
    protected JComboBox CmbAccion;
    protected JButton BtnAccion;
    
    public Matricula ()
    {
        this.setTitle ("Matricula");
        this.setSize (300, 320);
        Dimension ss = Toolkit.getDefaultToolkit().getScreenSize();
        this.setLocation((ss.width/2) - (this.getWidth()/2), (ss.height/2) - (this.getHeight()/2));
        this.setLayout (null);
        this.setResizable (false);
        this.setDefaultCloseOperation (JFrame.HIDE_ON_CLOSE);
        
        this.LblCurso = new JLabel ("Curso");
        this.LblCurso.setSize(250, 24);
        this.LblCurso.setLocation(25, 12);
        
        String[] cursos = {"Curso 1", "Curso 2", "Curso 3"};
        this.CmbCurso = new JComboBox (cursos);
        this.CmbCurso.setSize (250, 24);
        this.CmbCurso.setLocation(25, 36);
        
        this.LblDocuEstudiante = new JLabel ("Documento Estudiante");
        this.LblDocuEstudiante.setSize (250, 24);
        this.LblDocuEstudiante.setLocation (25, 72);
        
        this.TxtDocuEstudiante = new JTextField ();
        this.TxtDocuEstudiante.setSize (250, 24);
        this.TxtDocuEstudiante.setLocation(25, 108);
        
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
        
        this.add (this.LblCurso);
        this.add (this.CmbCurso);
        this.add (this.LblDocuEstudiante);
        this.add (this.TxtDocuEstudiante);
        this.add (this.LblAccion);
        this.add (this.CmbAccion);
        this.add (this.BtnAccion);
    }
    
    private void ActionSql (ActionEvent e)
    {
        
    }
}
