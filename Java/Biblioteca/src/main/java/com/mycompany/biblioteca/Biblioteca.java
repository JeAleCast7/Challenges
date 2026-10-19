/*
 * Visit my Repo:https://github.com/JeAleCast7
 */

package com.mycompany.biblioteca;
import java.util.Scanner;


public class Biblioteca {
static Scanner sc = new Scanner(System.in);
static int opc;
static String correo = "";
static String pwd = "";
    
    public static void main(String[] args) {
        menu();
    }
    public static void menu(){
        System.out.println("==============================================");
        System.out.println("    BIENVENIDO A LA BILBLIOTECA DISTRITAL     ");
        System.out.println("==============================================");
        System.out.println("1. INGRESAR");
        System.out.println("2. CONSULTA");
        System.out.println("3. SALIR \n");
        opc = sc.nextInt();
        
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
    }
    

}
