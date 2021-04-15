import java.util.*;

public class countBrackets
{
    public static boolean checkBrackets(String strs)
    {   
        Map<Character,Character> bracketPair = new HashMap<Character,Character>();
        bracketPair.put('(', ')');
        bracketPair.put('[', ']');
        bracketPair.put('{', '}');
        
        Stack<Character> charStack = new Stack<Character>();

              for(int i =0;i<strs.length();i++)
              {

                  if(bracketPair.containsKey(strs.charAt(i))){
                    charStack.push(strs.charAt(i));
                  }
                  else if(bracketPair.containsValue(strs.charAt(i))){
                      if(charStack.isEmpty()||bracketPair.get(charStack.pop())!=strs.charAt(i))
                      return false;
                  }
              }
      
        if(charStack.isEmpty()){
            return true;
        }
        else {
            return false;
        }
    }
        
    

    public static void main (String [] args )
    {   String check = "{[(())]()}";
        String checkTwo = "{[(()])()}";
        System.out.println(countBrackets.checkBrackets(check));
        System.out.println(countBrackets.checkBrackets(checkTwo));
    }
}
