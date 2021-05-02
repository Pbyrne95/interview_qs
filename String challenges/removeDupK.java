import java.util.*;

public class removeDupK {

    public String uniqueChars( String chrs ){
        StringBuilder returnString =  new StringBuilder();
        char comp = chrs.charAt(0);
        returnString.insert(0, chrs.charAt(0));

        for (int i = 1 ; i < chrs.toCharArray().length ; i ++ ){
            if ( comp != chrs.charAt(i)  ){
                returnString.append(chrs.charAt(i));
            }
            comp = chrs.charAt(i);
        }

        return returnString.toString();
    }

    public String cutAfterK( String chrs , int k ){
        HashMap<Character,Integer> freq = new HashMap<Character,Integer>();

        for ( Character c : chrs.toCharArray() ){
            if ( c == ' '){
                continue;
            }
            else if ( freq.get(c) == null ){
                freq.put(c,1);
            }
            else{
                freq.put(c,freq.get(c) + 1);
            }
        }
        
        boolean check = freq.keySet().toArray().length == 1;

        StringBuilder toReturn = new StringBuilder();
        for (Map.Entry<Character, Integer> entry : freq.entrySet()) {
            Integer value = entry.getValue();
            if (check){
                return entry.getKey().toString().repeat(value);
            }
            else if((int) value  == 1 || (int) value > k){
                String key = entry.getKey().toString().repeat(value);
                toReturn.append(this.uniqueChars(key));
            }
            
        }
        
        return toReturn.toString();
    }
    
    public String removeDuplicates(String s, int k) {
        char sSort[] = s.toCharArray();
        Arrays.sort(sSort);
        for( int i = 0 ; i < sSort.length - 2 ; i++){
            String temp = String.valueOf(Arrays.copyOfRange(sSort , i , i + 3));
            if ( this.uniqueChars(temp).length() == 1 ){
                s = s.replace(s.charAt(i), ' ');
            }
        }
       
        return this.cutAfterK(s,k);
    }

    public static void main( String[] args ){
        removeDupK temp = new removeDupK();

        System.out.println(temp.removeDuplicates("deeedbbcccbdaa", 3));
        System.out.println(temp.removeDuplicates("abcd", 2));
        System.out.println(temp.removeDuplicates("pbbcggttciiippooaais", 2));
    }
}
