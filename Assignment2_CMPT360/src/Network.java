// Michael Angelo C. Adraincem
// MCA655 11208422
// Network.java Assignment2 Part A

import java.io.*;
import java.util.StringTokenizer;  
//****************
//START: READ ONLY
//****************
public class Network {
//****************
//END: READ ONLY
//****************

// YOU CAN DEFINE YOUR OWN FUNCTIONS HERE IF YOU REALLY NEED ONE

//****************
//START: READ ONLY
//****************

    /**     
	 * @param n : The number of packets
     * @param D : An array representing the packet ordering  
     * @return The performance metric for D
     */
    public static int metric(int []D, int n) {
//****************
//END: READ ONLY
//****************

		//WRITE YOUR NSID: MCA655
		
		//start: edit and write your code here
        /** Time complexity of O(n) **/
        int max = 0, min = 9999999;
		int index1 = 0, index2 = n;
		if (n == 0)
		    return 0;
		else {
            for (int i = 0; i < n; i++) {
                /** Get new max if current index is greater than current max's index **/
                if (max < D[i] && i < index2) {
                    max = D[i];
                    index1 = i;
                }
                /** Get new min if current index is less than current max's index **/
                if (min > D[n - 1 - i] && index1 < n - 1 - i) {
                    min = D[n - 1 - i];
                    index2 = n - 1 - i;
                }
            }
            return max - min;
        }
        //end: write your code here 
	 
		 
		
    }
//****************
//START: READ ONLY
//****************
    /**
     * Main Function.
     */
    public static void main(String[] args) {

        BufferedReader reader;
        File file = new File("output.txt");
		int n = 0;
		int []X= new int[1000];
		String line;
        try {
            reader = new BufferedReader(new FileReader("src/Network.txt"));
            BufferedWriter writer = new BufferedWriter(new FileWriter(file));            
            while(true){ 
				line = reader.readLine();
				if(line == null) break;				
				StringTokenizer st = new StringTokenizer(line, ",");
				n = 0;
				while (st.hasMoreTokens()) {  
					X[n] = Integer.parseInt(st.nextToken()); 
					//System.out.println(""+X[n]);					
					n++;
				} 
                writer.write(metric(X,n) + "\n");
            } 

            reader.close();
            writer.close();
        } catch (FileNotFoundException e) {
            System.out.println("Could not locate input file.");
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }

}
