package com.company;

import java.util.Scanner;

public class Main{

    public static void main(String[] args) {

        Scanner vvod = new Scanner(System.in);
        int a = vvod.nextInt();
        int b = vvod.nextInt();
        int c = vvod.nextInt();

        if ((b == 0) && (c == 0)){
            System.out.println(0);
            return;
        }

        double kol = (double)(a) / (b + c);

        if (kol == (int)(kol)){
            kol -= 1;
        }
        else{
            kol = (int)(a / (b + c));
        }
        int rezult = 1;

        int min_ch = Math.min(b, c);
        int max_ch = Math.max(b, c);
        int pr_min = 0;
        int pr_max = 0;
        int kon = 0;

        for (int i = 0; i < kol; i++){
            pr_min += min_ch;
            pr_max += max_ch;

            kon = (int)((pr_max - pr_min) / (max_ch - min_ch));
            kon += 1;

            rezult += kon;

        }
        System.out.println(rezult);
    }

}
