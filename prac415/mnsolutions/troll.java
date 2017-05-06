import java.util.Scanner;

public class troll{
    public static int solve(int b, int k, int g){
        --b;
        int ret = 0;
        while(b > 0){
            b -= (k/g);
            ret++;
        }
        return ret;
    }

    public static void main(String[] args){
        Scanner inp = new Scanner(System.in);

        int b = inp.nextInt();
        int k = inp.nextInt();
        int g = inp.nextInt();

        System.out.printf("%d",solve(b,k,g));
    }

}
