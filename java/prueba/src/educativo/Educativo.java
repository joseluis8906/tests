/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package educativo;
import java.awt.Dimension;
import java.awt.Rectangle;
import java.awt.Toolkit;
import java.awt.Window;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
/**
 *
 * @author joseluis
 */
public class Educativo extends JFrame {
    
    protected JButton BtnMateria;
    protected JButton BtnProfesor;
    protected JButton BtnCurso;
    protected JButton BtnEstudiante;
    protected JButton BtnMatricula;
    protected JButton BtnNotas;
    
    
    public Educativo ()
    {
        this.setTitle ("Menú Principal");
        this.setSize (300, 512);
        Dimension ss = Toolkit.getDefaultToolkit().getScreenSize();
        this.setLocation((ss.width/2) - (this.getWidth()/2), (ss.height/2) - (this.getHeight()/2));
        this.setLayout (null);
        this.setResizable (false);
        this.setDefaultCloseOperation (JFrame.EXIT_ON_CLOSE);
        
        this.BtnMateria = new JButton (new ImageIcon("area.png"));
        this.BtnMateria.setText("Materia");
        this.BtnMateria.setSize (170, 64);
        this.BtnMateria.setLocation ((this.getWidth()/2)-(this.BtnMateria.getWidth()/2), 12);
        this.BtnMateria.addActionListener(new ActionListener() {
            @Override public void actionPerformed(ActionEvent e) {
                ActionMateria(e);
            }
        });
        
        this.BtnProfesor = new JButton (new ImageIcon("teacher.png"));
        this.BtnProfesor.setText("Profesor");
        this.BtnProfesor.setSize (170, 64);
        this.BtnProfesor.setLocation ((this.getWidth()/2)-(this.BtnProfesor.getWidth()/2), 88);
        this.BtnProfesor.addActionListener(new ActionListener() {
            @Override public void actionPerformed(ActionEvent e) {
                ActionProfesor(e);
            }
        });
        
        this.BtnEstudiante = new JButton (new ImageIcon("student.png"));
        this.BtnEstudiante.setText("Estudiante");
        this.BtnEstudiante.setSize (185, 64);
        this.BtnEstudiante.setLocation ((this.getWidth()/2)-(this.BtnEstudiante.getWidth()/2), 164);
        this.BtnEstudiante.addActionListener(new ActionListener() {
            @Override public void actionPerformed(ActionEvent e) {
                ActionEstudiante(e);
            }
        });
        
        this.BtnCurso = new JButton (new ImageIcon("course.png"));
        this.BtnCurso.setText("Curso");
        this.BtnCurso.setSize (170, 64);
        this.BtnCurso.setLocation ((this.getWidth()/2)-(this.BtnCurso.getWidth()/2), 240);
        this.BtnCurso.addActionListener(new ActionListener() {
            @Override public void actionPerformed(ActionEvent e) {
                ActionCurso(e);
            }
        });
        
        this.BtnMatricula = new JButton (new ImageIcon("books.png"));
        this.BtnMatricula.setText("Matricula");
        this.BtnMatricula.setSize (170, 64);
        this.BtnMatricula.setLocation ((this.getWidth()/2)-(this.BtnMatricula.getWidth()/2), 316);
        this.BtnMatricula.addActionListener(new ActionListener() {
            @Override public void actionPerformed(ActionEvent e) {
                ActionMatricula(e);
            }
        });
        
        this.BtnNotas = new JButton (new ImageIcon("qualification.png"));
        this.BtnNotas.setText("Notas");
        this.BtnNotas.setSize (170, 64);
        this.BtnNotas.setLocation ((this.getWidth()/2)-(this.BtnNotas.getWidth()/2), 392);
        this.BtnNotas.addActionListener(new ActionListener() {
            @Override public void actionPerformed(ActionEvent e) {
                ActionNota(e);
            }
        });
        
        this.add(this.BtnMateria);
        this.add(this.BtnProfesor);
        this.add(this.BtnEstudiante);
        this.add(this.BtnCurso);
        this.add(this.BtnMatricula);
        this.add(this.BtnNotas);
        
    }
    
    private void ActionMateria (ActionEvent e)
    {
        Materia frame = new Materia ();
        frame.setVisible(true);
    }
    
    private void ActionProfesor (ActionEvent e)
    {
        Profesor frame = new Profesor ();
        frame.setVisible(true);
    }
    
    private void ActionEstudiante (ActionEvent e)
    {
        Estudiante frame = new Estudiante ();
        frame.setVisible(true); 
    }
    
    private void ActionCurso (ActionEvent e)
    {
        Curso frame = new Curso ();
        frame.setVisible(true); 
    }
    
    private void ActionMatricula (ActionEvent e)
    {
        Matricula frame = new Matricula ();
        frame.setVisible(true); 
    }
    
    private void ActionNota (ActionEvent e)
    {
        Nota frame = new Nota ();
        frame.setVisible(true); 
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        Educativo frame = new Educativo ();
        frame.setVisible(true);
        
        
    }
}
