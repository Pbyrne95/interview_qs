import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;


public class challenge_one {
    public Integer get_most_occ(int[] arr)
    {   System.out.println(Arrays.toString(arr));
        if (arr.length < 1)
        {
            return null;
        }

        Map<Integer,Integer> dict = new HashMap<Integer, Integer>();

        for (int i = 0 ; i < arr.length; i++)
        {
            Integer count = dict.get(arr[i]);
            if ( count == null )
            {
                dict.put(arr[i],1);
            } else {
                dict.put(arr[i], count + 1);
            }
        }
        return Collections.max(dict.entrySet(), Comparator.comparingInt(Map.Entry::getValue)).getKey();
    }

    public static void main( String [] args)
    {
        challenge_one test = new challenge_one();

   
        int[] array1 = {1, 3, 1, 3, 2, 1};
        // mostFrequent(array2) should return 3.
        int[] array2 = {3, 3, 1, 3, 2, 1};
        // mostFrequent(array3) should return null.
        int[] array3 = {};
        // mostFrequent(array4) should return 0.
        int[] array4 = {0};
        // mostFrequent(array5) should return -1.
        int[] array5 = {0, -1, 10, 10, -1, 10, -1, -1, -1, 1};

        System.out.println(test.get_most_occ(array3));
    }
}
