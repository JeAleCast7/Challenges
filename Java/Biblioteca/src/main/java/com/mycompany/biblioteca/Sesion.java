package com.mycompany.biblioteca;

public class Sesion {
    
    private static int cedula;
    private static String nombre;
    private static boolean logueado = false;
    
    public static void iniciar(int cedulaUsuario, String nombreUsuario){
        cedula = cedulaUsuario;
        nombre = nombreUsuario;
        logueado = true;
    }
    
    public static void cerrar(){
        cedula = 0;
        nombre = null;
        logueado = false;
    }
    
    public static boolean estaLogueado() {return logueado;}
    public static int getCedula()        {return cedula;}
    public static String getNombre()     {return nombre;}
    
}
