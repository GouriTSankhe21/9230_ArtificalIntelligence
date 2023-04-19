import java.util.Scanner;

public class TicTacToe {

    public static void main(String[] args) {

        char[][] board = new char[3][3];
        initializeBoard(board);

        char currentPlayer = 'X';

        boolean gameFinished = false;

        while (!gameFinished) {
            displayBoard(board);

            int[] move = getPlayerMove(board, currentPlayer);
            int row = move[0];
            int col = move[1];

            board[row][col] = currentPlayer;

            if (checkForWin(board, currentPlayer)) {
                displayBoard(board);
                System.out.println("Player " + currentPlayer + " wins!");
                gameFinished = true;
            } else if (checkForTie(board)) {
                displayBoard(board);
                System.out.println("It's a tie!");
                gameFinished = true;
            } else {
                currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
            }
        }
    }

    public static void initializeBoard(char[][] board) {
        for (int row = 0; row < board.length; row++) {
            for (int col = 0; col < board[row].length; col++) {
                board[row][col] = ' ';
            }
        }
    }

    public static void displayBoard(char[][] board) {
        for (int row = 0; row < board.length; row++) {
            System.out.print("| ");
            for (int col = 0; col < board[row].length; col++) {
                System.out.print(board[row][col] + " | ");
            }
            System.out.println();
        }
    }

    public static int[] getPlayerMove(char[][] board, char player) {
        Scanner scanner = new Scanner(System.in);

        int row = -1;
        int col = -1;

        while (row < 0 || row > 2 || col < 0 || col > 2 || board[row][col] != ' ') {
            System.out.print("Player " + player + ", enter your move (row[0-2] column[0-2]): ");
            row = scanner.nextInt();
            col = scanner.nextInt();
        }

        return new int[] {row, col};
    }

    public static boolean checkForWin(char[][] board, char player) {
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == player && board[i][1] == player && board[i][2] == player) {
                return true;
            }
            if (board[0][i] == player && board[1][i] == player && board[2][i] == player) {
                return true;
            }
        }
        if (board[0][0] == player && board[1][1] == player && board[2][2] == player) {
            return true;
        }
        if (board[0][2] == player && board[1][1] == player && board[2][0] == player) {
            return true;
        }
        return false;
    }

    public static boolean checkForTie(char[][] board) {
        for (int row = 0; row < board.length; row++) {
            for (int col = 0; col < board[row].length; col++) {
                if (board[row][col] == ' ') {
                    return false;
                }
            }
        }
        return true;
    }
}
