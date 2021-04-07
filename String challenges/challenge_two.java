import java.util.ArrayList;
import java.util.Arrays;


public class challenge_two 
{
    public boolean is_rep(int[] arr_one, int[] arr_two)
    {
        int key  = arr_one[0];
        
        int index_to = this.BinarySearch(arr_two, key);
        if ( index_to == -1 && (arr_one.length == arr_one.length) == true) {
            return false;
        }
        else
        {   int are_start[] = Arrays.copyOfRange(arr_two, 0, index_to);
            int are_end[] = Arrays.copyOfRange(arr_two, index_to, arr_two.length);

            int check_arr[] = this.concat(are_end,are_start);

            return Arrays.equals(arr_one, check_arr);
          
        }

    }
    public int[] concat(int[] array1 , int[] array2)
    {

        int length = array1.length + array2.length;

        int[] result = new int[length];
        int pos = 0;
        for (int element : array1) {
            result[pos] = element;
            pos++;
        }

        for (int element : array2) {
            result[pos] = element;
            pos++;
        }
        return result;
    }
    public int BinarySearch(int[] arr , int value )
    {
        for( int i = 0; i < arr.length - 1; i ++)
        {
            if (arr[i] == value)
            {
                return i;
            }
        }
        return -1;
    }
    
    public static void main(String[] args)
    {
        int[] array1 = {1, 2, 3, 4, 5, 6, 7};
        int[] array2a = {4, 5, 6, 7, 8, 1, 2, 3};
        // isRotation(array1, array2a) should return false.
        int[] array2b = {4, 5, 6, 7, 1, 2, 3};
        // isRotation(array1, array2b) should return true.
        int[] array2c = {4, 5, 6, 9, 1, 2, 3};
        // isRotation(array1, array2c) should return false.
        int[] array2d = {4, 6, 5, 7, 1, 2, 3};
        // isRotation(array1, array2d) should return false.
        int[] array2e = {4, 5, 6, 7, 0, 2, 3};
        // isRotation(array1, array2e) should return false.
        int[] array2f = {1, 2, 3, 4, 5, 6, 7};
        // isRotation(array1, array2f) should return true.
        challenge_two test = new challenge_two();

        System.out.println(test.is_rep( array1, array2b )); // true
        System.out.println(test.is_rep( array1, array2c )); // false
        System.out.println(test.is_rep( array1, array2d )); // false
        System.out.println(test.is_rep( array1, array2e )); // false
        System.out.println(test.is_rep( array1, array2f )); // true
        System.out.println(test.is_rep( array1, array2a )); // false
 
    }   
}
