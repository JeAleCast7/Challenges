/*
 * Visit my Repo:https://github.com/JeAleCast7
 */
package com.mycompany.biblioteca;
import javax.swing.SwingUtilities;

public class Biblioteca {
    /*
static String correo = "";
static String pwd = "";
    */
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new BibliotecaVentana().setVisible(true));
    }  
}
    

