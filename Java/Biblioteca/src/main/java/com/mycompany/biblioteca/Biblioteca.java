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
        /*
        switch (opc){
            case 1: 
                System.out.println("Ya eres miembro?");
                System.out.println("1. Iniciar Sesion");
                System.out.println("2. Registrarse");
                System.out.println("3. salir");
                opc = sc.nextInt();
                
                switch (opc) {
                    case 1:
                        System.out.println("Porfavor digita lo siguiente:");
                        System.out.println("Correo: ");
                        String correo = sc.next();
                        System.out.println("Password: ");
                        String pwd = sc.next(); 
                        
                        Ingresar ingresar = new Ingresar();
                        Boolean acceso = ingresar.validar(correo, pwd);
                        
                        if (acceso = true){
                            System.out.println("Bienvenid@ " + correo);
                        }
                        
                        else
                            System.out.println("Usuario no encontrado ");
                    case 2:
                };
        }
        */
    }
    

