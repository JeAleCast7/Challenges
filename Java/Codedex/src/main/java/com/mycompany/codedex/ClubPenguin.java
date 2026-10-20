package com.mycompany.codedex;
import java.util.Scanner;

public class ClubPenguin {
static Scanner sc = new Scanner(System.in);
static int coin;

    public static void Club_Penguin(){
        System.out.println("Insert the amount of Penguin Coins you got");
        coin = sc.nextInt();
        double usd = coin * 0.0045;
        
        System.out.println("You have: " + usd + " USD in Coins!");
    }
}
