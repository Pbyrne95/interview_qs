import java.util.Arrays;

public class MS {

    public static int[][] insert_warnings(int[][] arr)
    {   
        for ( int idx = 0 ; idx < arr.length ; idx ++)
        {   
            // define outer loop rules 

            boolean check_up = idx - 1 <= 0;
            boolean check_down = idx + 1 < arr.length;
            boolean check_left = idx - 1 < 0 ; 
            boolean cheak_right = idx + 1 < arr.length;

            for ( int j = 0 ; j < arr[idx].length ; j ++)
            {   
                // define inner loop rules
                int upward_pos = idx - 1;
                int downward =  idx + 1;
                int up_right = j + 1;
                int up_left = j - 1;
                int current_pos = arr[idx][j];

                if ( up_left >= 0 )
                {
                    if ( arr[idx][up_left] == - 1 && current_pos >= 0)
                    {
                        arr[idx][j] += 1;
                    }
                }
                if ( up_right < arr[idx].length )
                {
                    if ( arr[idx][up_right] == -1 && current_pos >= 0 )
                    {
                        arr[idx][j] += 1;
                    }
                }

            }
        }


        return arr;
    }
    public static void main(String[] args) {
        // NOTE: The following input values will be used for testing your solution.
        int[][] bombs1 = {{0, 2}, {2, 0}};
        int[][] field = mineSweeper(bombs1, 3, 3);
        System.out.println(Arrays.deepToString(field)); // should return:
        // [[0, 1, -1],
        //  [1, 2, 1],
        //  [-1, 1, 0]]

        int[][] bombs2 = {{0, 0}, {0, 1}, {1, 2}};
        // mineSweeper(bombs2, 3, 4) should return:
        // [[-1, -1, 2, 1],
        //  [2, 3, -1, 1],
        //  [0, 1, 1, 1]]

        int[][] bombs3 = {{1, 1}, {1, 2}, {2, 2}, {4, 3}};
        // mineSweeper(bombs3, 5, 5) should return:
        // [[1, 2, 2, 1, 0],
        //  [1, -1, -1, 2, 0],
        //  [1, 3, -1, 2, 0],
        //  [0, 1, 2, 2, 1],
        //  [0, 0, 1, -1, 1]]
    }

    // Implement your solution below.
    public static int[][] mineSweeper(int[][] bombs, int numRows, int numCols) {
        int[][] field = new int[numRows][numCols];
        for ( int i = 0 ; i < field.length ; i ++)
        {
            for ( int j = 0 ; j < field[i].length ; j ++)
            {
                field[i][j] = 0;
            }
        }
        for ( int i = 0 ; i < bombs.length ; i ++){
                int index = bombs[i][0];
                int insert_bomb = bombs[i][1];

                field[index][insert_bomb] = -1;
        }
        return field;
    }
 }