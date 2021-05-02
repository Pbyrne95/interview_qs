import java.util.Arrays;

public class SortingAlgos {
    // Looking at different divide and conquer algorythms
    // they work by dibide into parts 
    // finding solutions to each each part

    // constructing the final answer from the subsolutions 
    // often divide and conquer algorithmns are called recursively 

    // recursive examle for sumOfSquares 
    public int sumOfSquares ( int n ){
        if (n == 1){
            return 1;
        }
        else{
            return (n * n + sumOfSquares(n-1));
        }
    }


    public void merge( int arr[] , int p , int q , int r ){
        int n1 = q - p + 1;
        int n2 = r - q;

        int L[] = new int[n1];
        int M[] = new int[n2];

        for (int i = 0; i < n1; i++)
            L[i] = arr[p + i];
        for (int j = 0; j < n2; j++)
            M[j] = arr[q + 1 + j];

        int i, j, k;
        i = 0;
        j = 0;
        k = p;

        while (i < n1 && j < n2) {
            if (L[i] <= M[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = M[j];
                j++;
            }
            k++;
            }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = M[j];
            j++;
            k++;
            }
    }      

    public int[] mergeSort(int arr[], int l, int r){
        if( l < r ){
            int m = (l+r)/2;

            mergeSort(arr, l, m);
            mergeSort(arr, m+1, r);
            merge( arr , l , m , r );
        }
        return arr;
    }

    static void swop(int[] arr , int i , int j ){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static int partirtion(int[] array, int low, int high){
        int pivot = array[high];
        int i = (low - 1);

        for(int j = low ; j <= high -1  ; j++){
            if ( array[j] < pivot ){
                i++;
                swop(array , i , j);
            }
        }
        swop(array , i+1 , high );
        return (i+1);
    }

    public void quickSort( int[] array , int low , int high ){
        // splits from index p to q for given array 
        // index p to m and from m+1 to q 
        // solves the parts recursively 
        // and recombines them into a recursive solution 
        if (low < high){
               
        int p = partirtion( array , low , high );
        
        quickSort(array, low, p - 1);
        quickSort(array, p+1 , high);

        }
    }
    
    public static void main(String args[]){
        // SortingAlgos test = new SortingAlgos();

        int arr[] = { 6, 5, 12, 10, 9, 1 };
        int arrQS[] = {2,1,4,13,14,12,3,16,5,2,10};

        SortingAlgos ob = new SortingAlgos();
        ob.mergeSort(arr, 0, arr.length - 1);
    
        System.out.println("Sorted array:");

        ob.quickSort(arrQS, 0 , arrQS.length - 1);
        
        System.out.println( Arrays.toString( arrQS ) );
        

    }
}
