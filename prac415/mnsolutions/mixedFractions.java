import java.util.Scanner;

public class mixedFractions{
    public static void main(String[] args){
        Scanner inp = new Scanner(System.in);
        int a,b;
        do{
            a = inp.nextInt();
            b = inp.nextInt();
            System.out.printf("%d %d\n",a/b,a%b);
        } while(a != 0 && b != 0);
    }
}
