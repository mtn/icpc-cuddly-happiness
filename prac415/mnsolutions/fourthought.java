import java.util.Scanner;

public class fourthought{
    public static void main(String[] args){
        Scanner inp = new Scanner(System.in);
        int numTrials = inp.nextInt();
        int[][][] lookup = new int[4][4][4];
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                for(int k = 0; k < 4; k++){
                    int temp = 4;
                    switch(i){
                        case 0:
                            temp *= 4;
                            break;
                        case 1:
                            temp += 4;
                            // better in python with eval...
                    }
                }
            }
        }
        for(int i = 0; i < numTrials; i++){
            
        }
    }
}
