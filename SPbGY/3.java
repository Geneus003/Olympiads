

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
        long rezult = 0;

        int min_ch = Math.min(b, c);
        int max_ch = Math.max(b, c);
        int pr_min = 0;
        int pr_max = 0;
        int kon = 0;

        if (min_ch == max_ch){
          double koll = (double)(a) / (b + c);
          if (koll == (int)(koll)){
            System.out.println((int)(koll));
          }
          else{
            System.out.println((int)(koll) + 1);
          }
          return;
        }

        

        for (int i = 0; i <= kol + 1; i++){

            rezult += i;

        }
        System.out.println(rezult);
    }

}
