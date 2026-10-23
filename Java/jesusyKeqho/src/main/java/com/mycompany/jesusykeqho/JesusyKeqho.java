/*
Variables y Constantes globales y locales
menu
funciones metodos
matrices, vectores
*/
package com.mycompany.jesusykeqho;
import java.util.Scanner;
//import javax.swing.SwingUtilities;

public class JesusyKeqho {
// static is for use the variable globally otherwise the code won't reconginze it
static Scanner sc = new Scanner(System.in);
static int[] vec = new int[4];
static String opc;
static int fil = 0 , col = 0;
static int[][] math = new int [fil][col];


//static final is for state what is inside as constant
//static final int TAM = 0;

    public static void main(String[] args) {
        //SwingUtilities.invokeLater(() -> new MenuVentana().setVisible(true));
        menu();
    }
    
    public static void menu() {
        System.out.println("===============================");
        System.out.println("         MENU PRINCIPAL        ");
        System.out.println("===============================");
        System.out.println("1. VECTORES");
        System.out.println("2. MATRICES");
        System.out.println("3. SALIR");
        System.out.println("Digite su opcion: ");
        opc = sc.next();
        
        switch (opc) {
            case "1": 
                vector();
                break;
            case "2":
                matriz();
                break;
            case "3":
                break;
            default:
                throw new AssertionError();
        }
    }
    
    public static void vector() {
        for (int i = 0; i <= 3; i++) {
            System.out.println("Digite el valor de posicion " + i + "\n" );
            vec[i] = sc.nextInt();
        }
        menu();
    }
    
    public static void matriz() {
        
        int fil = 0 , col = 0;
        
        System.out.println("Ingrese Filas: ");
        fil = sc.nextInt();
        
        System.out.println("Ingrese columnas: ");
        col = sc.nextInt();
        
        int[][] math = new int [fil][col];
        
        for (fil = 0; fil < math.length; fil++) {
            for (col = 0; col < math[fil].length; col++) {
                System.out.println("Digite el valor [" + fil + "]" + "[" + col + "]");
                math[fil][col] = sc.nextInt();
                
            }
            
        } 
        System.out.println("La matriz es:");
        for (int i = 0; i < math.length; i++) {
                for (int j = 0; j < math[i].length; j++) {
                    System.out.print(math[i][j] + "\t");   
                }
            System.out.println();
        }
}
}
 