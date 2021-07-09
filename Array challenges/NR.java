import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class NR {
    public Map<Character, Integer>  dict = new HashMap<Character,Integer>();

    public boolean checkKey(char c)
    {
        if (dict.containsKey(c))
        {
            return true;
        }
        return false;
    }
    public Map<Character, Integer> putIntoMap( String chars )
    {   
        for ( int i = 0; i <= chars.length()-1; i++ )
        {
            boolean charGet = this.checkKey(chars.charAt(i));
            
            if (charGet == false)
            {   int count = (Integer) 1;
                this.dict.put(chars.charAt(i) , (Integer) count);
            } else
            {   int countNew = this.dict.get(chars.charAt(i));
                
                this.dict.put(chars.charAt(i), (Integer) countNew + 1 );
            }
        }    
        return this.dict;
    }
    public static void main(String[] args) {
        // NOTE: The following input values will be used for testing your solution.
        nonRepeating("abcab"); // should return 'c'
        nonRepeating("abab"); // should return null
        nonRepeating("aabbbc"); // should return 'c'
        nonRepeating("aabbdbc"); // should return 'd'
    }

    // Implement your solution below.
    public static Character nonRepeating(String s) {
        NR test = new NR();
        Map<Character, Integer> dict = test.putIntoMap(s);
        
        for( char c: s.toCharArray())
        {
            if(dict.get(c) == 1){      
                return c;
            }
        }
        return null;
    }
}