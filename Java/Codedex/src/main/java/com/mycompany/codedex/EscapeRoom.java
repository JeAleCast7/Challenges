package com.mycompany.codedex;
import java.util.Scanner;

public class EscapeRoom {
static Scanner sc = new Scanner(System.in);
static String ans;

    public static void Escape_Room(){
        
        String riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?";
        System.out.println(riddle);
        ans = sc.nextLine(); 
        
        if (ans.equals("echo")){
        System.out.println("Congratulations!");
        }
        else {
        System.out.println("Nope");
        }
    }
}
