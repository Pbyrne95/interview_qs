import java.util.*;
import java.io.*;

public class MatchBrack {


    public boolean isMatched( String expression){
        String opening = "({[";
        String closing = ")}]";

        Stack<String> buffer = new Stack<String>();

        for(char c : expression.toCharArray()){
            if(opening.indexOf(c) != -1){
                buffer.push(String.valueOf(c));
            }
            else if( closing.indexOf(c) != -1){
                if(buffer.isEmpty()){
                    return false;
                }
                if(closing.indexOf(c) != opening.indexOf(buffer.pop())){
                    return false;
                }
            }

        }
        return buffer.isEmpty();

    }

    // public static void main(String[] args ){
    //     MatchBrack test = new MatchBrack();
    //     // System.out.println( test.isMatched("[(5+x)-[y+z]]") );
    // }

}
