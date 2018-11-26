package com.company;

import java.util.Scanner;

public class Main{

    public static void main(String[] args) {

        Scanner vvod = new Scanner(System.in);
        int a = vvod.nextInt();

        for (int g = 0; g < a; g ++){
            int mill = vvod.nextInt();
            String m = vvod.nextLine();
            String[] vars = m.split(" ", 3);
            String fir = vars[1];
            String sec = vars[2];

            int min_st = Math.min(fir.length(), sec.length());
            boolean f = false;
            for(int i = 0; i < min_st; i++){
                if (fir.charAt(i) != sec.charAt(i)){
                    f = true;
                    mill -= min_st - i;
                    mill -= sec.length() - i;
                    if ((mill >= 0)&&(mill % 2 == 0)){
                        System.out.println("Yes");
                    }
                    else{
                        System.out.println("No");
                    }
                    break;
                }
            }
            if(f == false){
                mill -= Math.max(fir.length(), sec.length()) - min_st;

                if ((mill >= 0)&&(mill % 2 == 0)){
                    System.out.println("Yes");
                }
                else{
                    System.out.println("No");
                }
            }
        }

    }

}
