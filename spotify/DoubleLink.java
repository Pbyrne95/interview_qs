import java.util.*;

public class DoubleLink
{   

    private ListNode head;
    private ListNode tail;
    private int length;


    private class ListNode
    {
        private int data;
        private ListNode next;
        private ListNode previous;

        public ListNode(int data)
        {
            this.data = data;
        }

    }

    public DoubleLink()
    {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    public List<Integer> showNodes()
    {   
        List<Integer> allNodes = new ArrayList<Integer>();

        if(this.head == null)
        {
            return allNodes;
        }
        else
        {
            ListNode peek = head;
            int iterations = 0;
            while(peek != null )
            {
                Integer addPeek = (Integer) peek.data;
                allNodes.add(addPeek);
                peek = peek.next;
            }

            return allNodes;

        }
    }


    public boolean isEmpty()
    {
        return ( this.length == 0 );
    }

    public int length()
    {
        return this.length;
    }

    public void insertFirst( int value )
    {
        ListNode newNode = new ListNode(value);

        if(this.isEmpty()){
            tail = newNode;
        }else{
            head.previous = newNode;
        }


        newNode.next = head;
        head = newNode;
        this.length++;
    }

    public void insertTail( int value )
    {
        ListNode newTailNode = new ListNode(value);

        if(isEmpty()){

            head = newTailNode;
        }else{

            tail.next = newTailNode;
            newTailNode.previous = tail;
        }
        tail = newTailNode;
    }

    public DoubleLink.ListNode removeNode( int value )
    {
        ListNode searchNode = head;

        if(isEmpty() || (! this.showNodes().contains((Integer) value) ) ) {
            throw new NoSuchElementException( " There is nothing to remove " );
        }

        ListNode toRemove = new ListNode( value );

        if (head.data == toRemove.data ){
            head = head.next;
            length--;
            return head;
        }

        if ( tail.data == toRemove.data ){
            ListNode temp = tail.previous;
            tail.previous.next = null;
            tail = temp;
            length--;
            return tail;
        }

        

        else{
            
            while ( searchNode != null )
            {
                if( searchNode.data == toRemove.data ){
                    ListNode temp = searchNode.next;
                    searchNode.previous.next = temp;
                    length--;
                    break; 
                }
                searchNode = searchNode.next;
            }


        }
        return searchNode;

    }

    public Integer getHead()
    {
        return (Integer) head.data;
    }

    public Integer getTail()
    {
        return (Integer) tail.data;
    }

    public static void main ( String [] args )
    {
        DoubleLink test = new DoubleLink();
        test.insertFirst(4);
        test.insertFirst(3);
        test.insertFirst(2);
        test.insertFirst(1); 
        test.removeNode(4);
        test.insertTail(6);
        System.out.println(test.showNodes());
        
    }
}