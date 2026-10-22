package com.mycompany.biblioteca;

public class Menu {

    public static String menu() {
        return "=======================================================\n"
             + "                                                       \n"
             + "          Bienvenid@ a la Biblioteca Distrital         \n"
             + "               Francisco Jose de Caldas                \n"
             + "                                                       \n"
             + "=======================================================\n";
    }
    
    public static String menuIngresar(){
        return "=======================================================\n"
             + "                                                       \n"
             + "      Ya eres miembro de la Biblioteca?                 \n"
             + "                                                       \n"
             + "=======================================================\n";
    }
    
    public static String menuInicioSesion(){
        return "==============================================================\n"
             + "                                                              \n"
             + "      Vas a Iniciar Sesion                                    \n"
             + "                                                              \n"
             + "==============================================================\n";
    }
    
    public static String menuRegistro(){
        return "==============================================================\n"
             + "                                                              \n"
             + "      Porfavor llena el formulario de registro                \n"
             + "                                                              \n"
             + "==============================================================\n";
    }
    
    public static String menuPP(){
        String saludo;
        
        if (Sesion.estaLogueado()){
            saludo = "Bienvendid@ " + Sesion.getNombre();
        }
        else {
            saludo = "";
        }
        return "================================================================"
             + "================================================================\n"
             + "                                                                \n"
             + "      Biblioteca Francisco Jose de Caldas                       \n"
             + saludo + "                                                       \n"
             + "                                                                \n"
             + "================================================================"
             + "================================================================\n";
    }
}
