import java.util.Scanner;

public class queens{
    public static void main(String[] args){
        Scanner inp = new Scanner(System.in);
        int dim = inp.nextInt();          
        boolean[][] board = new boolean[dim][dim];
        int a, b;
        for(int i = 0; i < dim; i++){
            a = inp.nextInt();
            b = inp.nextInt();
            board[a][b] = true;
        }
        boolean valid = true;

        for(int i = 0; i < dim; i++){
            for(int j = 0; j < dim; j++){
                if(!board[i][j]) continue;
                else{
                    for(int k = -dim; k < dim; k++){
                        if(k > 0){
                            if(board[k][j] && k != i){
                                valid = false;
                            }
                            if(board[i][k] && k != j){
                                valid = false;
                            }
                        }
                        if(k != 0 && (i + k >= 0 && i + k < dim)){
                            if((j + k >= 0 && j + k < dim) && board[i+k][j+k]){
                                valid = false;
                            }
                            if(((j - k < dim) && (j - k >= 0)) && board[i+k][j-k]){
                                valid = false;
                            }
                        }
                    }
                }
            }
        }

        if(valid) System.out.println("CORRECT");
        else System.out.println("INCORRECT");
    }
}
